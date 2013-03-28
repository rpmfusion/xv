%define vprog 3.10a
%define vjumbo 20070520

Name: xv
Version: %{vprog}.jumbopatch.%{vjumbo}
Release: 18%{?dist}
Summary: Interactive image display program for X
Summary(de.UTF-8): X-basierender Bild-Viewer für praktische sämtliche Grafiken
Summary(es.UTF-8): Visualizador de imágenes para X para cuasi todos los formatos de imágenes
Summary(fr.UTF-8): Visualisateur sous X pour quasiment tous les types d'images
Summary(pl.UTF-8): Przeglądarka różnego rodzaju plików graficznych pracująca w X Window
Summary(pt_BR.UTF-8): Visualizador de imagens para X para quase todos os formatos de imagens
Summary(ru.UTF-8): Программа для просмотра и преобразования файлов изображений для X
Summary(tr.UTF-8): X tabanlı resim görüntüleyici
Summary(uk.UTF-8): Програма для перегляду та перетворення файлів зображень для X
License: Shareware
Group: Applications/Multimedia
URL: http://www.trilon.com/xv/xv.html
Source0: ftp://ftp.trilon.com/pub/xv/%{name}-%{vprog}.tar.gz
Source1: http://downloads.sourceforge.net/png-mng/%{name}-%{vprog}-jumbo-patches-%{vjumbo}.tar.gz
Source2: DISTRIBUTE.txt
Source3: %{name}.desktop
Source4: %{name}.png
Source5: ftp://ftp.trilon.com/pub/xv/xvman310a-html.tar.gz
Source6: xv-non-english-Xman-pages.tar.bz2
Patch0: xv-jumbo-20070520-makefile.patch
Patch1: http://www.gregroelofs.com/code/xv-3.10a-enhancements.20070520-20081216.diff
Patch2: xv-3.10a-cleanup.patch
Patch3: xv-FLmask.v2.1.patch
Patch4: xv-wait.patch
Patch5: xv-3.10a-libpng15.patch
Patch6: xv-3.10a-namemax.patch
Patch7: xv-3.10a-xvcut.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libtiff-devel libpng-devel jasper-devel desktop-file-utils
%if "%{?rhel}" != "4"
BuildRequires: libX11-devel libXt-devel
%global xlibdir %{_libdir}
%else
BuildRequires: xorg-x11-devel
Requires: man
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%global xlibdir /usr/X11R6/%{_lib}
%endif
Requires: hicolor-icon-theme

%description
This is the famous 'xv' by John Bradley. It is shareware, but we ship
it with the permission of the authors. It is a graphics viewer for
many file types, including gif, jpg, tiff, xwd, etc. It also has
manipulation features such as cropping, expanding, etc. Patched to
include flmask, a popular feature in Japan.

%description -l de.UTF-8
Dies ist das berühmte 'xv' von John Bradley, ein Shareware- Programm,
das wir mit Erlaubnis des Autors liefern. Es ist ein Grafik-Viewer für
diverse Dateitypen, einschließlich gif, funktionen wie Trimmen,
Strecken u.ä. Mit flmask.

%description -l es.UTF-8
Este es el famoso 'xv' de John Bradley. Es shareware, pero nosotros lo
distribuimos con la permisión de los autores. Es un visor gráfico para
varios tipos de archivos, incluyendo gif, jpg, tiff, xwd, etc. También
posee características de manejo como corte, expansión, etc.

%description -l fr.UTF-8
Le célébre xv de John Bradley. C'est shareware, mais nous le
distribuons avec la permission de l'auteur. C'est un visualiseur
graphique pour de nombreux formats de fichier dont gif, jpg, tiff,
xwd, etc. Il offre aussi des fonctionnalités comme la capture,
l'extension, la retouche de palette, etc. Flmask.

%description -l pl.UTF-8
Słynne 'xv' Johna Bradleya. Jest to program shareware, ale
udostępniamy go za zgodą autora. Jest to przeglądarka plików
graficznych w różnych formatach, takich jak: gif, jpg, tiff, xwd i
innych. Ma też proste możliwości obróbki obrazków, takie jak obcinanie
czy rozszerzanie. Zawiera obsługę flmask.

%description -l pt_BR.UTF-8
Este é o famoso 'xv' de John Bradley. Ele é shareware, mas nós o
distribuimos com a permissão dos autores. É um visualizador gráfico
para vários tipos de arquivos, incluindo gif, jpg, tiff, xwd, etc.
Também possui características de manipulação como corte, expansão,
etc.

%description -l ru.UTF-8
Xv - это программа для просмотра и преобразования изображений для X
Window System. Xv умеет показывать GIF, JPEG, TIFF, PBM, PPM, PDF, X11
bitmap, Utah Raster Toolkit RLE, PDS/VICAR, Sun Rasterfile, BMP, PCX,
IRIS RGB, XPM, Targa, XWD, PostScript(TM) и PM. Xv также умеет делать
простую обработку изображений - cropping, expanding, снимки экрана и
т.п.

%description -l tr.UTF-8
xv başta PNG, GIF, JPG, BMP, XBM, XPM olmak üzere birçok resim
dosyasını görüntüleyebilir, değişik formatlarda kaydedebilir ve
üzerinde boyutlandırma, renk değiştirme gibi bazı temel işlemleri
yapabilir. Çok detaylı işlemler yapamamasına rağmen temel resim
işlemlerinde öncellikle kullanılabilecek, kullanışlı arayüzüne sahip
bir programdır. Flmask.

%description -l uk.UTF-8
Xv - це програма для перегляду та перетворення зображень для X Window
System. Xv вміє показувати GIF, JPEG, TIFF, PBM, PPM, PDF, X11 bitmap,
Utah Raster Toolkit RLE, PDS/VICAR, Sun Rasterfile, BMP, PCX, IRIS
RGB, XPM, Targa, XWD, PostScript(TM) та PM. Xv також вміє робити
просту обробку зображень - cropping, expanding, знімки экрану і т.і.

%package doc
Summary: Manuals in various formats for the xv image viewer
Group: Documentation
%if 0%{?fedora} >= 10 || 0%{?rhel} >= 6
BuildArch: noarch
%endif

%description doc
Manuals in various formats for the xv image viewer, plus technical details
of the various image file formats supported.

%prep
%setup -q -n %{name}-%{vprog} -b 1 -a 5 -a 6

# Apply 20070520 jumbo enhancement patch, bundled with %%{SOURCE1}
%{__patch} -p1 < ../%{name}-%{vprog}-jumbo-fix-enh-patch-%{vjumbo}.txt
%{__rm} ../%{name}-%{vprog}-jumbo-fix-enh-patch-%{vjumbo}.txt

# Fix compiler options, install directories; enable JPEG 2000 support
%patch0 -p1

# Interim jumbo patch update
%patch1 -p1

# Clean up code
%patch2 -p1

# Add FLmask feature (rebased patch; original version won't apply after jumbo patch)
%patch3 -p1

# replace CLK_TCK with sysconf(_SC_CLK_TCK)
%patch4 -p1

# libpng 1.5 compatibility
%patch5 -p0

# NAME_MAX buffer overflow fix
%patch6 -p1

# cut/paste fix for 24bit+ images
%patch7 -p1

# Include permission to distribute
%{__install} -m 0644 -p %{SOURCE2} .

# Recode docs as UTF-8
for F in README.jumbo copyright.h fi/man1/xv.1; do
  iconv -f iso88591 -t utf8 ${F} -o ${F}.utf8 && %{__mv} -f ${F}.utf8 ${F}
done
for F in pl/man1/xvpictoppm.1; do
  iconv -f iso-8859-2 -t utf8 ${F} -o ${F}.utf8 && %{__mv} -f ${F}.utf8 ${F}
done
for F in 00_README CPMASK; do
  iconv -f EUC-JP -t utf8 ${F} -o ${F}.utf8 && %{__mv} -f ${F}.utf8 ${F}
done

# Reorganize docs
#
# Note: Man pages for p?m file formats would conflict with netpbm-progs if installed under %%{_mandir}
%{__mv} 00_README README.FLmask
%{__mv} docs/README README.docs
%{__mkdir} docs/{formats,manuals}/
%{__mv} docs/{bmp.doc,epsf.ps,gif*,p[bgp]m.5,xpm.ps} docs/formats/
%{__mv} docs/{xvdocs.{ps,pdf},xvtitle.ps} docs/manuals/

# HTML manual
%{__mv} -f xvman310a docs/manuals/html

# Fix line endings
for doc in docs/manuals/xv*.ps; do
  %{__sed} -e 's/\r$//' ${doc} > ${doc}.unix
  touch -r ${doc} ${doc}.unix
  %{__mv} -f ${doc}.unix ${doc}
done

# Fix directory location of X libs
%{__sed} -i -e 's@-L/usr/X11R6/lib[[:space:]]@-L%{xlibdir} @' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

desktop-file-install \
  --vendor=livna \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE3}

%{__install} -D -p -m 0644 %{SOURCE4} \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# Non-English man pages
%{__install} -D -p -m 0644 fi/man1/xv.1 \
  %{buildroot}%{_mandir}/fi/man1/xv.1
%{__install} -D -p -m 0644 pl/man1/xvpictoppm.1 \
  %{buildroot}%{_mandir}/pl/man1/xvpictoppm.1

# Populate the docs directory
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{vprog}/
for doc in \
  BUGS \
  CHANGELOG \
  copyright.h \
  CPMASK \
  DISTRIBUTE.txt \
  IDEAS \
  README \
  README.docs \
  README.FLmask \
  README.jumbo \
  README.pcd \
  xv_mgcsfx.sample \
  docs/bigxv.jpg \
  docs/formats/ \
  docs/manuals/
do
  %{__cp} -a ${doc} %{buildroot}%{_docdir}/%{name}-%{vprog}/
done

%clean
%{__rm} -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%if "%{?rhel}" != "4"
# EL-4 doesn't have %%posttrans, nor does it have an icon cache to maintain
%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{vprog}/BUGS
%doc %{_docdir}/%{name}-%{vprog}/CHANGELOG
%doc %{_docdir}/%{name}-%{vprog}/copyright.h
%doc %{_docdir}/%{name}-%{vprog}/CPMASK
%doc %{_docdir}/%{name}-%{vprog}/DISTRIBUTE.txt
%doc %{_docdir}/%{name}-%{vprog}/IDEAS
%doc %{_docdir}/%{name}-%{vprog}/README
%doc %{_docdir}/%{name}-%{vprog}/README.FLmask
%doc %{_docdir}/%{name}-%{vprog}/README.jumbo
%doc %{_docdir}/%{name}-%{vprog}/README.pcd
%doc %{_docdir}/%{name}-%{vprog}/xv_mgcsfx.sample
%{_bindir}/bggen
%{_bindir}/vdcomp
%{_bindir}/xcmap
%{_bindir}/xv
%{_bindir}/xvpictoppm
%{_datadir}/applications/livna-xv.desktop
%{_datadir}/icons/hicolor/48x48/apps/xv.png
%{_mandir}/man1/bggen.1*
%{_mandir}/man1/vdcomp.1*
%{_mandir}/man1/xcmap.1*
%{_mandir}/man1/xv.1*
%{_mandir}/man1/xvpictoppm.1*
%lang(fi) %{_mandir}/fi/man1/xv.1*
%lang(pl) %{_mandir}/pl/man1/xvpictoppm.1*

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{vprog}/README.docs
%doc %{_docdir}/%{name}-%{vprog}/bigxv.jpg
%doc %{_docdir}/%{name}-%{vprog}/formats/
%doc %{_docdir}/%{name}-%{vprog}/manuals/

%changelog
* Thu Mar 28 2013 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-18
- patch for cut/paste bug in 24+ bit mode (by Mark Brader <msb@vex.net>)
- further buffer overflow fix for overly long command line argument

* Thu Mar 14 2013 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-17
- additional fix for long filename buffer overflow

* Mon Mar  4 2013 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-16
- fix buffer overflow caused by filenames longer than the window title limit

* Mon Aug  6 2012 Paul Howarth <paul@city-fan.org> 3.10a.jumbopatch.20070520-15
- rebuild for libtiff.so.5 (libtiff 4.0) in Rawhide

* Thu Feb  9 2012 Nicolas Chauvet <kwizart@gmail.com> 3.10a.jumbopatch.20070520-14
- rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec  9 2011 Paul Howarth <paul@city-fan.org> 3.10a.jumbopatch.20070520-13
- add patch from Gentoo for libpng 1.5 compatibility

* Wed Sep 07 2011 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-12
- fix wait timer (BZ 1929, thanks to Sjoerd Mullender <sjoerd@acm.org>)

* Mon Jul 19 2010 Paul Howarth <paul@city-fan.org> 3.10a.jumbopatch.20070520-11
- drop dependency on man, except for EL-4 build where it's required for
  ownership of %%{_mandir}/{fi,pl} (later releases include these directories
  in the filesystem package)

* Tue Sep 15 2009 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-10
- update desktop file MimeType list (thanks to goeran@uddeborg.se)

* Thu Sep 03 2009 Paul Howarth <paul@city-fan.org> 3.10a.jumbopatch.20070520-9
- clean up prep, build, install, and changelog sections prior to surgery
- include Greg Roelofs' jumbo patch update (20081216)
- drop -imc patch, included in jumbo patch update
- get upstream tarball from ftp.trilon.com
- add patch cleaning up pointer conversions and buffer overflow checks that
  could get optimized out by compilers due to invalid code constructs
- add FLMask patch (rebased; original won't apply over jumbo patch)
- add HTML format manual
- reshuffle documents and put them all in the same directory hierarchy
- require hicolor-icon-theme for ownership of icon directory
- associate image MIME types with xv in desktop file and add scriptlets
- add some manpage translations from PLD
- require man for ownership of translated manpage directories
- add desktop file and package summary/description translations from PLD
- make doc package noarch for F-10, EL-6 onwards
- fix buildreqs, Makefile, and scriptlets for EL-4 compatibility

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 3.10a.jumbopatch.20070520-8
- rebuild for new F11 features

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 3.10a.jumbopatch.20070520-7
- rebuild

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 3.10a.jumbopatch.20070520-6
- rebuild

* Fri Jan 18 2008 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-5
- fix window destroy, file dialog bugs (thanks to <Ian.Collier@comlab.ox.ac.uk>)

* Sun Dec 17 2007 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-4
- added icon

* Fri Dec 14 2007 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-3
- move utf8 cleanup to prep section
- remove redundant BuildRequires
- remove redundant manpages from doc directory
- added desktop file
- split out documentation into separate subpackage

* Wed Dec 12 2007 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-2
- spec file cleanup
- remove redundant doc files, make the rest of them utf8-clean

* Tue Dec 11 2007 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-1
- added DISTRIBUTE.txt - permission to distribute from John Bradley

* Sun Dec 09 2007 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-0
- initial package combining xv with Greg Roelofs' jumbo patches
- patch to adjust makefile: jasper location, prefix, and -g cflag for debuginfo
