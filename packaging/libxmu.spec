
Name:       libxmu
Summary:    X.Org X11 libXmu/libXmuu runtime libraries
Version:    1.1.0
Release:    2.6
Group:      Graphics/X Window System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Source1001: packaging/libxmu.manifest 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xextproto)


%description
This library contains miscellaneous utilities and is not part of the Xlib
standard.  It contains routines which only use public interfaces so that it
may be layered on top of any proprietary implementation of Xlib or Xt.



%package devel
Summary:    X.Org X11 libXmu development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-filesystem

%description devel
This library contains miscellaneous utilities and is not part of the Xlib
standard.



%prep
%setup -q


%build
cp %{SOURCE1001} .

%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%manifest libxmu.manifest
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXmu.so.6
%{_libdir}/libXmu.so.6.2.0
%{_libdir}/libXmuu.so.1
%{_libdir}/libXmuu.so.1.0.0


%files devel
%manifest libxmu.manifest
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/Xmu
%doc README ChangeLog
%doc %{_docdir}/libXmu/Xmu.xml
%doc %{_docdir}/libXmu/xlogo.svg
%{_includedir}/X11/Xmu/*.h
%{_libdir}/libXmu.so
%{_libdir}/libXmuu.so
%{_libdir}/pkgconfig/xmu.pc
%{_libdir}/pkgconfig/xmuu.pc
