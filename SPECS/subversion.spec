%bcond_with fsfswd
%bcond_without swig
%bcond_without tools
%bcond_without devel
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
Version: 1.13.0
Release: 2%{?dist}
License: Apache 2.0
Group: Utilities/System
URL: http://www.wandisco.com

Source: %{name}-1.13.0.tar.bz2
Source1: sqlite-amalgamation-3081101.zip
Source2: subversion.conf

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
%setup -n subversion-1.13.0

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
* Sun Apr  5 2020 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.13.0-2
- Disable runtime module search

* Tue Nov 12 2019 Wu Zhouhui <wuzhouhui250@gmail.com> - 1.13.0-1
- Subversion 1.13.0, nothing touched
