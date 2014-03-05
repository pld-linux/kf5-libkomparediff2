%define		_state		stable
%define		orgname		libkomparediff2
%define		qtver		4.8.1

Summary:	libkomparediff2
Name:		kde4-%{orgname}
Version:	4.12.3
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	24c0377caae2571736e3a38cdc2c5ad3
BuildRequires:	OpenAL-devel
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libsndfile-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libkomparediff2

%package devel
Summary:	Development files for libkomparediff2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdegame-devel

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

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkomparediff2.so.?
%attr(755,root,root) %{_libdir}/libkomparediff2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkomparediff2.so
%{_libdir}/cmake/libkomparediff2
%{_includedir}/libkomparediff2
