Summary:	Several X utilities mainly for use with multimedia files
Summary(de):	Ein CD-Player und Audio-Mixer für X11
Summary(es):	Un CD player y mezclador de audio para X11
Summary(fr):	Un lecteur CD audio et un mixer pour X11
Summary(pl):	Ró¿ne narzêdzia pod X g³ównie do obs³ugi plików multimedialnych
Summary(pt_BR):	Um CD player e mixador de áudio para X11
Summary(tr):	X11 için CD çalýcý ve ses mikseri
Name:		multimedia
Version:	2.1
Release:	25
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/suites/%{name}-%{version}.tar.gz
Source1:	xplaycd.desktop
Source2:	xmixer.desktop
Source3:	xplaycd.png
Source4:	xmixer.png
Patch0:		%{name}-misc.patch
Patch1:		%{name}-scsi.patch
Patch2:		%{name}-res.patch
Patch3:		%{name}-64bit.patch
Patch4:		%{name}-ustat.patch
Patch5:		%{name}-DESTDIR.patch
Patch6:		%{name}-umask.patch
BuildRequires:	XFree86-devel
URL:		http://metalab.unc.edu/pub/Linux/apps/sound/suites/!INDEX.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The multimedia package contains several X Window System utilities for
handling multimedia files: xplaycd, xmixer and xgetfile. Xplaycd is a
CD player for playing audio CDs on your machine's CD-ROM drive. Xmixer
controls the volume settings on your machine's sound card. Xgetfile is
a versatile file browser, intended for use in shell scripts.

%description -l de
Dieses Paket enthält Xplaycd, Xmixer und Xgetfile. Xplaycd ist ein
Programm zum Abspielen von Audio-CDs im CD-ROM-Laufwerk. Xmixer dient
zur Steuerung des Mixers auf einer Soundkarte, und Xgetfile ist ein
Allround-Datei-Browser zur Benutzung in Shell-Skripts.

%description -l es
Este paquete contiene XPlaycd, XMixer y XGetfile. XPlaycd es un
programa para reproducir cds de audio usando el drive de cdrom. XMixer
se usa para controlar las mezclas en la tarjeta de sonido. XGetfile es
un versátil navegador de archivo, hecho para usar en shell scripts.

%description -l fr
Ce paquetage contient XPlaycd, XMixer et XGetfile. XPlaycd est un
programme pour lire des CDs audio en utilisant le lecteur de CD-ROM.
XMixer sert à commander le mixer d'une carte son. XGetfile est un
navigateur de fichier, créé pour être utilisé dans des scripts shell.

%description -l pl
Ten pakiet zawiera kilka narzêdzi dla X Window System do obs³ugi
plików multimedialnych: xplaycd, xmixer i xgetfile. xplaycd jest
odtwarzaczem p³yt CD Audio przy u¿yciu napêdu CD-ROM. xmixer
kontroluje ustawienia g³o¶no¶ci na karcie d¼wiêkowej. xgetfile jest
wszechstronn± przegl±dark± plików, króra ma byæ u¿ywana w skryptach
pow³oki.

%description -l pt_BR
Este pacote contém XPlaycd, XMixer e XGetfile. XPlaycd é um programa
para tocar cds de áudio usando o drive de cdrom. XMixer é usado para
controlar a mixagem na placa de som. XGetfile é um versátil navegador
de arquivo, feito para usar em shell scripts.

%description -l tr
Bu paket XPlaycd, XMixer ve XGetfile programlarýný içerir. XPlaycd,
cdrom sürücü yoluyla ses cdlerini çalan bir programdýr. XMixer, ses
kartý üzerindeki mikserin kontrol edilmesini saðlar. XGetfile ise
kabuk yorumlayýcýlarýnda kullanýlabilecek bir dosya tarayýcýsýdýr.

%prep
%setup -q -n multimedia
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__make} depend
%{__make} \
	CC=%{__cc} \
	OPTIMIZE="%{rpmcflags}" \
	LIBOPTS="-L%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/X11/app-defaults} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT/var/lib/cddb

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	DEFAULTDIR=%{_libdir}/X11/app-defaults

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/xplaycd.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/xmixer.desktop
install %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%attr(1777,root,root) %dir /var/lib/cddb
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*.png
%{_libdir}/X11/app-defaults/*
