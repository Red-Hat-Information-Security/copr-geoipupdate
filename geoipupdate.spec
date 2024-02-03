Name:           geoipupdate
Version:        6.1.0
Release:        1%{?dist}
Summary:        GeoIP update client code

License:        MIT
URL:            https://github.com/maxmind/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Patch0:         makefile-buildmode-pie.patch

BuildRequires: git
BuildRequires: make
BuildRequires: pandoc
BuildRequires: golang-bin >= 1.16.0

%undefine _auto_set_build_flags

%global debug_package %{nil}

%description
The GeoIP Update program performs automatic updates of GeoIP2 and GeoLite2 binary databases. CSV databases are not supported.


%prep
%setup -q

%patch0

%build
make


%install
%{__install} -Dm 0755 build/geoipupdate %{buildroot}%{_bindir}/geoipupdate
%{__install} -Dm 0644 build/GeoIP.conf %{buildroot}%{_sysconfdir}/GeoIP.conf

mkdir -p %{buildroot}%{_pkgdocdir}
%{__install} -Dm 0644 build/GeoIP.conf.md build/geoipupdate.md \
  %{buildroot}%{_pkgdocdir}

gzip build/geoipupdate.1
gzip build/GeoIP.conf.5
%{__install} -Dm 0644 build/geoipupdate.1.gz %{buildroot}%{_mandir}/man1/geoipupdate.1.gz
%{__install} -Dm 0644 build/GeoIP.conf.5.gz %{buildroot}%{_mandir}/man5/GeoIP.conf.5.gz
mkdir -p %{buildroot}/usr/share/GeoIP

%files
%license LICENSE-MIT
%dir /usr/share/GeoIP
%{_bindir}/geoipupdate
%{_sysconfdir}/GeoIP.conf
%{_pkgdocdir}
%{_mandir}/man?/*


%changelog
* Sat Feb 3 2024 Lukas Hajn <lhajn@redhat.com> - 6.1.0-1
- bump version to v6.1.0

* Mon Nov 20 2023 Lukas Hajn <lhajn@redhat.com> - 6.0.0-1
- upgrade to v6.0.0

* Mon Oct 10 2022 Lukas Hajn <lhajn@redhat.com> - 4.10.0-2
- create /usr/share/GeoIP directory

* Mon Oct 10 2022 Lukas Hajn <lhajn@redhat.com> - 4.10.0-1
- initial release
