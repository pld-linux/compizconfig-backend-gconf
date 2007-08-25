Summary:	The gconf backend for CompizConfig
Summary(pl.UTF-8):	Backend gconf dla CompizConfiga
Name:		compizconfig-backend-gconf
Version:	0.5.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	f64426ae486e62b5d475ab4e40d9d0d3
#Patch0:		%{name}-am.patch
URL:		http://forum.compiz-fusion.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	libcompizconfig-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gconf backend for CompizConfig. It uses the GConf configuration
system to store the compiz configuration and provides integration
into the GNOME desktop environment.

%description -l pl.UTF-8
Backend gconf dla CompizConfiga. Używa systemu konfiguracji GConf do
przechowywania konfiguracji compiza i zapewnia intergrację ze
środowiskiem GNOME.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/compizconfig/backends/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/compizconfig/backends/libgconf.so
