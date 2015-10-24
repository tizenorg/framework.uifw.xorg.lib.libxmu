# TODO: libXmuu split and/or elf filter emulation

Summary: X.Org X11 libXmu/libXmuu runtime libraries
Name: libXmu
Version: 1.1.2
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires: xorg-x11-xutils-dev
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXt-devel

%description
X.Org X11 libXmu/libXmuu runtime libraries

%package devel
Summary: X.Org X11 libXmu development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libxmu-devel

%description devel
X.Org X11 libXmu development package

%prep
%setup -q

%build
%reconfigure --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# fixup later
rm -rf $RPM_BUILD_ROOT%{_docdir}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
%doc COPYING README
%{_libdir}/libXmu.so.6
%{_libdir}/libXmu.so.6.2.0
%{_libdir}/libXmuu.so.1
%{_libdir}/libXmuu.so.1.0.0

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xmu
%{_includedir}/X11/Xmu/Atoms.h
%{_includedir}/X11/Xmu/CharSet.h
%{_includedir}/X11/Xmu/CloseHook.h
%{_includedir}/X11/Xmu/Converters.h
%{_includedir}/X11/Xmu/CurUtil.h
%{_includedir}/X11/Xmu/CvtCache.h
%{_includedir}/X11/Xmu/DisplayQue.h
%{_includedir}/X11/Xmu/Drawing.h
%{_includedir}/X11/Xmu/Editres.h
%{_includedir}/X11/Xmu/EditresP.h
%{_includedir}/X11/Xmu/Error.h
%{_includedir}/X11/Xmu/ExtAgent.h
%{_includedir}/X11/Xmu/Initer.h
%{_includedir}/X11/Xmu/Lookup.h
%{_includedir}/X11/Xmu/Misc.h
%{_includedir}/X11/Xmu/StdCmap.h
%{_includedir}/X11/Xmu/StdSel.h
%{_includedir}/X11/Xmu/SysUtil.h
%{_includedir}/X11/Xmu/WhitePoint.h
%{_includedir}/X11/Xmu/WidgetNode.h
%{_includedir}/X11/Xmu/WinUtil.h
%{_includedir}/X11/Xmu/Xct.h
%{_includedir}/X11/Xmu/Xmu.h
%{_libdir}/libXmu.so
%{_libdir}/libXmuu.so
%{_libdir}/pkgconfig/xmu.pc
%{_libdir}/pkgconfig/xmuu.pc