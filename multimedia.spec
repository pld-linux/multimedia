Summary:	Several X utilities mainly for use with multimedia files
Summary(de.UTF-8):	Ein CD-Player und Audio-Mixer für X11
Summary(es.UTF-8):	Un CD player y mezclador de audio para X11
Summary(fr.UTF-8):	Un lecteur CD audio et un mixer pour X11
Summary(pl.UTF-8):	Różne narzędzia pod X głównie do obsługi plików multimedialnych
Summary(pt_BR.UTF-8):	Um CD player e mixador de áudio para X11
Summary(tr.UTF-8):	X11 için CD çalıcı ve ses mikseri
Name:		multimedia
Version:	2.1
Release:	26
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/suites/%{name}-%{version}.tar.gz
# Source0-md5:	db7f5b0aafaf92425ed18a3f99af9150
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
Patch7:		%{name}-gcc34.patch
BuildRequires:	XFree86-devel
URL:		http://metalab.unc.edu/pub/Linux/apps/sound/suites/!INDEX.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
The multimedia package contains several X Window System utilities for
handling multimedia files: xplaycd, xmixer and xgetfile. Xplaycd is a
CD player for playing audio CDs on your machine's CD-ROM drive. Xmixer
controls the volume settings on your machine's sound card. Xgetfile is
a versatile file browser, intended for use in shell scripts.

%description -l de.UTF-8
Dieses Paket enthält Xplaycd, Xmixer und Xgetfile. Xplaycd ist ein
Programm zum Abspielen von Audio-CDs im CD-ROM-Laufwerk. Xmixer dient
zur Steuerung des Mixers auf einer Soundkarte, und Xgetfile ist ein
Allround-Datei-Browser zur Benutzung in Shell-Skripts.

%description -l es.UTF-8
Este paquete contiene XPlaycd, XMixer y XGetfile. XPlaycd es un
programa para reproducir cds de audio usando el drive de cdrom. XMixer
se usa para controlar las mezclas en la tarjeta de sonido. XGetfile es
un versátil navegador de archivo, hecho para usar en shell scripts.

%description -l fr.UTF-8
Ce paquetage contient XPlaycd, XMixer et XGetfile. XPlaycd est un
programme pour lire des CDs audio en utilisant le lecteur de CD-ROM.
XMixer sert à commander le mixer d'une carte son. XGetfile est un
navigateur de fichier, créé pour être utilisé dans des scripts shell.

%description -l pl.UTF-8
Ten pakiet zawiera kilka narzędzi dla X Window System do obsługi
plików multimedialnych: xplaycd, xmixer i xgetfile. xplaycd jest
odtwarzaczem płyt CD Audio przy użyciu napędu CD-ROM. xmixer
kontroluje ustawienia głośności na karcie dźwiękowej. xgetfile jest
wszechstronną przeglądarką plików, która ma być używana w skryptach
powłoki.

%description -l pt_BR.UTF-8
Este pacote contém XPlaycd, XMixer e XGetfile. XPlaycd é um programa
para tocar cds de áudio usando o drive de cdrom. XMixer é usado para
controlar a mixagem na placa de som. XGetfile é um versátil navegador
de arquivo, feito para usar em shell scripts.

%description -l tr.UTF-8
Bu paket XPlaycd, XMixer ve XGetfile programlarını içerir. XPlaycd,
cdrom sürücü yoluyla ses cdlerini çalan bir programdır. XMixer, ses
kartı üzerindeki mikserin kontrol edilmesini sağlar. XGetfile ise
kabuk yorumlayıcılarında kullanılabilecek bir dosya tarayıcısıdır.

%prep
%setup -q -n multimedia
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1

%build
%{__make} depend
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}/man1 \
	DEFAULTDIR=%{_appdefsdir}

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},/var/lib/cddb}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%attr(1777,root,root) %dir /var/lib/cddb
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_appdefsdir}/*
