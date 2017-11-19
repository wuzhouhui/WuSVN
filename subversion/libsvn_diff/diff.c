/*
 * diff.c :  routines for doing diffs
 *
 * ====================================================================
 *    Licensed to the Apache Software Foundation (ASF) under one
 *    or more contributor license agreements.  See the NOTICE file
 *    distributed with this work for additional information
 *    regarding copyright ownership.  The ASF licenses this file
 *    to you under the Apache License, Version 2.0 (the
 *    "License"); you may not use this file except in compliance
 *    with the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *    Unless required by applicable law or agreed to in writing,
 *    software distributed under the License is distributed on an
 *    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *    KIND, either express or implied.  See the License for the
 *    specific language governing permissions and limitations
 *    under the License.
 * ====================================================================
 */


#include <apr.h>
#include <apr_pools.h>
#include <apr_general.h>

#include "svn_pools.h"
#include "svn_error.h"
#include "svn_diff.h"
#include "svn_types.h"

#include "diff.h"
#include "private/svn_color.h"


svn_diff__token_index_t*
svn_diff__get_token_counts(svn_diff__position_t *loop_start,
                           svn_diff__token_index_t num_tokens,
                           apr_pool_t *pool)
{
  svn_diff__token_index_t *token_counts;
  svn_diff__token_index_t token_index;
  svn_diff__position_t *current;

  token_counts = apr_palloc(pool, num_tokens * sizeof(*token_counts));
  for (token_index = 0; token_index < num_tokens; token_index++)
    token_counts[token_index] = 0;

  current = loop_start;
  if (current != NULL)
    {
      do
        {
          token_counts[current->token_index]++;
          current = current->next;
        }
      while (current != loop_start);
    }

  return token_counts;
}


svn_diff_t *
svn_diff__diff(svn_diff__lcs_t *lcs,
               apr_off_t original_start, apr_off_t modified_start,
               svn_boolean_t want_common,
               apr_pool_t *pool)
{
  svn_diff_t *diff;
  svn_diff_t **diff_ref = &diff;

  while (1)
    {
      if (original_start < lcs->position[0]->offset
          || modified_start < lcs->position[1]->offset)
      {
          (*diff_ref) = apr_palloc(pool, sizeof(**diff_ref));

          (*diff_ref)->type = svn_diff__type_diff_modified;
          (*diff_ref)->original_start = original_start - 1;
          (*diff_ref)->original_length =
            lcs->position[0]->offset - original_start;
          (*diff_ref)->modified_start = modified_start - 1;
          (*diff_ref)->modified_length =
            lcs->position[1]->offset - modified_start;
          (*diff_ref)->latest_start = 0;
          (*diff_ref)->latest_length = 0;

          diff_ref = &(*diff_ref)->next;
      }

      /* Detect the EOF */
      if (lcs->length == 0)
          break;

      original_start = lcs->position[0]->offset;
      modified_start = lcs->position[1]->offset;

      if (want_common)
        {
          (*diff_ref) = apr_palloc(pool, sizeof(**diff_ref));

          (*diff_ref)->type = svn_diff__type_common;
          (*diff_ref)->original_start = original_start - 1;
          (*diff_ref)->original_length = lcs->length;
          (*diff_ref)->modified_start = modified_start - 1;
          (*diff_ref)->modified_length = lcs->length;
          (*diff_ref)->latest_start = 0;
          (*diff_ref)->latest_length = 0;

          diff_ref = &(*diff_ref)->next;
        }

      original_start += lcs->length;
      modified_start += lcs->length;

      lcs = lcs->next;
    }

  *diff_ref = NULL;

  return diff;
}


svn_error_t *
svn_diff_diff_2(svn_diff_t **diff,
                void *diff_baton,
                const svn_diff_fns2_t *vtable,
                apr_pool_t *pool)
{
  svn_diff__tree_t *tree;
  svn_diff__position_t *position_list[2];
  svn_diff__token_index_t num_tokens;
  svn_diff__token_index_t *token_counts[2];
  svn_diff_datasource_e datasource[] = {svn_diff_datasource_original,
                                        svn_diff_datasource_modified};
  svn_diff__lcs_t *lcs;
  apr_pool_t *subpool;
  apr_pool_t *treepool;
  apr_off_t prefix_lines = 0;
  apr_off_t suffix_lines = 0;

  *diff = NULL;

  subpool = svn_pool_create(pool);
  treepool = svn_pool_create(pool);

  svn_diff__tree_create(&tree, treepool);

  SVN_ERR(vtable->datasources_open(diff_baton, &prefix_lines, &suffix_lines,
                                   datasource, 2));

  /* Insert the data into the tree */
  SVN_ERR(svn_diff__get_tokens(&position_list[0],
                               tree,
                               diff_baton, vtable,
                               svn_diff_datasource_original,
                               prefix_lines,
                               subpool));

  SVN_ERR(svn_diff__get_tokens(&position_list[1],
                               tree,
                               diff_baton, vtable,
                               svn_diff_datasource_modified,
                               prefix_lines,
                               subpool));

  num_tokens = svn_diff__get_node_count(tree);

  /* The cool part is that we don't need the tokens anymore.
   * Allow the app to clean them up if it wants to.
   */
  if (vtable->token_discard_all != NULL)
    vtable->token_discard_all(diff_baton);

  /* We don't need the nodes in the tree either anymore, nor the tree itself */
  svn_pool_destroy(treepool);

  token_counts[0] = svn_diff__get_token_counts(position_list[0], num_tokens,
                                               subpool);
  token_counts[1] = svn_diff__get_token_counts(position_list[1], num_tokens,
                                               subpool);

  /* Get the lcs */
  lcs = svn_diff__lcs(position_list[0], position_list[1], token_counts[0],
                      token_counts[1], num_tokens, prefix_lines,
                      suffix_lines, subpool);

  /* Produce the diff */
  *diff = svn_diff__diff(lcs, 1, 1, TRUE, pool);

  /* Get rid of all the data we don't have a use for anymore */
  svn_pool_destroy(subpool);

  return SVN_NO_ERROR;
}



/******************************************************************************
 * Copyright 1994-2015,2016 by Thomas E. Dickey                               *
 * All Rights Reserved.                                                       *
 *                                                                            *
 * Permission to use, copy, modify, and distribute this software and its      *
 * documentation for any purpose and without fee is hereby granted, provided  *
 * that the above copyright notice appear in all copies and that both that    *
 * copyright notice and this permission notice appear in supporting           *
 * documentation, and that the name of the above listed copyright holder(s)   *
 * not be used in advertising or publicity pertaining to distribution of the  *
 * software without specific, written prior permission.                       *
 *                                                                            *
 * THE ABOVE LISTED COPYRIGHT HOLDER(S) DISCLAIM ALL WARRANTIES WITH REGARD   *
 * TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND  *
 * FITNESS, IN NO EVENT SHALL THE ABOVE LISTED COPYRIGHT HOLDER(S) BE LIABLE  *
 * FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES          *
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN      *
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR *
 * IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.                *
 ******************************************************************************/

#ifndef	NO_IDENT
static const char *Id = "$Id: diffstat.c,v 1.61 2016/01/14 00:52:29 tom Exp $";
#endif

/*
 * Title:	diffstat.c
 * Author:	T.E.Dickey
 * Created:	02 Feb 1992
 * Modified:
 *		14 Jan 2016, extend -S option to count unmodified files.
 *			     add -T option to show values with histogram
 *		06 Jul 2015, handle double-quotes, e.g., from diffutils 3.3
 *			     when filenames have embedded spaces.
 *		05 Jun 2014, add -E option to filter colordiff output.
 *		28 Oct 2013, portability improvements for MinGW.
 *		15 Apr 2013, modify to accommodate output of "diff -q", which
 *			     tells only if the files are different.  Work
 *			     around the equivalent ambiguous message introduced
 *			     in diffutils 2.8.4 and finally removed for 3.0
 *		11 Feb 2013, add -K option.  Use strtol() to provide error
 *			     checking of optarg values.
 *		10 Feb 2013, document -b, -C, -s option in usage (patch by
 *			     Tim Waugh, Red Hat #852770).  Improve pathname
 *			     merging.
 *		02 Jun 2012, fix for svn diff with spaces in path (patch by
 *			     Stuart Prescott, Debian #675465).
 *		03 Jan 2012, Correct case for "xz" suffix in is_compressed()
 *			     (patch from Frederic Culot in FreeBSD ports).  Add
 *			     "-R" option.  Improve dequoting of filenames in
 *			     headers.
 *		10 Oct 2010, correct display of new files when -S/-D options
 *			     are used.  Remove the temporary directory on
 *			     error, introduced in 1.48+ (patch by Solar
 *			     Designer).
 *		19 Jul 2010, add missing "break" statement which left "-c"
 *			     option falling-through into "-C".
 *		16 Jul 2010, configure "xz" path explicitly, in case lzcat
 *			     does not support xz format.  Add "-s" (summary)
 *			     and "-C" (color) options.
 *		15 Jul 2010, fix strict gcc warnings, e.g., using const.
 *		10 Jan 2010, improve a case where filenames have embedded blanks
 *			     (patch by Reinier Post).
 *		07 Nov 2009, correct suffix-check for ".xz" files as
 *			     command-line parameters rather than as piped
 *			     input (report by Moritz Barsnick).
 *		06 Oct 2009, fixes to build/run with MSYS or MinGW.  use
 *			     $TMPDIR for path of temporary file used in
 *			     decompression.  correct else-condition for
 *			     detecting compression type (patch by Zach Hirsch).
 *		31 Aug 2009, improve lzma support, add support for xz (patch by
 *			     Eric Blake).  Add special case for no-newline
 *			     message from some diff's (Ubuntu #269895).
 *			     Improve configure check for getopt().
 *		11 Aug 2009, Add logic to check standard input, decompress if
 *			     possible.  Add -N option, to truncate long names.
 *			     Add pack/pcat as a compression type.
 *			     Add lzma/lzcat as a compression type.
 *			     Allow overriding program paths with environment.
 *		10 Aug 2009, modify to work with Perforce-style diffs (patch
 *			     by Ed Schouten).
 *		29 Mar 2009, modify to work with patch ".rej" files, which have
 *			     no filename header (use the name of the ".rej"
 *			     file if it is available).
 *		29 Sep 2008, fix typo in usage message.
 *		06 Aug 2008, add "-m", "-S" and "-D" options.
 *		05 Aug 2008, add "-q" option to suppress 0-files-changed
 *			     message (patch by Greg Norris).
 *		04 Sep 2007, add "-b" option to suppress binary-files (patch
 *			     by Greg Norris).
 *		26 Aug 2007, add "-d" option to show debugging traces, rather
 *			     than by defining DEBUG.  Add check after
 *			     unified-diff chunk to avoid adding non-diff text
 *			     (report by Adrian Bunk).  Quote pathname passed
 *			     in command to gzip/uncompress.  Add a check for
 *			     default-diff output without the "diff" command
 *			     supplied to provide filename, mark as "unknown".
 *		16 Jul 2006, fix to avoid modifying which is being used by
 *			     tsearch() for ordering the binary tree (report by
 *			     Adrian Bunk).
 *		02 Jul 2006, do not ignore pathnames in /tmp/, since some tools
 *			     create usable pathnames for both old/new files
 *			     there (Debian #376086).  Correct ifdef for
 *			     fgetc_unlocked().  Add configure check for
 *			     compress, gzip and bzip2 programs that may be used
 *			     to decompress files.
 *		24 Aug 2005, update usage message for -l, -r changes.
 *		15 Aug 2005, apply PLURAL() to num_files (Jean Delvare).
 *			     add -l option (request by Michael Burian).
 *			     Use fgetc_locked() if available.
 *		14 Aug 2005, add -r2 option (rounding with adjustment to ensure
 *			     that nonzero values always display a histogram
 *			     bar), adapted from patch by Jean Delvare.  Extend
 *			     the -f option (2=filled, 4=verbose).
 *		12 Aug 2005, modify to use tsearch() for sorted lists.
 *		11 Aug 2005, minor fixes to scaling of modified lines.  Add
 *			     -r (round) option.
 *		05 Aug 2005, add -t (table) option.
 *		10 Apr 2005, change order of merging and prefix-stripping so
 *			     stripping all prefixes, e.g., with -p9, will be
 *			     sorted as expected (Patch by Jean Delvare
 *			     <khali@linux-fr.org>).
 *		10 Jan 2005, add support for '--help' and '--version' (Patch
 *			     by Eric Blake <ebb9@byu.net>.)
 *		16 Dec 2004, fix a different case for data beginning with "--"
 *			     which was treated as a header line.
 *		14 Dec 2004, Fix allocation problems.  Open files in binary
 *			     mode for reading.  Getopt returns -1, not
 *			     necessarily EOF.  Add const where useful.  Use
 *			     NO_IDENT where necessary.  malloc() comes from
 *			     <stdlib.h> in standard systems (Patch by Eric
 *			     Blake <ebb9@byu.net>.)
 *		08 Nov 2004, minor fix for resync of unified diffs checks for
 *			     range (line beginning with '@' without header
 *			     lines (successive lines beginning with "---" and
 *			     "+++").  Fix a few problems reported by valgrind.
 *		09 Nov 2003, modify check for lines beginning with '-' or '+'
 *			     to treat only "---" in old-style diffs as a
 *			     special case.
 *		14 Feb 2003, modify check for filenames to allow for some cases
 *			     of incomplete dates (the reported example omitted
 *			     the day of the month).  Correct a typo in usage().
 *			     Add -e, -h, -o options.
 *		04 Jan 2003, improve tracking of chunks in unified diff, in
 *			     case the original files contained a '+' or '-' in
 *			     the first column (Debian #155000).  Add -v option
 *			     (Debian #170947).  Modify to allocate buffers big
 *			     enough for long input lines.  Do additional
 *			     merging to handle unusual Index/diff constructs in
 *			     recent makepatch script.
 *		20 Aug 2002, add -u option to tell diffstat to preserve the
 *			     order of filenames as given rather than sort them
 *			     (request by H Peter Anvin <hpa@zytor.com>).  Add
 *			     -k option for completeness.
 *		09 Aug 2002, allow either '/' or '-' as delimiters in dates,
 *			     to accommodate diffutils 2.8 (report by Rik van
 *			     Riel <riel@conectiva.com.br>).
 *		10 Oct 2001, add bzip2 (.bz2) suffix as suggested by
 *			     Gregory T Norris <haphazard@socket.net> in Debian
 *			     bug report #82969).
 *			     add check for diff from RCS archive where the
 *			     "diff" lines do not reference a filename.
 *		29 Mar 2000, add -c option.  Check for compressed input, read
 *			     via pipe.  Change to ANSI C.  Adapted change from
 *			     Troy Engel to add option that displays a number
 *			     only, rather than a histogram.
 *		17 May 1998, handle Debian diff files, which do not contain
 *			     dates on the header lines.
 *		16 Jan 1998, accommodate patches w/o tabs in header lines (e.g.,
 *			     from cut/paste).  Strip suffixes such as ".orig".
 *		24 Mar 1996, corrected -p0 logic, more fixes in do_merging.
 *		16 Mar 1996, corrected state-change for "Binary".  Added -p
 *			     option.
 *		17 Dec 1995, corrected matching algorithm in 'do_merging()'
 *		11 Dec 1995, mods to accommodate diffs against /dev/null or
 *			     /tmp/XXX (tempfiles).
 *		06 May 1995, limit scaling -- only shrink-to-fit.
 *		29 Apr 1995, recognize 'rcsdiff -u' format.
 *		26 Dec 1994, strip common pathname-prefix.
 *		13 Nov 1994, added '-n' option.  Corrected logic of 'match'.
 *		17 Jun 1994, ifdef-<string.h>
 *		12 Jun 1994, recognize unified diff, and output of makepatch.
 *		04 Oct 1993, merge multiple diff-files, busy message when the
 *			     output is piped to a file.
 *
 * Function:	this program reads the output of 'diff' and displays a histogram
 *		of the insertions/deletions/modifications per-file.
 */

#if defined(HAVE_CONFIG_H)
#include <config.h>
#endif

#if defined(WIN32) && !defined(HAVE_CONFIG_H)
#define HAVE_STDLIB_H
#define HAVE_STRING_H
#define HAVE_MALLOC_H
#define HAVE_GETOPT_H
#endif

#include <stdio.h>
#include <ctype.h>

#ifdef HAVE_STRING_H
#include <string.h>
#else
#include <strings.h>
#define strchr index
#define strrchr rindex
#endif

#ifdef HAVE_STDLIB_H
#include <stdlib.h>
#else
extern int atoi(const char *);
#endif

#ifdef HAVE_UNISTD_H
#include <unistd.h>
#else
extern int isatty(int);
#endif

#ifdef HAVE_OPENDIR
#include <dirent.h>
#endif

#ifdef HAVE_MALLOC_H
#include <malloc.h>
#endif

#if defined(HAVE_SEARCH_H) && defined(HAVE_TSEARCH)
#include <search.h>
#else
#undef HAVE_TSEARCH
#endif

#ifdef HAVE_GETC_UNLOCKED
#define MY_GETC getc_unlocked
#else
#define MY_GETC getc
#endif

#ifdef HAVE_GETOPT_H
#include <getopt.h>
#elif !defined(HAVE_GETOPT_HEADER)
extern int getopt(int, char *const *, const char *);
extern char *optarg;
extern int optind;
#endif

#include <sys/types.h>
#include <sys/stat.h>

#if defined(HAVE_POPEN) && !defined(HAVE_POPEN_PROTOTYPE)
extern FILE *popen(const char *, const char *);
extern int pclose(FILE *);
#endif

#if !defined(EXIT_SUCCESS)
#define EXIT_SUCCESS 0
#define EXIT_FAILURE 1
#endif

#ifndef BZCAT_PATH
#define BZCAT_PATH ""
#endif

#ifndef BZIP2_PATH
#define BZIP2_PATH ""
#endif

#ifndef COMPRESS_PATH
#define COMPRESS_PATH ""
#endif

#ifndef GZIP_PATH
#define GZIP_PATH ""
#endif

#ifndef LZCAT_PATH
#define LZCAT_PATH ""
#endif

#ifndef PCAT_PATH
#define PCAT_PATH ""
#endif

#ifndef UNCOMPRESS_PATH
#define UNCOMPRESS_PATH ""
#endif

#ifndef XZ_PATH
#define XZ_PATH ""
#endif

#ifndef ZCAT_PATH
#define ZCAT_PATH ""
#endif

/******************************************************************************/

#if defined(__MINGW32__) || defined(WIN32)
#define MKDIR(name,mode) mkdir(name)
#else
#define MKDIR(name,mode) mkdir(name,mode)
#endif

#if defined(WIN32) && !defined(__MINGW32__)
#define PATHSEP '\\'
#else
#define PATHSEP '/'
#endif

#define DQUOTE  '"'
#define SQUOTE  '\''
#define EOS     '\0'
#define BLANK   ' '

#define UC(c)   ((unsigned char)(c))

#ifndef OPT_TRACE
#define OPT_TRACE 1
#endif

#if OPT_TRACE
#define TRACE(p) if (trace_opt) printf p
#else
#define TRACE(p)		/*nothing */
#endif

#define contain_any(s,reject) (strcspn(s,reject) != strlen(s))
#define maximum(a,b) ((a) < (b) ? (b) : (a))

#define HAVE_NOTHING 0
#define HAVE_GENERIC 1		/* e.g., "Index: foo" w/o pathname */
#define HAVE_PATH    2		/* reference-file from "diff dirname/foo" */
#define HAVE_PATH2   4		/* comparison-file from "diff dirname/foo" */

#define FMT_CONCISE  0
#define FMT_NORMAL   1
#define FMT_FILLED   2
#define FMT_VERBOSE  4

typedef enum comment {
    Normal, Only, OnlyLeft, OnlyRight, Binary, Differs, Either
} Comment;

#define MARKS 4			/* each of +, - and ! */

typedef enum {
    cInsert = 0,
    cDelete,
    cModify,
    cEquals
} Change;

typedef svn_dfstat_ctx_t DATA;

#define InsOf(p) (p)->inserted_num	/* "+" count inserted lines */
#define DelOf(p) (p)->deleted_num	/* "-" count deleted lines */

#define TotalOf(p) (InsOf(p) + DelOf(p))
#define for_each_mark(n) for (n = 0; n < num_marks; ++n)


static const char marks[MARKS + 1] = "+-!=";
static const int colors[MARKS + 1] =
{2, 1, 6, 4};

static const char *comment_opt = "";
static char *path_opt = 0;
static int count_files;		/* true if we count added/deleted files */
static int format_opt = FMT_NORMAL;
static int max_name_wide;	/* maximum amount reserved for filenames */
static int max_width = 80;		/* the specified width-limit */
static int merge_names = 1;	/* true if we merge similar filenames */
static int merge_opt = 0;	/* true if we merge ins/del as modified */
static int min_name_wide;	/* minimum amount reserved for filenames */
static int names_only;		/* true if we list filenames only */
static int num_marks = 3;	/* 3 or 4, according to "-P" option */
static int path_dest;		/* true if path_opt is destination (patched) */
static int plot_width;		/* the amount left over for histogram */
static int prefix_opt = 0;	/* if positive, controls stripping of PATHSEP */
static int quiet = 0;		/* -q option */
static int reverse_opt;		/* true if results are reversed */
static int round_opt = 0;	/* if nonzero, round data for histogram */
#define show_colors (!dont_use_color)	/* true if showing SGR colors */
static int show_progress;	/* if not writing to tty, show progress */
static int sort_names = 1;	/* true if we sort filenames */
static int summary_only = 0;	/* true if only summary line is shown */
static int suppress_binary = 0;	/* -b option */
static int trim_escapes = 0;	/* -E option */
static int table_opt = 0;	/* if 1/2, write table instead/also plot */
static int trace_opt = 0;	/* if nonzero, write debugging information */
static int unchanged = 0;	/* special-case for -S vs modified-files */
static int verbose = 0;		/* -v option */
static long plot_scale;		/* the effective scale (1:maximum) */

static int number_len = 5;
static int prefix_len = -1;

/******************************************************************************/

static int
compare_data(const void *a, const void *b)
{
    const DATA *p = (const DATA *) a;
    const DATA *q = (const DATA *) b;
    return strcmp(p->file_path + p->base, q->file_path + q->base);
}

static int
count_prefix(const char *name)
{
    int count = 0;
    const char *s;
    while ((s = strchr(name, PATHSEP)) != 0) {
	name = s + 1;
	++count;
    }
    return count;
}

static const char *
skip_prefix(const char *name, int prefix, int *base)
{
    if (prefix >= 0) {
	int n;
	*base = 0;

	for (n = prefix; n > 0; n--) {
	    const char *s = strchr(name + *base, PATHSEP);
	    if (s == 0 || *++s == EOS) {
		name = s;
		break;
	    }
	    *base = (int) (s - name);
	}
	TRACE(("** base set to %d\n", *base));
    }
    return name;
}


static void
show_color(int color)
{
    if (color >= 0)
	printf("\033[%dm", color + 30);
    else
	printf("\033[0;39m");
}

static long
plot_bar(long count, int c, int color)
{
    long result = count;

    if (show_colors && result != 0)
	show_color(color);

    while (--count >= 0)
	(void) putchar(c);

    if (show_colors && result != 0)
	show_color(-1);

    return result;
}

/*
 * Each call to 'plot_num()' prints a scaled bar of 'c' characters.  The
 * 'extra' parameter is used to keep the accumulated error in the bar's total
 * length from getting large.
 */
static long
plot_num(long num_value, int c, int color, long *extra)
{
    long product;
    long result = 0;

    /* the value to plot */
    /* character to display in the bar */
    /* accumulated error in the bar */
    if (num_value) {
	product = (plot_width * num_value);
	result = ((product + *extra) / plot_scale);
	*extra = product - (result * plot_scale) - *extra;
	plot_bar(result, c, color);
    }
    return result;
}

static void
plot_numbers(const DATA * p)
{
    long temp = 0;
    long used = 0;
    int i;

    printf("%5ld ", TotalOf(p));

    if (format_opt & FMT_VERBOSE) {
	printf("%5ld ", InsOf(p));
	printf("%5ld ", DelOf(p));
    }

    if (format_opt == FMT_CONCISE) {
	printf("\t%ld %c", p->inserted_num, marks[0]);
	printf("\t%ld %c", p->deleted_num, marks[1]);
    } else {
	switch (round_opt) {
	default:
	    used += plot_num(p->inserted_num, marks[0], colors[0], &temp);
	    used += plot_num(p->deleted_num, marks[1], colors[1], &temp);
	    break;
	}

	if ((format_opt & FMT_FILLED) != 0) {
	    if (used > plot_width)
		printf("%ld", used - plot_width);	/* oops */
	    else
		plot_bar(plot_width - used, '.', 0);
	}
    }
}

static char *
data_filename(const DATA * p)
{
    return p ? (p->file_path + (prefix_opt >= 0 ? p->base : prefix_len)) : "";
}

static void
show_data(DATA * p)
{
    char *name = data_filename(p);
    int width;

    if (summary_only) {
	;
    } else if (table_opt == 1) {
	if (names_only) {
	    printf("%s\n", name);
	} else {
	    printf("%ld,%ld,",
		   InsOf(p),
		   DelOf(p));
	    printf("%s\n", name);
	}
    } else if (names_only) {
	printf("%s\n", name);
    } else {
	printf("%s ", comment_opt);
	if (max_name_wide > 0
	    && max_name_wide < min_name_wide
	    && max_name_wide < ((width = (int) strlen(name)))) {
	    printf("%.*s", max_name_wide, name + (width - max_name_wide));
	} else {
	    width = ((max_name_wide > 0 && max_name_wide < min_name_wide)
		     ? max_name_wide
		     : min_name_wide);
	    printf("%-*.*s", width, width, name);
	}
	if (table_opt == 2) {
	    putchar('|');
	    printf("%*ld ", number_len, InsOf(p));
	    printf("%*ld ", number_len, DelOf(p));
	}
	putchar('|');
	if (p->cmt == svn_dfstat_bin)
		printf("binary");
	else
		plot_numbers(p);
	printf("\n");
    }
}

#ifdef HAVE_TSEARCH
static void
show_tsearch(const void *nodep, const VISIT which, const int depth)
{
    const DATA *p = *(DATA * const *) nodep;
    (void) depth;
    if (which == postorder || which == leaf)
	show_data(p);
}
#endif


/*
 * Return the length of any directory-prefix from the given path.
 */
static size_t
path_length(const char *path)
{
    size_t result = 0;
    char *mark = strrchr(path, PATHSEP);
    if (mark != 0 && mark != path)
	result = (size_t) (mark + 1 - path);
    return result;
}


static void
update_min_name_wide(long longest_name)
{
    if (prefix_opt < 0) {
	if (prefix_len < 0)
	    prefix_len = 0;
	if ((longest_name - prefix_len) > min_name_wide)
	    min_name_wide = (longest_name - prefix_len);
    }

    if (min_name_wide < 1)
	min_name_wide = 0;
    min_name_wide++;		/* make sure it's nonzero */
}

static void
summarize(DATA *all_data)
{
    DATA *p;
    long total_ins = 0;
    long total_del = 0;
    long total_mod = 0;
    long total_eql = 0;
    long files_added = 0;
    long files_equal = 0;
    long files_binary = 0;
    long files_removed = 0;
    long temp;
    int num_files = 0, shortest_name = -1, longest_name = -1;

    plot_scale = 0;
    for (p = all_data; p; p = p->next) {
	int len = (int) strlen(p->file_path);

	/*
	 * If "-pX" option is given, prefix_opt is positive.
	 *
	 * "-p0" gives the whole pathname unmodified.  "-p1" strips
	 * through the first path-separator, etc.
	 */
	if (prefix_opt >= 0) {
	    /* p->base has been computed at node creation */
	    if (min_name_wide < (len - p->base))
		min_name_wide = (len - p->base);
	} else {
	    /*
	     * If "-pX" option is not given, strip off any prefix which is
	     * shared by all of the names.
	     */
	    if (len < prefix_len || prefix_len < 0)
		prefix_len = len;
	    while (prefix_len > 0) {
		if (p->file_path[prefix_len - 1] != PATHSEP)
		    prefix_len--;
		else if (strncmp(all_data->file_path, p->file_path, (size_t) prefix_len))
		    prefix_len--;
		else
		    break;
	    }

	    if (len > longest_name)
		longest_name = len;
	    if (len < shortest_name || shortest_name < 0)
		shortest_name = len;
	}
    }

    /*
     * Use a separate loop after computing prefix_len so we can apply the "-S"
     * or "-D" options to find files that we can use as reference for the
     * unchanged-count.
     */
    for (p = all_data; p; p = p->next) {
	    if (reverse_opt) {
		long save_ins = InsOf(p);
		long save_del = DelOf(p);
		InsOf(p) = save_del;
		DelOf(p) = save_ins;
	    }
	    num_files++;
	    total_ins += InsOf(p);
	    total_del += DelOf(p);
	    temp = TotalOf(p);
	    if (temp > plot_scale)
		plot_scale = temp;
    }

    update_min_name_wide(longest_name);

    plot_width = (max_width - min_name_wide - 8);
    if (plot_width < 10)
	plot_width = 10;

    if (plot_scale < plot_width)
	plot_scale = plot_width;	/* 1:1 */

    if (table_opt == 1) {
	if (!names_only) {
	    printf("INSERTED,DELETED,MODIFIED,");
	    if (path_opt)
		printf("UNCHANGED,");
	    if (count_files && !reverse_opt)
		printf("FILE-ADDED,FILE-DELETED,FILE-BINARY,");
	}
	printf("FILENAME\n");
    } else if (table_opt == 2) {
	long largest = 0;
	for (p = all_data; p; p = p->next) {
	    largest = maximum(largest, InsOf(p));
	    largest = maximum(largest, DelOf(p));
	}
	number_len = 0;
	while (largest > 0) {
	    number_len++;
	    largest /= 10;
	}
	number_len = maximum(number_len, 3);
    }
	for (p = all_data; p; p = p->next) {
	    show_data(p);
	}

    if ((table_opt != 1) && !names_only) {
#define PLURAL(n) n, n != 1 ? "s" : ""
	if (num_files > 0 || !quiet) {
	    printf("%s %d file%s changed", comment_opt, PLURAL(num_files));
	    if (total_ins)
		printf(", %ld insertion%s(+)", PLURAL(total_ins));
	    if (total_del)
		printf(", %ld deletion%s(-)", PLURAL(total_del));
	    (void) putchar('\n');
	}
    }
}


static svn_dfstat_ctx_t dfctx;
static apr_pool_t *dfctx_pool;

svn_error_t *
svn_diff_create_dfctx(svn_dfstat_ctx_t **ctx)
{
  apr_status_t err = apr_pool_create(&dfctx_pool, NULL);
  if (err)
    svn_error_wrap_apr(err, "Create dfctx pool failed");
  memset(&dfctx, 0, sizeof(dfctx));
  *ctx = &dfctx;

  /* Re-initialize diffstat's static variables */
  path_opt = 0;
  count_files = 0;		/* true if we count added/deleted files */
  format_opt = FMT_NORMAL;
  max_name_wide = 0;	/* maximum amount reserved for filenames */

  max_width = 80;		/* the specified width-limit */
  if (tty_fileno >= 0)
    {
      struct winsize winsz;

      if (ioctl(tty_fileno, TIOCGWINSZ, (char *)&winsz) < 0)
        {
          fprintf(stderr, "get win size failed: %s\n", strerror(errno));
          exit(EXIT_FAILURE);
        }
      max_width = winsz.ws_col;
    }

  merge_names = 1;	/* true if we merge similar filenames */
  merge_opt = 0;	/* true if we merge ins/del as modified */
  min_name_wide = 0;	/* minimum amount reserved for filenames */
  names_only = 0;		/* true if we list filenames only */
  num_marks = 3;	/* 3 or 4, according to "-P" option */
  path_dest = 0;		/* true if path_opt is destination (patched) */
  plot_width = 0;		/* the amount left over for histogram */
  prefix_opt = 0;	/* if positive, controls stripping of PATHSEP */
  quiet = 0;		/* -q option */
  reverse_opt = 0;		/* true if results are reversed */
  round_opt = 0;	/* if nonzero, round data for histogram */
  show_progress = 0;	/* if not writing to tty, show progress */
  sort_names = 1;	/* true if we sort filenames */
  summary_only = 0;	/* true if only summary line is shown */
  suppress_binary = 0;	/* -b option */
  trim_escapes = 0;	/* -E option */
  table_opt = 0;	/* if 1/2, write table instead/also plot */
  trace_opt = 0;	/* if nonzero, write debugging information */
  unchanged = 0;	/* special-case for -S vs modified-files */
  verbose = 0;		/* -v option */
  plot_scale = 0;		/* the effective scale (1:maximum) */
  number_len = 5;
  prefix_len = -1;

  return SVN_NO_ERROR;
}


void
svn_diff_destroy_dfctx(svn_dfstat_ctx_t *ctx)
{
  ctx->next = NULL;
  apr_pool_destroy(dfctx_pool);
}


svn_error_t *
svn_diff_stat(svn_dfstat_ctx_t *head,
    const svn_diff_t *diff,
    const char *file_path,
    enum svn_dfstat_cmt cmt)
{
  svn_dfstat_ctx_t *t = apr_pcalloc(dfctx_pool, sizeof(*t));
  t->file_path = apr_pstrdup(dfctx_pool, file_path);
  t->cmt = cmt;
  t->next = head->next;
  head->next = (void *)t;
  while (diff)
    {
      if (diff->type == svn_diff__type_diff_modified)
        {
          t->inserted_num += diff->modified_length;
          t->deleted_num += diff->original_length;
        }
      diff = diff->next;
    }
  head->inserted_num += t->inserted_num;
  head->deleted_num += t->deleted_num;
  return SVN_NO_ERROR;
}

svn_error_t *
svn_diff_output_dfstat(svn_stream_t *outstream,
    svn_dfstat_ctx_t *head)
{
  summarize((DATA *)head->next);
  return SVN_NO_ERROR;
}
