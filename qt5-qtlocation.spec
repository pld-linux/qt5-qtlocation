# maybe TODO:
# Qt5Location (BR: Qt3d)
# plugins/position/simulator (BR: Qt5Simulator)
#
# Conditional build:
%bcond_without	qch	# documentation in QCH format
%bcond_without	qm	# QM translations

%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
%define		orgname		qtlocation
Summary:	The Qt5 Location library
Summary(pl.UTF-8):	Biblioteka Qt5 Location
Name:		qt5-%{orgname}
Version:	5.4.1
Release:	1
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3.0
Group:		Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.4/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	f7d693d3f3634da063b61928b502b79d
Source1:	http://download.qt-project.org/official_releases/qt/5.4/%{version}/submodules/qttranslations-opensource-src-%{version}.tar.xz
# Source1-md5:	0bdd1b0a83b03a04a4ebeedfa3057d21
URL:		http://qt-project.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	geoclue-devel
BuildRequires:	gypsy-devel
BuildRequires:	pkgconfig
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
%{?with_qm:BuildRequires:	qt5-linguist >= %{qttools_ver}}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Location (Qt5Positioning) library.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera biblioteki Qt5 Location (Qt5Positioning).

%package -n Qt5Positioning
Summary:	The Qt5 Positioning library
Summary(pl.UTF-8):	Biblioteka Qt5 Positioning
Group:		Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}
Obsoletes:	qt5-qtlocation

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
Requires:	Qt5Positioning = %{version}-%{release}
Obsoletes:	qt5-qtlocation-devel

%description -n Qt5Positioning-devel
Qt5 Positioning library - development files.

%description -n Qt5Positioning-devel -l pl.UTF-8
Biblioteka Qt5 Positioning - pliki programistyczne.

%package doc
Summary:	Qt5 Location (Qt5Positioning) documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 Location (Qt5Positioning) w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Location (Qt5Positioning) documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do biblioteki Qt5 Location (Qt5Positioning) w formacie
HTML.

%package doc-qch
Summary:	Qt5 Location (Qt5Positioning) documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 Location (Qt5Positioning) w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 Location (Qt5Positioning) documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do biblioteki Qt5 Location (Qt5Positioning) w formacie
QCH.

%package examples
Summary:	Qt5 Location (Qt5Positioning) examples
Summary(pl.UTF-8):	Przykłady do biblioteki Qt5 Location (Qt5Positioning)
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Location (Qt5Positioning) examples.

%description examples -l pl.UTF-8
Przykłady do biblioteki Qt5 Location (Qt5Positioning).

%prep
%setup -q -n %{orgname}-opensource-src-%{version} %{?with_qm:-a1}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%if %{with qm}
cd qttranslations-opensource-src-%{version}
qmake-qt5
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with qm}
%{__make} -C qttranslations-opensource-src-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# keep only qtlocation
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/{assistant,designer,linguist,qmlviewer,qt,qtbase,qtconfig,qtconnectivity,qtdeclarative,qtmultimedia,qtquick1,qtscript,qtxmlpatterns}_*.qm
%endif

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
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
ifecho_tree examples %{_examplesdir}/qt5/qtpositioning
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

%post	-n Qt5Positioning -p /sbin/ldconfig
%postun	-n Qt5Positioning -p /sbin/ldconfig

%files -n Qt5Positioning -f qtlocation.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Positioning.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Positioning.so.5
%dir %{qt5dir}/plugins/position
%attr(755,root,root) %{qt5dir}/plugins/position/libqtposition_geoclue.so
%attr(755,root,root) %{qt5dir}/plugins/position/libqtposition_gypsy.so
%attr(755,root,root) %{qt5dir}/plugins/position/libqtposition_positionpoll.so
%dir %{qt5dir}/qml/QtPositioning
%attr(755,root,root) %{qt5dir}/qml/QtPositioning/libdeclarative_positioning.so
%{qt5dir}/qml/QtPositioning/plugins.qmltypes
%{qt5dir}/qml/QtPositioning/qmldir

%files -n Qt5Positioning-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Positioning.so
%{_libdir}/libQt5Positioning.prl
%{_includedir}/qt5/QtPositioning
%{_pkgconfigdir}/Qt5Positioning.pc
%{_libdir}/cmake/Qt5Positioning
%{qt5dir}/mkspecs/modules/qt_lib_positioning.pri
%{qt5dir}/mkspecs/modules/qt_lib_positioning_private.pri

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtpositioning

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtpositioning.qch
%endif

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
