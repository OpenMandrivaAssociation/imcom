Name:		imcom
Version:	1.34
Release:	%mkrel 1
Group:		Networking/Instant messaging
License:	BSD
Summary:	Console-based jabber client
#URL:		http://imcom.floobin.cx/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	python-devel
Source:		http://nafai.dyndns.org/files/%{name}-%{version}.tar.bz2
Patch:		imcom-1.33-destdir.patch
Buildarch:	noarch

%description
What is IMCom
IMCom is console Jabber Client written in Python. It in many ways
resembles micq because that is the ICQ client that I used before
switching to jabber (micq).

%prep
%setup -q
%patch -p1 -b .destdir

%build
%configure
%make

%install
rm -Rf %{buildroot}

%makeinstall_std

rm -Rf %{buildroot}/%{_datadir}/%{name}/docs/

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
%doc README WHATSNEW docs/*.html docs/*.css docs/*.png docs/*.jpg

