# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       meegotouch-applauncherd
Summary:    Application launcher for fast startup
Version:    0.29.1
Release:    1
Group:      System/Daemons
License:    LGPLv2+
URL:        http://meego.gitorious.com/meegotouch/meegotouch-applauncherd
Source0:    %{name}-%{version}.tar.bz2
Source100:  meegotouch-applauncherd.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(meegotouch)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xext)
BuildRequires:  cmake

%description
Application invoker and launcher daemon that speed up
application startup time and share memory. Provides also
functionality to launch applications as single instances.

%package devel
Summary:    Development files for launchable applications
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for creating applications that can be launched 
using meegotouch-applauncherd.

%package doc
Summary:    Instructions for application developer
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation files for application developer. 

%package testapps
Summary:    Test applications for launchable applications
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}
BuildRequires:   desktop-file-utils

%description testapps
Test applications used for testing meegotouch-applauncherd.

%package tests
Summary:    Test scripts for launchable applications
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-testapps = %{version}-%{release}

%description tests
Test scripts used for testing meegotouch-applauncherd.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
export BUILD_TESTS=1
export MEEGO=1
unset LD_AS_NEEDED
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# rpmlint complains about installing binaries in /usr/share, so
# move them elsewhere and leave a symlink in place.
mv %{buildroot}/usr/share/applauncherd-tests %{buildroot}/usr/lib
(cd %{buildroot}/usr/share; ln -s ../lib/applauncherd-tests)

# applauncherd expects the theme daemon socket in /var/tmp in Harmattan,
# but it is in /tmp in MeeGo. Drop in a symbolic link as an interim solution.
(cd %{buildroot}/var/tmp; ln -s ../../tmp/m.mthemedaemon)
# << install post

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/invoker
%{_bindir}/applauncherd.bin
%{_libdir}/applauncherd/libapplauncherd.so
%{_bindir}/applauncherd
%{_libdir}/applauncherd/libebooster.so
%{_libdir}/applauncherd/libmbooster.so
%{_libdir}/applauncherd/libqtbooster.so
%{_libdir}/applauncherd/libqdeclarativebooster.so
%{_libdir}/libmdeclarativecache.so
%{_libdir}/libmdeclarativecache.so.*
%{_bindir}/single-instance
%config %{_sysconfdir}/xdg/autostart/applauncherd.desktop
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/meegotouch-boostable.pc
%{_libdir}/pkgconfig/qdeclarative-boostable.pc
%{_libdir}/pkgconfig/qt-boostable.pc
%{_includedir}/applauncherd/mdeclarativecache.h
%{_includedir}/applauncherd/MDeclarativeCache
%{_datadir}/qt4/mkspecs/features/meegotouch-boostable.prf
%{_datadir}/qt4/mkspecs/features/qt-boostable.prf
%{_datadir}/qt4/mkspecs/features/qdeclarative-boostable.prf
%{_libdir}/libmdeclarativecache.so
# >> files devel
# << files devel

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/applauncherd/*
# >> files doc
# << files doc

%files testapps
%defattr(-,root,root,-)
%{_bindir}/fala_ft_hello
%{_bindir}/fala_status
%{_bindir}/fala_ft_hello1
%{_bindir}/fala_ft_hello2
%{_bindir}/fala_ft_creds1
%{_bindir}/fala_ft_creds2
%{_bindir}/fala_multi-instance
%{_bindir}/fala_qml_wol
%{_bindir}/fala_qml_wl
%{_bindir}/fala_qml_helloworld
%{_bindir}/fala_qml_helloworld1
%{_bindir}/fala_qml_helloworld2
%{_bindir}/fala_wl
%{_bindir}/fala_wol
%{_bindir}/fala_gettime
%{_bindir}/fala_gettime_ms
%{_bindir}/fala_pixelchanged
%{_bindir}/fala_windowid
%{_bindir}/xsendevent
%{_datadir}/dbus-1/services/com.nokia.fala_testapp.service
%{_datadir}/dbus-1/services/com.nokia.fala_wl.service
%{_datadir}/dbus-1/services/com.nokia.fala_wol.service
%{_bindir}/fala_ft_themetest
%{_datadir}/themes/base/meegotouch/fala_ft_themetest/*
%{_datadir}/applications/fala_wl.desktop
%{_datadir}/applications/fala_wol.desktop
%{_datadir}/fala_qml_helloworld/main.qml
%{_datadir}/applications/fala_qml_wl.desktop
%{_datadir}/applications/fala_qml_wol.desktop
%{_datadir}/fala_images/*
# >> files testapps
# << files testapps

%files tests
%defattr(-,root,root,-)
%{_datadir}/applauncherd-testscripts/test-func-launcher.py
%{_datadir}/applauncherd-testscripts/ts_prestartapp.rb
%{_datadir}/applauncherd-testscripts/check_pipes.py
%{_datadir}/applauncherd-testscripts/test-perf-mbooster.py
%{_datadir}/applauncherd-testscripts/tc_theming.rb
%{_datadir}/applauncherd-testscripts/tc_splash.rb
%{_datadir}/applauncherd-testscripts/test-perf.rb
%{_datadir}/applauncherd-testscripts/get-coordinates.rb
%{_datadir}/applauncherd-testscripts/utils.py
%{_datadir}/applauncherd-testscripts/test-security.py
%{_datadir}/applauncherd-testscripts/test-daemons.py
%{_bindir}/fala_wid
%{_datadir}/applauncherd-testscripts/fala_xres_wl
%{_datadir}/applauncherd-testscripts/fala_xres_wol
%{_datadir}/applauncherd-testscripts/signal-forward/*
%{_datadir}/applauncherd-testscripts/test-single-instance.py
%{_datadir}/applauncherd-testscripts/test-core-dump.py
%{_datadir}/applauncherd-tests/tests.xml
%{_datadir}/applauncherd-tests/ut_booster
%{_datadir}/applauncherd-tests/ut_boosterfactory
%{_datadir}/applauncherd-tests/ut_daemon
%{_datadir}/applauncherd-tests/ut_connection
%{_datadir}/applauncherd-tests/ut_dbooster
%{_datadir}/applauncherd-tests/ut_ebooster
%{_datadir}/applauncherd-tests/ut_mbooster
%{_datadir}/applauncherd-tests/ut_qtbooster
%{_datadir}/applauncherd-tests/ut_socketmanager
%{_datadir}/applauncherd-functional-tests/tests.xml
%{_datadir}/applauncherd-libmeegotouch-perf-tests/tests.xml
%{_datadir}/applauncherd-qml-perf-tests/tests.xml
%{_datadir}/applauncherd-red-tests/tests.xml
%{_datadir}/applauncherd-reference-perf-tests/tests.xml
# >> files tests
# << files tests

