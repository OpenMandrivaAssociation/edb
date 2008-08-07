%define	name	edb
%define version 1.0.5.042
%define release %mkrel 4

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
Source: 	http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
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
%configure2_5x --disable-test --disable-gtk
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README src/LICENSE
%{_bindir}/edb_*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%_libdir/libedb.so
%_libdir/libedb.*a
%{_includedir}/Edb.h
