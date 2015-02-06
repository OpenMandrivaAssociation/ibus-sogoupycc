%if %{_use_internal_dependency_generator}
%define __noautoreq '/usr/bin/lua'
%endif

Summary:	Sogou Pinyin Cloud Client on ibus platform
Name:		ibus-sogoupycc
Version:	0.2.5
Release:	11
Group:		System/Internationalization
License:	GPLv2+
Url:		http://code.google.com/p/ibus-sogoupycc/
Source0:	http://ibus-sogoupycc.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		ibus-sogoupycc-0.2.5-default-use-sogoupy-schema.patch
Patch1:		ibus-sogoupycc-0.2.5-fix-dbus-build.patch
Patch2:		ibus-sogoupycc-0.2.5-libnotify0.7.patch
Patch3:		ibus-sogoupycc-0.2.5-no-strip.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(sqlite3)
Requires:	ibus >= 1.2.0
Requires:	lua-socket
Requires(post,preun):	GConf2

%description
ibus-sogoupycc is an unoffical Sogou pinyin cloud client on ibus platform. 
Features:
* double pinyin support: currently only support UCDOS style double pinyin
  scheme (slightly different from MSPY scheme)
* no preedit: always choose the default (1st) result
* non-blocking input: your input is not interrupted when waitting for
  server's responses.

%files
%{_libexecdir}/ibus-engine-sogoupycc
%{_datadir}/ibus-sogoupycc
%{_datadir}/ibus/component/sogoupycc.xml

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p1

%build
export LDFLAGS="-lm -lpthread"
%cmake
%make

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_libexecdir}
mv %{buildroot}%{_datadir}/ibus-sogoupycc/engine/ibus-sogoupycc %{buildroot}%{_libexecdir}/ibus-engine-sogoupycc

sed -i s,"%{_datadir}/ibus-sogoupycc/engine/ibus-sogoupycc","%{_libexecdir}/ibus-engine-sogoupycc",g \
	%{buildroot}%{_datadir}/ibus/component/sogoupycc.xml
