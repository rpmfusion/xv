Name: xv
Version: 6.1.0
Release: 1%{?dist}
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
URL: https://github.com/jasper-software/xv
Source0: https://github.com/jasper-software/xv/archive/refs/tags/v%{version}.tar.gz
Source2: DISTRIBUTE.txt
Source3: xv.desktop
Source4: xv.png
BuildRequires: cmake >= 3.12
BuildRequires: coreutils
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: hardlink
BuildRequires: jasper-devel
BuildRequires: libexif-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libXt-devel
# Require hicolor-icon-theme for ownership of %%{_datadir}/icons/hicolor/48x48/apps/
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
BuildArch: noarch

%description doc
Manuals in various formats for the xv image viewer, plus technical details
of the various image file formats supported.

%prep
%setup -q -n xv-%{version}

# Include permission to distribute
install -m 0644 -p %{SOURCE2} .

%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir}
%cmake_build

%install
%cmake_install

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE3}

install -D -p -m 0644 %{SOURCE4} \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/xv.png

# Add DISTRIBUTE.txt and NEWS.txt to the docs directory
cp -a DISTRIBUTE.txt NEWS.txt %{buildroot}%{_docdir}/xv/

# Hard link identical documentation files together
hardlink -cv %{buildroot}%{_docdir}/xv/manuals/html/images/

%files
%doc %{_docdir}/xv/BUGS
%doc %{_docdir}/xv/CHANGELOG
%doc %{_docdir}/xv/copyright.h
%doc %{_docdir}/xv/CPMASK
%doc %{_docdir}/xv/DISTRIBUTE.txt
%doc %{_docdir}/xv/IDEAS
%doc %{_docdir}/xv/NEWS.txt
%doc %{_docdir}/xv/README
%doc %{_docdir}/xv/README.FLmask
%doc %{_docdir}/xv/README.jumbo
%doc %{_docdir}/xv/README.pcd
%{_bindir}/bggen
%{_bindir}/vdcomp
%{_bindir}/xcmap
%{_bindir}/xv
%{_bindir}/xvpictoppm
%config(noreplace) %{_sysconfdir}/xv_mgcsfx
%{_datadir}/applications/xv.desktop
%{_datadir}/icons/hicolor/48x48/apps/xv.png
%{_datadir}/pixmaps/xv.xpm
%{_mandir}/man1/bggen.1*
%{_mandir}/man1/vdcomp.1*
%{_mandir}/man1/xcmap.1*
%{_mandir}/man1/xv.1*
%{_mandir}/man1/xvpictoppm.1*
%lang(fi) %{_mandir}/fi/man1/xv.1*
%lang(pl) %{_mandir}/pl/man1/xvpictoppm.1*

%files doc
%doc %{_docdir}/xv/README.docs
%doc %{_docdir}/xv/bigxv.jpg
%doc %{_docdir}/xv/formats/
%doc %{_docdir}/xv/manuals/

%changelog
* Mon Dec  1 2025 Paul Howarth <paul@city-fan.org> - 6.1.0-1
- Update to 6.1.0
  - Add support for EXIF orientation tags (GH#40)
  - Add support for depth 30, or 10bit/color, for compatibility with mode (GH#39)
  - Fix wasJpegUp → wasJp2kUp (GH#38)
- Build with EXIF (orientation) and XRANDR support

* Fri Aug 22 2025 Paul Howarth <paul@city-fan.org> - 6.0.4-1
- Update to 6.0.4
  - Updated URLs for the xv website
  - Fix crash when freeing JPEG comments (GH#37)

* Mon Jul 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 15 2024 Paul Howarth <paul@city-fan.org> - 6.0.2-1
- Update to 6.0.2
  - Added -isize option to control the icon size in the browser: the syntax is
    -isize <width> or -isize <width>x<height>
    If the height is omitted, it defaults to the width * 3/4
  - xv now checks the XV_OPTIONS environment variable before reading the
    command line; xv splits it into words and parses it like command line
    options
    Use XV_OPTIONS to set default options

* Tue Sep 24 2024 Paul Howarth <paul@city-fan.org> - 6.0.1-1
- Update to 6.0.1
  - xvjpeg.c, xvpng.c: Fix gcc warnings on -Wclobbered
  - xvjpeg.c: Fix a bad memory access on jpegs with inverted data
  - Fix xvtext.c overwrite exposed by the link-time optimization fix

* Tue Aug 13 2024 Paul Howarth <paul@city-fan.org> - 6.0.0-1
- Update to 6.0.0
  - Add basic HiDPI support
  - Improve the compatibility of the source code with more modern C standards
    (e.g., C23)
  - Fix the build with link-time optimization (GH#25)
  - Fix many other bugs
- Package NEWS.txt

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Paul Howarth <paul@city-fan.org> - 5.2.0-1
- Update to 5.2.0
  - Made some improvements to WEBP support

* Tue Feb  6 2024 Paul Howarth <paul@city-fan.org> - 5.0.0-1
- Update to 5.0.0
  - Removed all of the obsolete (and no longer used) make/imake-based build
    infrastructure
  - Removed the bundled copies of the source code for the external libraries
    used for JPEG and TIFF support (which were not used anyway)
- Avoid duplicate documentation files by hard linking them together

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Paul Howarth <paul@city-fan.org> - 4.2.0-3
- Rebuilt for new Jasper in Rawhide

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Paul Howarth <paul@city-fan.org> - 4.2.0-1
- Update to 4.2.0
  - Fixed the splash screen to display the correct version number (GH#9, GH#10)

* Thu Jun  8 2023 Paul Howarth <paul@city-fan.org> - 4.1.1-1
- Switch upstream to https://github.com/jasper-software/xv (#6702)
- Add webp support

* Thu Mar 30 2023 Paul Howarth <paul@city-fan.org> - 3.10a.jumbopatch.20070520-43
- Avoid deprecated patch syntax

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.10a.jumbopatch.20070520-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Mar  3 2022 Paul Howarth <paul@city-fan.org> - 3.10a.jumbopatch.20070520-41
- Fix incorrectly applied corrupt GIF patch

* Mon Feb 28 2022 Paul Howarth <paul@city-fan.org> - 3.10a.jumbopatch.20070520-40
- Ignore multiple APP1 data structs; libjpeg can't write them
- Fix segfault seen with some corrupt GIF file
- Report errors from libjpeg
- In file selection box, do not move cursor if no filename is there
- Add fix for colormap in 8-bit JPEG mode
- Add more thorough version of CLK_TCK patch

* Wed Feb 16 2022 Paul Howarth <paul@city-fan.org> - 3.10a.jumbopatch.20070520-39
- Fix Jasper support to use proper library APIs (patch from Michael Adams,
  Jasper upstream maintainer)
- Use a patch rather than iconv to fix documentation encoding
- Honour LDFLAGS if present in the environment

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.10a.jumbopatch.20070520-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.10a.jumbopatch.20070520-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  2 2021 Paul Howarth <paul@city-fan.org> - 3.10a.jumbopatch.20070520-36
- Fix jas_memdump replacement function

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.10a.jumbopatch.20070520-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb  9 2020 Paul Howarth <paul@city-fan.org> - 3.10a.jumbopatch.20070520-34
- Fix FTBFS with GCC 10

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.10a.jumbopatch.20070520-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.10a.jumbopatch.20070520-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.10a.jumbopatch.20070520-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.10a.jumbopatch.20070520-30
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Sat Jul 28 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 3.10a.jumbopatch.20070520-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.10a.jumbopatch.20070520-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.10a.jumbopatch.20070520-27
- Hopefully fix rfbz#3044

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.10a.jumbopatch.20070520-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.10a.jumbopatch.20070520-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec  4 2016 Paul Howarth <paul@city-fan.org> 3.10a.jumbopatch.20070520-24
- rebuild for libjasper.so.4 (jasper 2.0.2) in Rawhide

* Fri Jul 03 2015 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-23
- fix another typo in spec file

* Fri Jul 03 2015 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-22
- fix spec file (use -p1 with utf8 and smoothing patches)

* Fri Jul 03 2015 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-21
- patch by Erling A. Jacobsen to fix iTXt/utf8 png comment bug (#3141, #3704)
- patch by Erling A. Jacobsen to fix smoothing off-by-one bug (#3142)

* Wed Oct 22 2014 Paul Howarth <paul@city-fan.org> 3.10a.jumbopatch.20070520-20
- Fix build with -Werror=format-security

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 3.10a.jumbopatch.20070520-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

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

* Mon Dec 17 2007 Gabriel Somlo <somlo at cmu.edu> 3.10a.jumbopatch.20070520-4
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
