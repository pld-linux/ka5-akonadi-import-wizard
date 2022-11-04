#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		akonadi-import-wizard
Summary:	Akonadi import wizard
Name:		ka5-%{kaname}
Version:	22.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5a3046c89f89f25b27e5a61359d45166
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-mailcommon-devel >= %{kdeappsver}
BuildRequires:	ka5-mailimporter-devel >= %{kdeappsver}
BuildRequires:	ka5-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kauth-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcontacts-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
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
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadiimportwizard
%ghost %{_libdir}/libKPimImportWizard.so.5
%attr(755,root,root) %{_libdir}/libKPimImportWizard.so.*.*.*
%{_desktopdir}/org.kde.akonadiimportwizard.desktop
%{_iconsdir}/hicolor/128x128/apps/kontact-import-wizard.png
%{_iconsdir}/hicolor/256x256/apps/kontact-import-wizard.png
%{_iconsdir}/hicolor/64x64/apps/kontact-import-wizard.png
%{_datadir}/importwizard
%{_datadir}/qlogging-categories5/importwizard.categories
%{_datadir}/qlogging-categories5/importwizard.renamecategories
%dir %{_libdir}/qt5/plugins/pim5/importwizard
%{_libdir}/qt5/plugins/pim5/importwizard/balsaimporterplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/clawsmailimporterplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/evolutionv3importerplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/icedoveimporterplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/seamonkeyimporterplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/sylpheedimporterplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/thunderbirdimporterplugin.so
%{_libdir}/qt5/plugins/pim5/importwizard/trojitaimporterplugin.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KPim
%{_includedir}/KPim
%{_libdir}/cmake/KPimImportWizard
%{_libdir}/libKPimImportWizard.so
