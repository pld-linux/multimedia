Summary: Several X utilities mainly for use with multimedia files.
Name: multimedia
Version: 2.1
Release: 15
Copyright: GPL
Group: Applications/Multimedia
Source: ftp://sunsite.unc.edu/pub/Linux/apps/sound/suites/multimedia-2.1.tar.gz
Source1: xplaycd.wmconfig
Source2: xmixer.wmconfig
Patch: multimedia-2.1-misc.patch
Patch1: multimedia-2.1-scsi.patch
Patch2: multimedia-2.1-res.patch
Patch3: multimedia-2.1-64bit.patch
Patch4: multimedia-2.1-ustat.patch
Buildroot: /var/tmp/multimedia-root

%description
The multimedia package contains several X Window System utilities
for handling multimedia files:  xplaycd, xmixer and xgetfile.
Xplaycd is a CD player for playing audio CDs on your machine's
CD-ROM drive.  Xmixer controls the volume settings on your machine's
sound card.  Xgetfile is a versatile file browser, intended for use
in shell scripts.

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
make depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" LIBOPTS=-L/usr/X11R6/lib

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1,lib/X11/app-defaults} 
make install \
	BINDIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
	MANDIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
	DEFAULTDIR=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults \
	LIBDIR=$RPM_BUILD_ROOT/usr/X11R6/lib \
	MKDIR="mkdir -p"

chmod 644 $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/*
chmod 644 $RPM_BUILD_ROOT/usr/X11R6/man/man1/*
strip $RPM_BUILD_ROOT/usr/X11R6/bin/*
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 0644 $RPM_SOURCE_DIR/xplaycd.wmconfig \
	$RPM_BUILD_ROOT/etc/X11/wmconfig/xplaycd
install -m 0644 $RPM_SOURCE_DIR/xmixer.wmconfig \
	$RPM_BUILD_ROOT/etc/X11/wmconfig/xmixer

mkdir -p $RPM_BUILD_ROOT/var/lib/cddb/
chmod 1777 $RPM_BUILD_ROOT/var/lib/cddb/ 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/X11/wmconfig/*
/usr/X11R6/bin/*
/usr/X11R6/man/man1/*
%dir /var/lib/cddb/ 

%config /usr/X11R6/lib/X11/app-defaults/*
%doc INSTALL
