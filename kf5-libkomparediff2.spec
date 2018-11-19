%define		_state		stable
%define		orgname		libkomparediff2
%define		qtver		5.5.1

Summary:	libkomparediff2
Name:		kf5-%{orgname}
Version:	18.08.3
Release:	0.1
License:	LGPL
Group:		X11/Libraries
Source0:	http://download.kde.org/%{_state}/applications/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	80f64137fc73ffdfadcac9e356319645
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libkomparediff2

%package devel
Summary:	Development files for libkomparediff2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kde4-kdegame-devel
Conflicts:	kde4-libkomparediff2-devel

%description devel
Development files for libkomparediff2.

%description devel -l pl.UTF-8
Pliki dla programistów libkomparediff2

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkomparediff2.so.?
%attr(755,root,root) %{_libdir}/libkomparediff2.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkomparediff2.so
%{_libdir}/cmake/LibKompareDiff2
%{_includedir}/libkomparediff2
