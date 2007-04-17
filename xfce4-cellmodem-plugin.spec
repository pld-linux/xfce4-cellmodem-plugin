Summary:	A cellmodem plugin for the Xfce panel
Name:		xfce4-cellmodem-plugin
Version:	0.0.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-cellmodem-plugin/%{name}-%{version}.tar.gz
# Source0-md5:	e438eb703d40c42917027fcbc742d4eb
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cellmodem-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libusb-devel >= 0.1.12
BuildRequires:	pciutils-devel
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	zlib-devel
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cellmodem plugin is a monitoring plugin for cellular modems. It
reports provider and signal quality for GPRS/UMTS(3G)/HSDPA(3.5G)
modem cards. It works with mostly all cards which support an
out-of-band channel for monitoring purposes.

The current features include:
- Display the current network type (GPRS/UMTS)
- Display the current signal level
- Configure the maximum signal level
- Configure the low and critical signal level
- Asking for PIN if modem needs it
- Quick visual feedback on modem and registration status via LEDs

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-cellmodem-plugin
%{_datadir}/xfce4/panel-plugins/cellmodem.desktop
