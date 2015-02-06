Name:		imcom
Version:	1.34
Release:	7
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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.34-6mdv2011.0
+ Revision: 619622
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.34-5mdv2010.0
+ Revision: 429504
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.34-4mdv2009.0
+ Revision: 240837
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.34-2mdv2008.0
+ Revision: 70272
- use %%mkrel


* Tue Sep 06 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.34-1mdk
- New release 1.34

* Tue Sep 06 2005 Buchan Milne <bgmilne@mandriva.org> 1.34-1mdk
- 1.34
- url gone awol, new source url

* Wed Jul 21 2004 Buchan Milne <bgmilne@linux-mandrake.com> 1.33-1mdk
- first Mandrake package

