%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		akonadi-import-wizard
Summary:	Akonadi import wizard
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3c198b94a981b5acd25833ec1143769d
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-devel >= 18.12.0
BuildRequires:	ka5-kcontacts-devel >= 18.12.0
BuildRequires:	ka5-kidentitymanagement-devel >= 18.12.0
BuildRequires:	ka5-kmailtransport-devel >= 18.12.0
BuildRequires:	ka5-libkdepim-devel >= 18.12.0
BuildRequires:	ka5-mailcommon-devel >= 18.12.0
BuildRequires:	ka5-mailimporter-devel >= 18.12.0
BuildRequires:	ka5-messagelib-devel >= 18.12.0
BuildRequires:	ka5-pimcommon-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-kauth-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kcrash-devel >= 5.51.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-kwallet-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Assistant to import PIM data from other applications into Akonadi for
use in KDE PIM applications.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/importwizard.categories
/etc/xdg/importwizard.renamecategories
%attr(755,root,root) %{_bindir}/akonadiimportwizard
%attr(755,root,root) %ghost %{_libdir}/libKPimImportWizard.so.5
%attr(755,root,root) %{_libdir}/libKPimImportWizard.so.5.*.*
%dir %{_libdir}/qt5/plugins/importwizard
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/balsaimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/clawsmailimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/evolutionv3importerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/icedoveimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/seamonkeyimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/sylpheedimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/thunderbirdimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/importwizard/trojitaimporterplugin.so
%{_desktopdir}/org.kde.akonadiimportwizard.desktop
%{_iconsdir}/hicolor/128x128/apps/kontact-import-wizard.png
%{_iconsdir}/hicolor/256x256/apps/kontact-import-wizard.png
%{_iconsdir}/hicolor/64x64/apps/kontact-import-wizard.png
%{_datadir}/importwizard
%{_datadir}/kconf_update/importwizard-15.08-kickoff.sh
%{_datadir}/kconf_update/importwizard.upd

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KPim
%{_includedir}/KPim
%{_libdir}/cmake/KPimImportWizard
%{_libdir}/libKPimImportWizard.so
