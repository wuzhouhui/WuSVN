%bcond_with fsfswd
%bcond_without swig
%bcond_without tools
%bcond_without devel
%bcond_with timestamp
%bcond_without check

%define apache_version 2.2.3
%define apr_version 1.2.7
%define apu_version 1.2.7
%define swig_version 1.3.29
%define apache_dir /usr
%define pyver 2.7

%define perl_siteprefix %(eval "`%{__perl} -V:installarchlib`"; echo $installarchlib)

Summary: A Modern Concurrent Versioning system.
Name: subversion
Version: 1.10.7
Release: 1%{?dist}
License: Apache 2.0
Group: Utilities/System
URL: http://www.wandisco.com

Source: %{name}-1.10.3.tar.gz
Source1: sqlite-amalgamation-3081101.zip
Source2: subversion.conf

%if %{with timestamp}
Patch0: timestamp-replication-v5-1.8.txt
%endif
Patch1: 0001-Add-alias-rv-for-subcommand-revert.patch
Patch2: 0002-Add-a-macro-define-SVN_IGNORE_FILE.patch
Patch3: 0003-Add-a-field-svn_ignore_fd-in-struct-svn_sqlite__db_t.patch
Patch4: 0004-Open-.svnignore-if-it-existed.patch
Patch5: 0005-Close-.svnignore-in-apr-cleanup-function.patch
Patch6: 0006-Support-.svnignore.patch
Patch7: 0007-Ignore-nothing-in-default.patch
Patch8: 0008-Using-vi-as-default-editor.patch
Patch9: 0009-Aborting-commit-automatically-if-message-is-empty.patch
Patch10: 0010-Paging-output-automatically.patch
Patch11: 0011-Only-paging-output-of-blame-cat-di-log-st-list-and-h.patch
Patch12: 0012-Fix-wrong-judgement-about-subcommand.patch
Patch13: 0013-Paging-output-only-if-the-stdout-is-terminal.patch
Patch14: 0014-Support-syntax-highlighting.patch
Patch15: 0015-Enable-syntax-highlight-only-if-stdout_is_tty-is-set.patch
Patch16: 0016-Print-paths-with-color-in-diff-mode.patch
Patch17: 0017-Pring-hunk-header-with-color-yellow.patch
Patch18: 0018-Pring-log-header-with-color-magenta.patch
Patch19: 0019-Add-an-option-no-color-to-log-and-diff-for-disabling.patch
Patch20: 0020-Revert-commit-b1b3e25cc4ba75eb205a44c93f4110c6353862.patch
Patch21: 0021-Update-output-of-svn-help-in-testing-script.patch
Patch22: 0022-Fix-a-segmentation-fault-check-parameter-whether-is-.patch
Patch23: 0023-Reset-color-after-hunk-delimiter-printed.patch
Patch24: 0024-Enable-extension-option-p-in-default.patch
Patch25: 0025-Make-sure-parent-terminates-after-pager.patch
Patch26: 0026-Add-email-address-of-hacker.patch
Patch27: 0027-Add-option-v-verbose-for-svn-commit.patch
Patch28: 0028-Add-my-copyright-in-svn-version.patch
Patch29: 0029-Update-description-of-option-no-ignore.patch
Patch30: 0030-Add-subcommand-clean-for-removing-unversioned-files-.patch
Patch31: 0031-Subcommand-clean-support-removing-non-empty-director.patch
Patch32: 0032-Subcommand-clean-print-some-info-when-deleting-file-.patch
Patch33: 0033-Subcommand-clean-add-option-no-ignore.patch
Patch34: 0034-Update-description-of-subcommand-clean.patch
Patch35: 0035-Update-description-of-option-v-in-subcommand-commit.patch
Patch36: 0036-Subcommand-clean-stat-the-link-if-that-file-is-a-sym.patch
Patch37: 0037-README-add-main-patches-that-I-made.patch
Patch38: 0038-Update-expected-output-of-testing-script.patch
Patch39: 0039-Update-expected-output-of-testing-script.patch
Patch40: 0040-Update-the-order-of-expected-output.patch
Patch41: 0041-Subcmd-clean-remove-files-only-if-option-force-enabl.patch
Patch42: 0042-More-accurate-diff-output-when-svn-ci-v.patch
Patch43: 0043-Using-relative-path-to-reduce-memory-usage.patch
Patch44: 0044-Using-new-added-field-diff_relpath-in-verbose-commit.patch
Patch45: 0045-Subcommand-diff-add-option-stat-to-display-statistic.patch
Patch46: 0046-Subcommand-log-add-option-stat-to-show-statistics-of.patch
Patch47: 0047-Revert-Subcommand-log-add-option-stat-to-show-statis.patch
Patch48: 0048-Reimplementing-subcommand-log-s-option-stat-via-diff.patch
Patch49: 0049-option-stat-and-diff-are-not-mutual-exclusion.patch
Patch50: 0050-Output-newline-before-diff-statistics.patch
Patch51: 0051-Add-option-p0-to-diffstat-program.patch
Patch52: 0052-Reimplementation-of-option-stat-of-subcommand-diff.patch
Patch53: 0053-Remove-unused-functions-plot_round1-and-plot_round2.patch
Patch54: 0054-Initialize-max_width-to-80-instead-of-0.patch
Patch55: 0055-Remove-unused-field-from-struct-svn_dfstat_ctx_s.patch
Patch56: 0056-Fix-compile-error-introduced-by-cherry-pick.patch
Patch57: 0057-Implement-svn-di-cr-stat.patch
Patch58: 0058-Update-README-for-option-stat.patch
Patch59: 0059-Complete-a-TODO-in-diff_content_changed.patch
Patch60: 0060-Patching-subversion-1.9.4-diffstat-binary.patch.patch
Patch61: 0061-Update-expected-output-of-svn-help-log.patch
Patch62: 0062-Add-bash-completion-of-new-option-and-subcommand.patch
Patch63: 0063-I-think-we-should-not-paging-svn-version.patch
Patch64: 0064-Update-README.patch
Patch65: 0065-Adjust-max-width-of-diffstat-according-terminal-widt.patch
Patch66: 0066-Scale-max-width-for-diffstat-for-better-look.patch
Patch67: 0067-Remove-extra-EOL-marker-when-getting-log-from-editor.patch
Patch68: 0068-New-implementation-of-option-v-for-subcommand-ci.patch
Patch69: 0069-Remove-some-unused-local-variables-in-svn_cmdline__e.patch
Patch70: 0070-Write-newline-before-diff-for-svn-ci-with-option-v.patch
Patch71: 0071-New-year.patch
Patch72: 0072-Using-vi-if-no-other-editor-found.patch
Patch73: 0073-Set-properties-only-only-when-path-is-a-directory.patch
Patch74: 0074-Ignore-property-changes-when-option-stat-setted.patch
Patch75: 0075-Update-expected-output-of-svn-help-log.patch
Patch76: 0076-Add-some-comments-for-convenience.patch
Patch77: 0077-Do-not-set-properties_only-if-item-deleted-is-a-dir.patch
Patch78: 0078-Strip-extra-EOL-when-get-log-message-from-file.patch
Patch79: 0079-svn-auth-output-paging-automatically.patch
Patch80: 0080-diff-highlight-trailing-blanks-of-local-changes.patch
Patch81: 0081-clean-don-t-print-anything-about-changelist.patch
Patch82: 0082-svn-clean-add-option-dry-run.patch
Patch83: 0083-svn-clean-add-option-ignore.patch
Patch84: 0084-Set-no_peg_revision-of-do_diff-properly.patch
Patch85: 0085-Update-README.patch
Patch86: 0086-Revert-Enable-extension-option-p-in-default.patch
Patch87: 0087-test-update-expected-output-of-svn-help-diff.patch
Patch88: 0088-svn-print-information-of-hacker.patch
Patch89: 0089-Upstream-1.10.4.patch
Patch90: 0090-Put-functions-and-data-structs-of-hacker-into-privat.patch
Patch91: 0091-svn-ci-support-client-side-hooks-only-pre-commit-for.patch
Patch92: 0092-svn-ci-add-option-bypass-hooks-to-skip-all-client-si.patch
Patch93: 0093-Update-README-to-include-new-name-of-this-software.patch
Patch94: 0094-svn-ci-resolve-symlinks-when-check-pre-commit-hook.patch
Patch95: 0095-svn-mergeinfo-paging-outputs-of-svn-mergeinfo.patch
Patch96: 0001-svn-shelve-decrease-max-width-of-outputs.patch
Patch97: 0002-Upstream-1.10.6.patch
Patch98: 0001-svn-shelve-do-not-exec-external-tools-when-diffstat.patch
Patch99: 0002-svn-shelve-do-not-print-newline-if-log-message-is-em.patch
Patch100: 0001-svn-ci-support-hook-post-commit-in-client-side.patch
Patch101: 0002-svn-ci-extract-common-code-from-pre-post_commit.patch
Patch102: 0001-svn-log-remove-unnecessary-exclusion-between-option-.patch
Patch103: 0001-Upstream-1.10.7.patch

Vendor: WANdisco Inc
Packager: WANdisco Inc <opensource@wandisco.com>

Requires: apr >= %{apr_version}
Requires: apr-util >= %{apu_version}

BuildRequires: qt4-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: dbus-devel
BuildRequires: kdelibs-devel
BuildRequires: docbook-style-xsl >= 1.58.1
BuildRequires: doxygen
BuildRequires: expat-devel
BuildRequires: gettext
BuildRequires: httpd-devel >= %{apache_version}
BuildRequires: apr-devel >= %{apr_version}
BuildRequires: apr-util-devel >= %{apr_version}
BuildRequires: libxslt >= 1.0.27
BuildRequires: openssl-devel
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: python-devel
BuildRequires: swig >= %{swig_version}
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: libserf-devel

Obsoletes: subversion-server
Obsoletes: subversion-libs
Obsoletes: subversion < %{svn_ver}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Prefix: /usr
%description
Subversion is a concurrent version control system which enables one or more
users to collaborate in developing and maintaining a hierarchy of files and
directories while keeping a history of all changes.  Subversion only stores
the differences between versions, instead of every complete file.  Subversion
also keeps a log of who, when, and why changes occurred.

As such it basically does the same thing CVS does (Concurrent Versioning System)
but has major enhancements compared to CVS and fixes a lot of the annoyances
that CVS users face.

*** Note: This is a relocatable package; it can be installed anywhere you like
with the "rpm -Uvh --prefix /your/favorite/path" command. This is useful
if you don't have root access on your machine but would like to use this
package.

%if !%{without devel}
%package devel
Group: Utilities/System
Summary: Development package for Subversion developers.
Requires: subversion = %{version}-%{release}
%description devel
The subversion-devel package includes the static libraries and include files
for developers interacting with the subversion package.
%endif

%package gnome
Group: Development/Tools
Summary: GNOME Keyring support for Subversion
Requires: subversion = %{version}-%{release}

%description gnome
The subversion-gnome package adds support for storing Subversion
passwords in the GNOME Keyring.

%package -n mod_dav_svn
Group: Utilities/System
Summary: Apache server module for Subversion server.
Requires: subversion = %{version}-%{release}
Requires: httpd >= %{apache_version}
%description -n mod_dav_svn
The mod_dav_svn package adds the Subversion server Apache module to
the Apache directories and configuration.

%if !%{without swig}
%package perl
Group: Utilities/System
Summary: Allows Perl scripts to directly use Subversion repositories.
Requires: perl
%description perl
Provides Perl (SWIG) support for Subversion.

%package python
Group: Utilities/System
Summary: Allows Python scripts to directly use Subversion repositories.
Requires: python >= 2
%description python
Provides Python (SWIG) support for Subversion.
%endif

%package javahl
Group: Utilities/System
Summary: Allows java scripts to directly use Subversion repositories.
%description javahl
Provides Java (jni/c++) oracle jdk6 support for Subversion.

%if !%{without swig}
%package tools
Group: Utilities/System
Summary: Tools for Subversion
%description tools
Tools for Subversion.
%endif

%if %{with fsfswd}
%package fsfswd
Group: Utilities/System
Summary: WANdisco extensions to subversion
%description fsfswd
WANdisco extensions to subversion
%endif

%prep
%setup -n subversion-1.10.3
%{?_with_timestamp:%patch0 -p0}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1

echo "Putting SQLite in to place"
rm -rf sqlite-amalgamation
unzip %{SOURCE1}
mv sqlite-amalgamation-3081101 sqlite-amalgamation

# Delete apr, apr-util, and neon from the tree as those packages should already
# be installed.
rm -rf apr apr-util neon

PYTHON=/usr/bin/python2.7
export PYTHON

%configure \
	--disable-mod-activation \
	%{?_without_swig} \
	--with-berkeley-db \
	--with-apxs=%{apache_dir}/bin/apxs \
	--with-apr=%{apache_dir}/bin/apr-1-config \
	--with-apr-util=%{apache_dir}/bin/apu-1-config \
	--with-apache-libexecdir=yes \
	--with-old-gnome-keyring \
	--enable-javahl \
	--with-jdk=${JAVA_HOME} \
	--without-jikes \
	--with-sqlite=sqlite-amalgamation/sqlite3.c \
	--with-lz4=internal \
	--with-utf8proc=internal \
	--enable-apache-whitelist=2.4.6 \
  	--with-serf
%build
make clean

# build javahl - needs to be done before the plain make for fsfswd to succeed
make javahl %{?_with_fsfswd:javahl-java-fsfswd}

make

%if !%{without swig}
# Build python bindings
make swig-py swig-pl DESTDIR=$RPM_BUILD_ROOT
%endif

%if !%{without tools}
# Build tools
make tools
%endif

%if !%{without check}
%check
make check
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{apache_dir}/conf
make install %{!?_without_tools:install-tools} DESTDIR="$RPM_BUILD_ROOT"
%if !%{without tools}
# Fix broken symlink
rm -r $RPM_BUILD_ROOT/%{_bindir}/svn-tools/svnmucc
ln -s %{_bindir}/svnmucc $RPM_BUILD_ROOT/%{_bindir}/svn-tools/svnmucc
%endif

# install javahl
make install-javahl %{?_with_fsfswd: install-javahl-java-fsfswd} DESTDIR="$RPM_BUILD_ROOT"


# Add subversion.conf configuration file into httpd/conf.d directory.
mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.d
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/httpd/conf.d

%if !%{without swig}
# Install Python SWIG bindings.
make install-swig-py DESTDIR=$RPM_BUILD_ROOT DISTUTIL_PARAM=--prefix=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages
mv $RPM_BUILD_ROOT/%{_libdir}/svn-python/* $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages
rmdir $RPM_BUILD_ROOT/%{_libdir}/svn-python

# Install PERL SWIG bindings.
make install-swig-pl DESTDIR=$RPM_BUILD_ROOT

# Clean up unneeded files for package installation
rm -rf $RPM_BUILD_ROOT/%{_libdir}/perl5/%{perl_version}
%endif

# Create doxygen documentation.
%{!?_without_devel:doxygen doc/doxygen.conf}

%post -n mod_dav_svn
# Restart apache server if needed.
source /etc/init.d/functions
if [ "`pidof httpd`"x != "x" ]; then
   /etc/init.d/httpd restart || true
fi

%postun -n mod_dav_svn
# Restart apache server if needed.
source /etc/init.d/functions
if [ "`pidof httpd`"x != "x" ]; then
   /etc/init.d/httpd restart || true
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BUGS CHANGES COMMITTERS INSTALL README LICENSE
%{_bindir}/svn
%{_bindir}/svnadmin
%{_bindir}/svndumpfilter
%{_bindir}/svnlook
%{_bindir}/svnserve
%{_bindir}/svnsync
%{_bindir}/svnversion
%{_bindir}/svnrdump
%{_bindir}/svnfsfs
%{_libdir}/libsvn_client*so*
%{_libdir}/libsvn_delta*so*
%{_libdir}/libsvn_diff*so*
%{_libdir}/libsvn_fs*so*
%{_libdir}/libsvn_ra*so*
%{_libdir}/libsvn_repos*so*
%{_libdir}/libsvn_subr*so*
%{_libdir}/libsvn_wc*so*
/usr/share/locale/*/*/*
/usr/share/man/man1/*
/usr/share/man/man5/*
/usr/share/man/man8/*
%{!?_without_swig: %exclude %{_libdir}/libsvn_swig_perl*}
%exclude %{_libdir}/libsvn_auth_gnome*
%{?_with_fsfswd: %exclude %{_libdir}/*fsfswd*.so*}
%{?_without_tools: %exclude %{_bindir}/svnmucc}
%{?_without_devel: %exclude %{_includedir}/subversion-1}
%{?_without_devel: %exclude %{_libdir}/*.a}
%{?_without_devel: %exclude %{_libdir}/*.la}

%if !%{without devel}
%files devel
%defattr(-,root,root)
%doc doc/doxygen/html/*
%{_libdir}/libsvn*.a
%{_libdir}/libsvn*.la
/usr/include/subversion-1
/usr/share/pkgconfig/*
%endif

%files -n mod_dav_svn
%defattr(-,root,root)
%config(noreplace) /etc/httpd/conf.d/subversion.conf
%{_libdir}/httpd/modules/mod_dav_svn.so
%{_libdir}/httpd/modules/mod_authz_svn.so
%{!?_without_tools: %{_libdir}/httpd/modules/mod_dontdothat.so}

%files gnome
%defattr(-,root,root)
%{_libdir}/libsvn_auth_gnome_keyring-*.so.*

%if !%{without swig}
%files perl
%defattr(-,root,root)
%{perl_siteprefix}/SVN
%{perl_siteprefix}/auto/SVN
%{_libdir}/libsvn_swig_perl*so*
%{_mandir}/man3/SVN*
%{perl_archlib}/perllocal.pod

%files python
%defattr(-,root,root)
%{_libdir}/python%{pyver}/site-packages/svn
%{_libdir}/python%{pyver}/site-packages/libsvn
%{_libdir}/libsvn_swig_py*so*
%endif

%files javahl
%defattr(-,root,root)
%{_libdir}/libsvnjavahl*.so*
%{_libdir}/svn-javahl/svn-javahl.jar

%if %{with fsfswd}
%files fsfswd
%defattr(-,root,root)
%{_bindir}/resequence
%{_libdir}/svn-javahl/svn-javahl-fsfswd.jar
%{_libdir}/*fsfswd*.so*
%endif

%if !%{without tools}
%files tools
%defattr(-,root,root)
%{_bindir}/svnmucc
%{_bindir}/svn-tools
%{_bindir}/svnbench
%endif

%changelog
* Fri Feb 12 2021 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.10.7-1
- Upstream 1.10.7

* Sun Apr  5 2020 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.10.6-5
- Disable runtime module search

* Mon Dec 23 2019 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.10.6-4
- svn/log: remove unnecessary exclusion between option quiet and diff

* Thu Aug 15 2019 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.10.6-3
- svn/ci: support hook post-commit in client side
- svn/ci: extract common code from pre/post_commit

* Tue Aug  6 2019 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.10.6-2
- svn/shelve: do not exec external tools when diffstat
- svn/shelve: do not print newline if log message is empty

* Sat Jul 20 2019 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.10.6-1
- svn/shelve: decrease max width of outputs
- Upstream 1.10.6

* Sat Jun  8 2019 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.10.4-1
- svn/mergeinfo: paging outputs of svn mergeinfo
- svn/ci: resolve symlinks when check pre-commit hook
- Update README to include new name of this software
- svn/ci: add option --bypass-hooks to skip all client side hooks
- svn/ci: support client side hooks, only pre-commit for now
- Put functions and data structs of hacker into private header
- Upstream 1.10.4
- svn: print information of hacker
- test: update expected output of svn help diff
- Revert "Enable extension option -p in default"
- Update README
- Set no_peg_revision of do_diff() properly.
- svn/clean: add option --ignore
- svn/clean: add option --dry-run
- clean: don't print anything about changelist
- diff: highlight trailing blanks of local changes
- svn/auth: output paging automatically
- Strip extra EOL when get log message from file
- Do not set properties_only if item deleted is a dir
- Add some comments for convenience
- Update expected output of svn help log
- Ignore property changes when option --stat setted
- Set properties-only only when path is a directory
- Using vi if no other editor found
- New year
- Write newline before diff for svn ci with option -v
- Remove some unused local variables in svn_cmdline__edit_string_externally_v
- New implementation of option -v for subcommand ci
- Remove extra EOL marker when getting log from editor
- Scale max width for diffstat, for better look
- Adjust max width of diffstat according terminal width
- Update README
- I think we should not paging svn --version
- Add bash completion of new option and subcommand
- Update expected output of svn help log
- Patching subversion-1.9.4-diffstat-binary.patch
- Complete a TODO in diff_content_changed
- Update README for option --stat
- Implement svn di -[cr] --stat
- Fix compile error introduced by cherry-pick
- Remove unused field from struct svn_dfstat_ctx_s
- Initialize max_width to 80, instead of 0
- Remove unused functions: plot_round1 and plot_round2
- Reimplementation of option --stat of subcommand diff
- Add option -p0 to diffstat program
- Output newline before diff statistics
- option --stat and --diff are not mutual exclusion
- Reimplementing subcommand log's option --stat via diffstat's source
- Revert "Subcommand log: add option --stat to show statistics of diff"
- Subcommand log: add option --stat to show statistics of diff
- Subcommand diff: add option --stat to display statistics of diff
- Using new added field diff_relpath in verbose commit
- Using relative path to reduce memory usage
- More accurate diff output when "svn ci -v"
- Subcmd clean: remove files only if option --force enabled
- Update the order of expected output
- Update expected output of testing script
- Update expected output of testing script
- README: add main patches that I made
- Subcommand clean: stat the link if that file is a symbolic link
- Update description of option -v in subcommand commit
- Update description of subcommand clean
- Subcommand clean: add option --no-ignore
- Subcommand clean: print some info when deleting file or dir
- Subcommand clean support removing non-empty directory
- Add subcommand clean for removing unversioned files and empty directories
- Update description of option --no-ignore
- Add my copyright in svn --version
- Add option -v[--verbose] for svn commit.
- Add email address of hacker
- Make sure parent terminates after pager
- Enable extension option -p in default
- Reset color after hunk delimiter printed
- Fix a segmentation fault: check parameter whether is null before calling strcmp().
- Update output of svn help in testing script
- Revert commit b1b3e25cc4ba75eb205a44c93f4110c635386218
- Add an option '--no-color' to log and diff, for disabling syntax highlight
- Pring log header with color magenta
- Pring hunk header with color yellow
- Print paths with color in diff mode
- Enable syntax highlight only if stdout_is_tty is set
- Support syntax highlighting
- Paging output only if the stdout is terminal
- Fix wrong judgement about subcommand
- Only paging output of blame, cat, di, log, st, list, and help
- Paging output automatically
- Aborting commit automatically if message is empty
- Using vi as default editor
- Ignore nothing in default
- Support .svnignore
- Close .svnignore in apr cleanup function
- Open .svnignore if it existed
- Add a field "svn_ignore_fd" in struct svn_sqlite__db_t
- Add a macro define: SVN_IGNORE_FILE
- Add alias "rv" for subcommand revert

* Sat Feb 23 2019 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.10.3-1
- Subversion 1.10.3, nothing touched
- src.rpm downloaded from http://opensource.wandisco.com
