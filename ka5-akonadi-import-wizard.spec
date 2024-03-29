#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		akonadi-import-wizard
Summary:	Akonadi import wizard
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9434ce6a46713ad5ac0d3b1ec7af1c2a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 3.20
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
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
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
%{_desktopdir}/org.kde.akonadiimportwizard.desktop
%{_iconsdir}/hicolor/128x128/apps/kontact-import-wizard.png
%{_iconsdir}/hicolor/256x256/apps/kontact-import-wizard.png
%{_iconsdir}/hicolor/64x64/apps/kontact-import-wizard.png
%{_datadir}/importwizard
%{_datadir}/qlogging-categories5/importwizard.categories
%{_datadir}/qlogging-categories5/importwizard.renamecategories
%dir %{_libdir}/qt5/plugins/pim5/importwizard
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/importwizard/balsaimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/importwizard/clawsmailimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/importwizard/evolutionv3importerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/importwizard/icedoveimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/importwizard/seamonkeyimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/importwizard/sylpheedimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/importwizard/thunderbirdimporterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/importwizard/trojitaimporterplugin.so
%ghost %{_libdir}/libKPim5ImportWizard.so.5
%attr(755,root,root) %{_libdir}/libKPim5ImportWizard.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim5/ImportWizard
%{_libdir}/cmake/KPim5ImportWizard
%{_libdir}/cmake/KPimImportWizard
%{_libdir}/libKPim5ImportWizard.so
