%if %{_use_internal_dependency_generator}
%define __noautoreq '/usr/bin/lua'
%else
%define _requires_exceptions /usr/bin/lua
%endif

%define debug_package %{nil}

Name:      ibus-sogoupycc
Summary:   Sogou Pinyin Cloud Client on ibus platform
Version:   0.2.5
Release:   9
Group:     System/Internationalization
License:   GPLv2
URL:       http://code.google.com/p/ibus-sogoupycc/
Source0:   http://ibus-sogoupycc.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:    ibus-sogoupycc-0.2.5-default-use-sogoupy-schema.patch
Patch1:    ibus-sogoupycc-0.2.5-fix-dbus-build.patch
Patch2:    ibus-sogoupycc-0.2.5-libnotify0.7.patch
BuildRequires:	ibus-devel >= 1.3.9-5
BuildRequires:	lua-devel >= 5.1
BuildRequires:	glib2-devel >= 2.22
BuildRequires:	dbus-devel >= 1.2
BuildRequires:	gtk+2-devel
BuildRequires:	sqlite3-devel
BuildRequires:	libnotify-devel >= 0.4
BuildRequires:  cmake
Requires:	ibus >= 1.2.0
Requires:	lua-socket
Requires(post,preun): GConf2

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
export LDFLAGS="-lm -lpthread"
%cmake
%make

%install
%makeinstall_std -C build

%post
%post_ibus_register_engine sgpycc zh_CN

%preun
%preun_ibus_unregister_engine sgpycc

%files
%defattr(-,root,root)
%{_datadir}/ibus-sogoupycc
%{_datadir}/ibus/component/sogoupycc.xml


%changelog
* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 0.2.5-7mdv2011.0
+ Revision: 669830
- rebuild

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 0.2.5-6
+ Revision: 659304
- rebuild for new ibus

* Tue Apr 12 2011 Funda Wang <fwang@mandriva.org> 0.2.5-5
+ Revision: 652781
- build with libnotify 0.7

* Sun Aug 08 2010 Funda Wang <fwang@mandriva.org> 0.2.5-4mdv2011.0
+ Revision: 567672
- default to use sogoupy as double pinyin schema
- fix build with latest dbus

* Mon Apr 26 2010 Funda Wang <fwang@mandriva.org> 0.2.5-3mdv2010.1
+ Revision: 538877
- rebuild for ibus 1.3

* Sun Apr 25 2010 Funda Wang <fwang@mandriva.org> 0.2.5-2mdv2010.1
+ Revision: 538603
- drop hard requries on lua executable

* Fri Apr 16 2010 Funda Wang <fwang@mandriva.org> 0.2.5-1mdv2010.1
+ Revision: 535308
- update to new version 0.2.5

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 0.2.4.20100401-2mdv2010.1
+ Revision: 533621
- New version 0.2.4.20100401

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 0.2.0.20100318-2mdv2010.1
+ Revision: 528586
- requires lua-socket

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 0.2.0.20100318-1mdv2010.1
+ Revision: 528561
- New version 0.2.0.20100318

* Mon Feb 15 2010 Funda Wang <fwang@mandriva.org> 0.0.1-0.svn21.2mdv2010.1
+ Revision: 506054
- New snapshot

* Thu Nov 12 2009 Funda Wang <fwang@mandriva.org> 0.0.1-0.svn18.2mdv2010.1
+ Revision: 465143
- fix else
- use shared_prefix
- use libexec

* Sat Nov 07 2009 Funda Wang <fwang@mandriva.org> 0.0.1-0.svn18.1mdv2010.1
+ Revision: 462399
- BR cmake
- import ibus-sogoupycc

