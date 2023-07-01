# maybe TODO:
# plugins/position/simulator (BR: Qt5Simulator)
#
# Conditional build:
%bcond_with	bootstrap	# disable features to able to build without installed qt5
# -- build targets
%bcond_without	doc		# Documentation
%bcond_without	qm		# QM translations
%bcond_without	gypsy		# gypsy plugin

%if %{with bootstrap}
%undefine	with_doc
%undefine	with_qm
%endif

%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qtserialport_ver	%{version}
%define		qttools_ver		5.9
%define		orgname		qtlocation
Summary:	The Qt5 Location library
Summary(pl.UTF-8):	Biblioteka Qt5 Location
Name:		qt5-%{orgname}
Version:	5.15.10
Release:	2
License:	LGPL v3 or GPL v2+ or commercial
Group:		Libraries
Source0:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	6d7c0a23fe701597815a54cac53c1e62
Source1:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/qttranslations-everywhere-opensource-src-%{version}.tar.xz
# Source1-md5:	f421a46bfd3cbbdf0a3fa701d3ccbedf
Patch0:		gcc13.patch
URL:		https://www.qt.io/
%{?with_gypsy:BuildRequires:	GConf2-devel >= 2.0}
BuildRequires:	Qt5Concurrent-devel >= %{qtbase_ver}
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5DBus-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5SerialPort-devel >= %{qtserialport_ver}
BuildRequires:	Qt5Sql-devel >= %{qtdeclarative_ver}
%{?with_gypsy:BuildRequires:	gypsy-devel}
BuildRequires:	pkgconfig
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
%{?with_qm:BuildRequires:	qt5-linguist >= %{qttools_ver}}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Location and Positioning libraries.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera biblioteki Qt5 Location i Positioning.

%package -n Qt5Location
Summary:	The Qt5 Location library
Summary(pl.UTF-8):	Biblioteka Qt5 Location
Group:		Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Positioning = %{version}-%{release}
Requires:	Qt5Quick >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtlocation < 5.3.0

%description -n Qt5Location
Qt5 Location library provides mapping, navigation and place search via
QML and C++ interfaces.

%description -n Qt5Location -l pl.UTF-8
Biblioteka Qt5 Location udostępnia mapy, nawigowanie oraz wyszukiwanie
miejsc poprzez interfejsy QML i C++.

%package -n Qt5Location-devel
Summary:	Qt5 Location library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Location - pliki programistyczne
Group:		Development/Libraries
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Location = %{version}-%{release}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Positioning-devel = %{version}-%{release}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}
Requires:	Qt5Quick-devel >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtlocation-devel < 5.3.0

%description -n Qt5Location-devel
Qt5 Location library - development files.

%description -n Qt5Location-devel -l pl.UTF-8
Biblioteka Qt5 Location - pliki programistyczne.

%package -n Qt5Positioning
Summary:	The Qt5 Positioning library
Summary(pl.UTF-8):	Biblioteka Qt5 Positioning
Group:		Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}
# for plugins
Requires:	Qt5DBus >= %{qtbase_ver}
Requires:	Qt5SerialPort >= %{qtserialport_ver}
Obsoletes:	qt5-qtlocation < 5.3.0

%description -n Qt5Positioning
Qt5 Positioning library provides positioning information via QML and
C++ interfaces.

%description -n Qt5Positioning -l pl.UTF-8
Biblioteka Qt5 Positioning udostępnia informacje o położeniu poprzez
interfejsy QML i C++.

%package -n Qt5Positioning-devel
Summary:	Qt5 Positioning library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Positioning - pliki programistyczne
Group:		Development/Libraries
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Positioning = %{version}-%{release}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}
Requires:	Qt5Quick-devel >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtlocation-devel < 5.3.0

%description -n Qt5Positioning-devel
Qt5 Positioning library - development files.

%description -n Qt5Positioning-devel -l pl.UTF-8
Biblioteka Qt5 Positioning - pliki programistyczne.

%package doc
Summary:	Qt5 Location and Positioning documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Location i Positioning w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 Location and Positioning documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Location i Positioning w formacie HTML.

%package doc-qch
Summary:	Qt5 Location and Positioning documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Location i Positioning w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 Location and Positioning documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Location i Positioning w formacie QCH.

%package examples
Summary:	Qt5 Location and Positioning examples
Summary(pl.UTF-8):	Przykłady do bibliotek Qt5 Location i Positioning
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Qt5 Location and Positioning examples.

%description examples -l pl.UTF-8
Przykłady do bibliotek Qt5 Location i Positioning.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version} %{?with_qm:-a1}
%patch0 -p1

%build
%{qmake_qt5} -- \
	%{!?with_gypsy:-no}-feature-gypsy
%{__make}
%{?with_doc:%{__make} docs}

%if %{with qm}
cd qttranslations-everywhere-src-%{version}
%{qmake_qt5}
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

%if %{with qm}
%{__make} -C qttranslations-everywhere-src-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# keep only qtlocation
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/{assistant,designer,linguist,qt,qtbase,qtconnectivity,qtdeclarative,qtmultimedia,qtquickcontrols,qtquickcontrols2,qtserialport,qtscript,qtwebengine,qtwebsockets,qtxmlpatterns}_*.qm
%endif

# kill unnecessary -L%{_libdir} from *.la, *.prl, *.pc
%{__sed} -i -e "s,-L%{_libdir} \?,,g" \
	$RPM_BUILD_ROOT%{_libdir}/*.{la,prl} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# Prepare some files list
ifecho() {
	r="$RPM_BUILD_ROOT$2"
	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}
ifecho_tree() {
	ifecho $1 $2
	for f in `find $RPM_BUILD_ROOT$2 -printf "%%P "`; do
		ifecho $1 $2/$f
	done
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/location
ifecho_tree examples %{_examplesdir}/qt5/positioning

# find_lang --with-qm supports only PLD qt3/qt4 specific %{_datadir}/locale/*/LC_MESSAGES layout
find_qt5_qm()
{
	name="$1"
	find $RPM_BUILD_ROOT%{_datadir}/qt5/translations -name "${name}_*.qm" | \
		sed -e "s:^$RPM_BUILD_ROOT::" \
		    -e 's:\(.*/'$name'_\)\([a-z][a-z][a-z]\?\)\(_[A-Z][A-Z]\)\?\(\.qm\)$:%lang(\2\3) \1\2\3\4:'
}

echo '%defattr(644,root,root,755)' > qtlocation.lang
%if %{with qm}
find_qt5_qm qtlocation >> qtlocation.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Location -p /sbin/ldconfig
%postun	-n Qt5Location -p /sbin/ldconfig

%post	-n Qt5Positioning -p /sbin/ldconfig
%postun	-n Qt5Positioning -p /sbin/ldconfig

%files -n Qt5Location -f qtlocation.lang
%defattr(644,root,root,755)
# R: Core Gui Qml QmlModels Positioning PositioningQuick Quick
%attr(755,root,root) %{_libdir}/libQt5Location.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Location.so.5
%dir %{qt5dir}/plugins/geoservices
# R: Core Location Network Positioning
%attr(755,root,root) %{qt5dir}/plugins/geoservices/libqtgeoservices_esri.so
# R: Core Location Positioning Quick
%attr(755,root,root) %{qt5dir}/plugins/geoservices/libqtgeoservices_itemsoverlay.so
# R: Core Location Network Positioning
%attr(755,root,root) %{qt5dir}/plugins/geoservices/libqtgeoservices_mapbox.so
# R: Core Gui Location Network Positioning Qml Quick Sql
%attr(755,root,root) %{qt5dir}/plugins/geoservices/libqtgeoservices_mapboxgl.so
# R: Core Gui Location Network Positioning
%attr(755,root,root) %{qt5dir}/plugins/geoservices/libqtgeoservices_nokia.so
# R: Core Gui Location Network Positioning
%attr(755,root,root) %{qt5dir}/plugins/geoservices/libqtgeoservices_osm.so
%dir %{qt5dir}/qml/QtLocation
# R: Core Location Positioning Qml Quick
%attr(755,root,root) %{qt5dir}/qml/QtLocation/libdeclarative_location.so
%{qt5dir}/qml/QtLocation/plugins.qmltypes
%{qt5dir}/qml/QtLocation/qmldir
%dir  %{_libdir}/qt5/qml/Qt/labs/location
# R: Core Location Positioning Qml
%attr(755,root,root) %{_libdir}/qt5/qml/Qt/labs/location/liblocationlabsplugin.so
%{_libdir}/qt5/qml/Qt/labs/location/plugins.qmltypes
%{_libdir}/qt5/qml/Qt/labs/location/qmldir

%files -n Qt5Location-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Location.so
%{_libdir}/libQt5Location.prl
%{_includedir}/qt5/QtLocation
%{_pkgconfigdir}/Qt5Location.pc
%{_libdir}/cmake/Qt5Location
%{qt5dir}/mkspecs/modules/qt_lib_location.pri
%{qt5dir}/mkspecs/modules/qt_lib_location_private.pri

%files -n Qt5Positioning
%defattr(644,root,root,755)
# R: Core
%attr(755,root,root) %{_libdir}/libQt5Positioning.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Positioning.so.5
# R: Core Network Qml Quick
%attr(755,root,root) %{_libdir}/libQt5PositioningQuick.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5PositioningQuick.so.5
%dir %{qt5dir}/plugins/position
# R: Core DBus Positioning
%attr(755,root,root) %{qt5dir}/plugins/position/libqtposition_geoclue.so
# R: Core DBus Positioning
%attr(755,root,root) %{qt5dir}/plugins/position/libqtposition_geoclue2.so
# R: Core Positioning, GConf2, gypsy
%{?with_gypsy:%attr(755,root,root) %{qt5dir}/plugins/position/libqtposition_gypsy.so}
# R: Core Positioning
%attr(755,root,root) %{qt5dir}/plugins/position/libqtposition_positionpoll.so
# R: Core Positioning SerialPort
%attr(755,root,root) %{qt5dir}/plugins/position/libqtposition_serialnmea.so
%dir %{qt5dir}/qml/QtPositioning
# R: Core Positioning PositioningQuick Qml Quick
%attr(755,root,root) %{qt5dir}/qml/QtPositioning/libdeclarative_positioning.so
%{qt5dir}/qml/QtPositioning/plugins.qmltypes
%{qt5dir}/qml/QtPositioning/qmldir

%files -n Qt5Positioning-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Positioning.so
%attr(755,root,root) %{_libdir}/libQt5PositioningQuick.so
%{_libdir}/libQt5Positioning.prl
%{_libdir}/libQt5PositioningQuick.prl
%{_includedir}/qt5/QtPositioning
%{_includedir}/qt5/QtPositioningQuick
%{_pkgconfigdir}/Qt5Positioning.pc
%{_pkgconfigdir}/Qt5PositioningQuick.pc
%{_libdir}/cmake/Qt5Positioning
%{_libdir}/cmake/Qt5PositioningQuick
%{qt5dir}/mkspecs/modules/qt_lib_positioning.pri
%{qt5dir}/mkspecs/modules/qt_lib_positioning_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_positioningquick.pri
%{qt5dir}/mkspecs/modules/qt_lib_positioningquick_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtlocation
%{_docdir}/qt5-doc/qtpositioning

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtlocation.qch
%{_docdir}/qt5-doc/qtpositioning.qch
%endif

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
