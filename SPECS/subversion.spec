%bcond_without tools
%bcond_without devel
%bcond_without check

%define apache_version 2.4.6
%define apr_version 1.4.8
%define apu_version 1.5.2
%define swig_version 2.0.10
%define apache_dir /usr
%define pyver 2.7
%define svn_version 1.9.10
%define svn_release 2%{?dist}

%define perl_siteprefix %(eval "`%{__perl} -V:installarchlib`"; echo $installarchlib)

Summary: A Modern Concurrent Versioning system.
Name: subversion
Version: %{svn_version}
Release: %{svn_release}
License: Apache 2.0
Group: Utilities/System
URL: https://github.com/wuzhouhui/subversion

Source: %{name}-1.9.7.tar.gz
Source1: sqlite-amalgamation-3210000.zip
Source2: subversion.conf

Patch1: for-1.9.7.patch
Patch2: 0001-New-implementation-of-option-v-for-subcommand-ci.patch
Patch3: 0002-Remove-some-unused-local-variables-in-svn_cmdline__e.patch
Patch4: 0003-Write-newline-before-diff-for-svn-ci-with-option-v.patch
Patch5: 0004-New-year.patch
Patch6: 0005-Using-vi-if-no-other-editor-found.patch
Patch7: 0006-Set-properties-only-only-when-path-is-a-directory.patch
Patch8: 0001-Ignore-property-changes-when-option-stat-setted.patch
Patch9: 0002-Update-expected-output-of-svn-help-log.patch
Patch10: 0001-Add-some-comments-for-convenience.patch
Patch11: 0002-Do-not-set-properties_only-if-item-deleted-is-a-dir.patch
Patch12: 0001-Strip-extra-EOL-when-get-log-message-from-file.patch
Patch13: SVNB-1866.patch
Patch14: shelve.patch
Patch15: 0001-shelve-limit-minimum-width-of-header-to-79-column.patch
Patch16: 0001-diff-highlight-trailing-blanks-of-local-changes.patch
Patch17: 0002-shelve-set-output-width-to-windows-s-col-minus-one.patch
Patch18: 0003-clean-don-t-print-anything-about-changelist.patch
Patch19: 0001-Upstream-1.9.9.patch
Patch20: 0002-svn-clean-add-option-dry-run.patch
Patch21: 0003-svn-clean-add-option-ignore.patch
Patch22: 0004-Update-README.patch
Patch23: 0005-Revert-Enable-extension-option-p-in-default.patch
Patch24: 0006-test-update-expected-output-of-svn-help-diff.patch
Patch25: 0007-svn-print-information-of-hacker.patch
Patch26: 0008-Upstream-1.9.10.patch
Patch27: 0001-Put-functions-and-data-structs-of-hacker-into-privat.patch
Patch28: 0002-svn-ci-support-client-side-hooks-only-pre-commit-for.patch
Patch29: 0003-svn-ci-add-option-bypass-hooks-to-skip-all-client-si.patch
Patch30: 0004-Update-README-to-include-new-name-of-this-software.patch
Patch31: 0005-svn-ci-resolve-symlinks-when-check-pre-commit-hook.patch
Patch32: 0006-Release-1.9.10.1.patch

Vendor: WANdisco Inc
Packager: WANdisco Inc <opensource@wandisco.com>

Requires: apr >= %{apr_version}
Requires: apr-util >= %{apu_version}
Requires: /bin/less

BuildRequires: qt4-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: dbus-devel
BuildRequires: kdelibs-devel
BuildRequires: libdb-devel >= 4.2.52
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
BuildRequires: swig >= %{swig_version}
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: libserf-devel

Obsoletes: subversion-server

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

%if %{with swig}
%package perl
Group: Utilities/System
Summary: Allows Perl scripts to directly use Subversion repositories.
Requires: perl
%description perl
Provides Perl (SWIG) support for Subversion.
%endif

%if %{with swig-py}
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

%if !%{without tools}
%package tools
Group: Utilities/System
Summary: Tools for Subversion
%description tools
Tools for Subversion.
%endif

%prep
%setup -n subversion-1.9.7
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
%patch13 -p0
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

echo "Putting SQLite in to place"
rm -rf sqlite-amalgamation
unzip %{SOURCE1}
mv sqlite-amalgamation-3210000 sqlite-amalgamation

# Delete apr, apr-util, and neon from the tree as those packages should already
# be installed.
rm -rf apr apr-util neon

export PYTHON=/usr/bin/python2.7

%configure \
	--disable-mod-activation \
	%{?_without_swig} \
	--with-berkeley-db \
	--with-apxs=%{apache_dir}/bin/apxs \
	--with-apr=%{apache_dir}/bin/apr-1-config \
	--with-apr-util=%{apache_dir}/bin/apu-1-config \
	--with-apache-libexecdir=yes \
	--with-gnome-keyring \
	--enable-javahl \
	--with-jdk=${JAVA_HOME} \
	--without-jikes \
	--with-sqlite=sqlite-amalgamation/sqlite3.c \
  --with-serf
%build
make clean

make %{?_smp_mflags}

# build javahl
make javahl

%if %{with swig}
# Build python bindings
make %{?_smp_mflags} swig-pl DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with swig-py}
# Build python bindings
make swig-py swig-pl DESTDIR=$RPM_BUILD_ROOT
%endif

%if !%{without tools}
# Build tools
make %{?_smp_mflags} tools
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
make install-javahl DESTDIR="$RPM_BUILD_ROOT"


# Add subversion.conf configuration file into httpd/conf.d directory.
mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.d
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/httpd/conf.d

%if %{with swig-py}
# Install Python SWIG bindings.
make install-swig-py DESTDIR=$RPM_BUILD_ROOT DISTUTIL_PARAM=--prefix=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages
mv $RPM_BUILD_ROOT/%{_libdir}/svn-python/* $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages
rmdir $RPM_BUILD_ROOT/%{_libdir}/svn-python
%endif

%if %{with swig}
# Install PERL SWIG bindings.
make install-swig-pl DESTDIR=$RPM_BUILD_ROOT

# Clean up unneeded files for package installation
rm -rf $RPM_BUILD_ROOT/%{_libdir}/perl5/%{perl_version}
%endif

# Create doxygen documentation.
%{!?_without_devel:doxygen doc/doxygen.conf}

# Install bash completion
install -Dpm 644 tools/client-side/bash_completion \
        $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}

%if !%{without check}
%check
make check
%endif

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
%{_sysconfdir}/bash_completion.d
/usr/share/locale/*/*/*
/usr/share/man/man1/*
/usr/share/man/man5/*
/usr/share/man/man8/*
%{!?_without_swig: %exclude %{_libdir}/libsvn_swig_perl*}
%exclude %{_libdir}/libsvn_auth_gnome*
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

%if %{with swig}
%files perl
%defattr(-,root,root)
%{perl_siteprefix}/SVN
%{perl_siteprefix}/auto/SVN
%{_libdir}/libsvn_swig_perl*so*
%{_mandir}/man3/SVN*
%{perl_archlib}/perllocal.pod
%endif

%if %{with swig-py}
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

%if !%{without tools}
%files tools
%defattr(-,root,root)
%{_bindir}/svnmucc
%{_bindir}/svn-tools
%{_bindir}/svnbench
%endif

%changelog
* Fri Apr 19 2019 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.10-2
- Put functions and data structs of hacker into private header
- svn/ci: support client side hooks, only pre-commit for now
- svn/ci: add option --bypass-hooks to skip all client side hooks
- Update README to include new name of this software
- svn/ci: resolve symlinks when check pre-commit hook
- Release 1.9.10.1

* Sat Feb 23 2019 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.10-1
- Require /bin/less, instead of less
- Require libgnome-keyring-devel when build
- Require libserf-devel when build, get it from http://opensource.wandisco.com
- Use env variable JAVA_HOME as argument of --with-jdk
- Upstream 1.9.9
- svn/clean: add option --dry-run
- svn/clean: add option --ignore
- Update README
- Revert "Enable extension option -p in default"
- test: update expected output of svn help diff
- svn: print information of hacker
- Upstream 1.9.10

* Sat Mar 31 2018 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.7-9
- diff: highlight trailing blanks of local changes
- shelve: set output width to windows's col minus one
- clean: don't print anything about changelist

* Thu Mar 22 2018 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.7-8
- shelve: limit minimum width of header to 79 column

* Fri Mar 16 2018 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.7-7
- New experimental subcommand shelve

* Thu Feb  1 2018 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.7-6
- Updated for rpmbuild in CentOS 7
- SVNB-1866.patch

* Sun Jan 14 2018 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.7-5
- Strip extra EOL when get log message from file

* Wed Jan 10 2018 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.7-4
- 0001-Add-some-comments-for-convenience.patch
- 0002-Do-not-set-properties_only-if-item-deleted-is-a-dir.patch
- Update URL to my GitHub repository

* Mon Jan  8 2018 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.7-3
- Add %{?dist} label in package name
- 0001-Ignore-property-changes-when-option-stat-setted.patch
- 0002-Update-expected-output-of-svn-help-log.patch

* Sat Jan  6 2018 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.7-2
- plain make before make javahl
- single threaded make javahl
- 0001-New-implementation-of-option-v-for-subcommand-ci.patch
- 0002-Remove-some-unused-local-variables-in-svn_cmdline__e.patch
- 0003-Write-newline-before-diff-for-svn-ci-with-option-v.patch
- 0004-New-year.patch
- 0005-Using-vi-if-no-other-editor-found.patch
- 0006-Set-properties-only-only-when-path-is-a-directory.patch

* Thu Dec 28 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.7-1
- for-1.9.7.patch

* Mon Dec 11 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-17
- 0001-Remove-extra-EOL-marker-when-getting-log-from-editor.patch

* Sun Nov 26 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-16
- SQLite upgrades to 3210000
- Remove macro svn_source

* Wed Nov 22 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-15
- 0001-I-think-we-should-not-paging-svn-version.patch
- 0002-Update-README.patch
- 0003-Adjust-max-width-of-diffstat-according-terminal-widt.patch
- 0004-Scale-max-width-for-diffstat-for-better-look.patch
- Using --without check to disable checking

* Thu Oct 26 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-14
- 0001-Add-bash-completion-of-new-option-and-subcommand
- Add bash_completion in package subversion
- Remove un-needed macro and related code
- subversion-1.9.4.testing.patch
- Remove --enable-runtime-module-search in configure, for make check.
- Add section check

* Fri Oct 20 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-13
- Sychronized with official subversion.spec

* Tue Oct 17 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-12
- subversion-1.9.4-diffstat-binary.patch

* Sun Oct 15 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-11
- 0001-Complete-a-TODO-in-diff_content_changed.patch

* Sat Oct 14 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-10
- 0001-Remove-unused-functions-plot_round1-and-plot_round2.patch
- 0002-Initialize-max_width-to-80-instead-of-0.patch
- 0003-Remove-unused-field-from-struct-svn_dfstat_ctx_s.patch
- 0004-Supress-binary-file-s-warnings-when-stat.patch
- 0005-Implement-svn-di-cr-stat.patch

* Mon Oct 9 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-9
- 0001-Reimplementation-of-option-stat-of-subcommand-diff.patch

* Sun Oct 8 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-8
- Add 0001-option-stat-and-diff-are-not-mutual-exclusion.patch
- Add 0002-Output-newline-before-diff-statistics.patch
- Add 0003-Add-option-p0-to-diffstat-program.patch

* Sun Oct 8 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-7
- Require diffstat >= 1.59

* Sun Oct 8 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-6
- subversion-1.9.4.dfstat-1.patch

* Sat Sep 2 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-5
- subversion-1.9.4.option-v.patch

* Fri Aug 11 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-4
- subversion-1.9.7.patch

* Thu Jul 6 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-3
- subversion-1.9.6.patch

* Fri Apr 14 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-2
- Subcmd-clean-remove-files-only-if-option-force-enabl.patch

* Mon Apr 3 2017 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.9.4-1
- First commit
- Add first patch: subversion-1.9.4.first_patch
