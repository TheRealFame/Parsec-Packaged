Name:           parsec
Version:        150
Release:        104a%{?dist}
Summary:        Simple, low-latency desktop and game streaming
License:        Proprietary
URL:            https://parsec.app/
Source0:        parsec-linux.deb

%description
Parsec is a low-latency game streaming and remote desktop application.

%prep
%setup -q -c -T
# Extract the deb
ar x %{SOURCE0}
tar -xf data.tar.*

%build
# Nothing to build - binary package

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps
mkdir -p %{buildroot}/usr/share/parsec/skel

install -m 755 usr/bin/parsecd %{buildroot}/usr/bin/parsecd
install -m 644 usr/share/applications/parsecd.desktop %{buildroot}/usr/share/applications/parsecd.desktop
install -m 644 usr/share/icons/hicolor/256x256/apps/parsecd.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/parsecd.png
install -m 644 usr/share/parsec/skel/parsecd-150-104a.so %{buildroot}/usr/share/parsec/skel/parsecd-150-104a.so
install -m 644 usr/share/parsec/skel/appdata.json %{buildroot}/usr/share/parsec/skel/appdata.json

%files
/usr/bin/parsecd
/usr/share/applications/parsecd.desktop
/usr/share/icons/hicolor/256x256/apps/parsecd.png
/usr/share/parsec/skel/parsecd-150-104a.so
/usr/share/parsec/skel/appdata.json

%changelog
* Mon Jul 29 2024 Parsec Team <founders@parsec.tv> - 150-104a
- Initial RPM package from official .deb
