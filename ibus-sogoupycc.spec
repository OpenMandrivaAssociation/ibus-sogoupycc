%define _requires_exceptions /usr/bin/lua

Name:      ibus-sogoupycc
Summary:   Sogou Pinyin Cloud Client on ibus platform
Version:   0.2.5
Release:   %mkrel 5
Group:     System/Internationalization
License:   GPLv2
URL:       http://code.google.com/p/ibus-sogoupycc/
Source0:   http://ibus-sogoupycc.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:    ibus-sogoupycc-0.2.5-default-use-sogoupy-schema.patch
Patch1:    ibus-sogoupycc-0.2.5-fix-dbus-build.patch
Patch2:    ibus-sogoupycc-0.2.5-libnotify0.7.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ibus-devel >= 1.2.0
BuildRequires:	lua-devel >= 5.1
BuildRequires:	glib2-devel >= 2.22
BuildRequires:	dbus-devel >= 1.2
BuildRequires:	gtk+2-devel
BuildRequires:	sqlite3-devel
BuildRequires:	libnotify-devel >= 0.4
BuildRequires:  cmake
Requires:	ibus >= 1.2.0
Requires:	lua-socket

%description
ibus-sogoupycc is an unoffical Sogou pinyin cloud client on ibus platform. 
Features:
* double pinyin support: currently only support UCDOS style double pinyin
  scheme (slightly different from MSPY scheme) 
* no preedit: always choose the default (1st) result 
* non-blocking input: your input is not interrupted when waitting for
  server's responses.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/ibus-sogoupycc
%{_datadir}/ibus/component/sogoupycc.xml
