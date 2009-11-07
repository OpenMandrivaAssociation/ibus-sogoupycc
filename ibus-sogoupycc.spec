%define svnrel 18

Name:      ibus-sogoupycc
Summary:   Sogou Pinyin Cloud Client on ibus platform
Version:   0.0.1
Release:   %mkrel -c svn%svnrel 1
Group:     System/Internationalization
License:   GPLv2
URL:       http://code.google.com/p/ibus-sogoupycc/
Source0:   %{name}-r18.tar.bz2
Source1:   CMakeLists.txt
Patch0:    ibus-sogoupycc-path-prefix.path
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ibus-devel >= 1.2.0
BuildRequires:  cmake
Requires:	ibus >= 1.2.0
Requires:	wget js

%description
ibus-sogoupycc is an unoffical Sogou pinyin cloud client on ibus platform. 
Features:
* double pinyin support: currently only support UCDOS style double pinyin
  scheme (slightly different from MSPY scheme) 
* no preedit: always choose the default (1st) result 
* non-blocking input: your input is not interrupted when waitting for
  server's responses.

%prep
%setup -q -n %{name}
%patch0 -p0
cp %{SOURCE1} .

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
%{_libexecdir}/ibus-sogoupycc
%dir %{_datadir}/ibus-sogoupycc
%{_datadir}/ibus-sogoupycc/sgccget.sh
%dir %{_datadir}/ibus-sogoupycc/icons
%{_datadir}/ibus-sogoupycc/icons/ibus-sogoupycc.png
%{_datadir}/ibus/component/sogoupycc.xml
