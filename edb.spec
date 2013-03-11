%define	name	edb
%define version 1.0.5.050
%define release 5

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Enlightenment database access library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source0: 	http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
BuildRequires:	ncurses-devel zlib-devel

%description
Edb is a simple, clean high-level db access/storage library.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %libname
Libraries for %{name}.

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{libname}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
%setup -q

%build
%configure2_5x --disable-test --disable-gtk --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README src/LICENSE
%{_bindir}/edb_*

%files -n %libname
%{_libdir}/lib*.so.%{major}*

%files -n %libnamedev
%{_libdir}/pkgconfig/*
%_libdir/libedb.so
%{_includedir}/Edb.h


%changelog
* Tue Jun 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.5.050-4
+ Revision: 807037
- rel up for new e17

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.5.050-3mdv2011.0
+ Revision: 618028
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5.050-2mdv2010.0
+ Revision: 437355
- rebuild

* Mon Mar 02 2009 Antoine Ginies <aginies@mandriva.com> 1.0.5.050-1mdv2009.1
+ Revision: 347433
- SVN SNAPSHOT 20090227, release 1.0.5.050

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5.042-4mdv2009.0
+ Revision: 266610
- rebuild early 2009.0 package (before pixel changes)

  + Antoine Ginies <aginies@mandriva.com>
    - CVS SNAPSHOT 20080805, release 1.0.5.042

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 1.0.5.042-2mdv2009.0
+ Revision: 213969
- spec cleanup

* Fri Feb 15 2008 Antoine Ginies <aginies@mandriva.com> 1.0.5.042-2mdv2008.1
+ Revision: 168737
- bump release to build E's libs in right order

* Fri Feb 01 2008 Austin Acton <austin@mandriva.org> 1.0.5.042-1mdv2008.1
+ Revision: 161249
- new version
- fix URL
- drop edb-config

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 10 2007 Austin Acton <austin@mandriva.org> 1.0.5.008-3mdv2008.1
+ Revision: 107474
- remove cumbersome gtk+1.2 frontend and tcl tests

* Wed Oct 31 2007 Antoine Ginies <aginies@mandriva.com> 1.0.5.008-2mdv2008.1
+ Revision: 104065
- CVS SNAPSHOT 20071031, release 1.0.5.008

* Thu Aug 30 2007 Antoine Ginies <aginies@mandriva.com> 1.0.5.008-1mdv2008.0
+ Revision: 76290
- fix missing edb-config
- remive edb-config multi-arch from spec
- fix path in tarball
- CVS SNAPSHOT 20070830, release 1.0.5.008

* Thu May 31 2007 Antoine Ginies <aginies@mandriva.com> 1.0.5.007-5mdv2008.0
+ Revision: 33074
- fix bad provides

* Wed May 30 2007 Antoine Ginies <aginies@mandriva.com> 1.0.5.007-4mdv2008.0
+ Revision: 32762
- add some provides

* Tue May 29 2007 Antoine Ginies <aginies@mandriva.com> 1.0.5.007-3mdv2008.0
+ Revision: 32620
- CVS SNAPSHOT 20070529, release 1.0.5.007

* Thu May 24 2007 Antoine Ginies <aginies@mandriva.com> 1.0.5.007-2mdv2008.0
+ Revision: 30803
- increase release
- CVS snapshot 20070524

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 1.0.5.007-1mdv2008.0
+ Revision: 17124
- New snapshot
- Import edb

