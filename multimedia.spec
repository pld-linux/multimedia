Summary:	Several X utilities mainly for use with multimedia files
Summary(pl):	Ró¿ne narzêdzia pod X g³ównie do obs³ugi plików multimedialnych
Name:		multimedia
Version:	2.1
Release:	15
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/suites/%{name}-%{version}.tar.gz
Source1:	xplaycd.wmconfig
Source2:	xmixer.wmconfig
Patch0:		%{name}-2.1-misc.patch
Patch1:		%{name}-2.1-scsi.patch
Patch2:		%{name}-2.1-res.patch
Patch3:		%{name}-2.1-64bit.patch
Patch4:		%{name}-2.1-ustat.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The multimedia package contains several X Window System utilities for
handling multimedia files: xplaycd, xmixer and xgetfile. Xplaycd is a
CD player for playing audio CDs on your machine's CD-ROM drive. Xmixer
controls the volume settings on your machine's sound card. Xgetfile is
a versatile file browser, intended for use in shell scripts.

Install the multimedia package if you need an audio CD player, a sound
card volume controller, or a file browser for use in shell scripts.

%prep
%setup -q -n multimedia
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} depend
%{__make} RPM_OPT_FLAGS="%{rpmcflags}" LIBOPTS=-L%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/X11/app-defaults} \
	$RPM_BUILD_ROOT/var/lib/cddb/

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \

MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	DEFAULTDIR=$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	MKDIR="install -d"

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xplaycd
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xmixer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/wmconfig/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%attr(1777,root,root) %dir /var/lib/cddb/ 

%{_libdir}/X11/app-defaults/*
