%define	name	edb
%define version 1.0.5.050
%define release 4

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
