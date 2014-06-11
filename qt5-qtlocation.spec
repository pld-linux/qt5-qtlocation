# TODO:
# - cleanup
#
# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		qtbase_ver		%{version}
%define		qttools_ver		%{version}
%define		orgname		qtlocation
Summary:	The Qt5 Location library
Summary(pl.UTF-8):	Biblioteka Qt5 Location
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	1c05c198cc3e43da4692f9dfb43b45d6
URL:		http://qt-project.org/
BuildRequires:	geoclue-devel
BuildRequires:	gypsy-devel
BuildRequires:	qt5-qtbase-devel >= %{qtbase_ver}
BuildRequires:	qt5-qttools-devel >= %{qttools_ver}
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
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
Obsoletes:	qt5-qtlocation

%description -n Qt5Positioning
Qt5 Positioning library (TODO: ...).

%description -n Qt5Positioning -l pl.UTF_8
Biblioteka Qt5 Positioning (TODO: ...)

%package -n Qt5Positioning-devel
Summary:	Qt5 Positioning library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Positioning - pliki programistyczne
Group:		Development/Libraries
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
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# Prepare some files list
ifecho() {
	RESULT=`echo $RPM_BUILD_ROOT$2 2>/dev/null`
	[ "$RESULT" == "" ] && return # XXX this is never true due $RPM_BUILD_ROOT being set
	r=`echo $RESULT | awk '{ print $1 }'`

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

echo "%defattr(644,root,root,755)" > examples.files
ifecho examples %{_examplesdir}/qt5
for f in `find $RPM_BUILD_ROOT%{_examplesdir}/qt5 -printf "%%P "`; do
	ifecho examples %{_examplesdir}/qt5/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Positioning -p /sbin/ldconfig
%postun	-n Qt5Positioning -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Positioning.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Positioning.so.5
%attr(755,root,root) %{qt5dir}/plugins/*
%{qt5dir}/qml/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Positioning.so
%{_libdir}/libQt5Positioning.prl
%{_includedir}/qt5/QtPositioning
%{_pkgconfigdir}/Qt5Positioning.pc
%{_libdir}/cmake/Qt5Positioning
%{qt5dir}/mkspecs/modules/*.pri

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtpositioning

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtpositioning.qch
%endif

%files examples -f examples.files
