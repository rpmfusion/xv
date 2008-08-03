%define vprog 3.10a
%define vjumbo 20070520

Name: xv
Version: %{vprog}.jumbopatch.%{vjumbo}
Release: 6%{?dist}
Summary: Interactive image display program for X
License: Shareware
Group: Applications/Multimedia
URL: http://www.trilon.com/xv/xv.html
Source0: ftp://ftp.cis.upenn.edu/pub/xv/%{name}-%{vprog}.tar.gz
Source1: http://downloads.sourceforge.net/png-mng/%{name}-%{vprog}-jumbo-patches-%{vjumbo}.tar.gz
Source2: DISTRIBUTE.txt
Source3: %{name}.desktop
Source4: %{name}.png
Patch0: xv-jumbo-20070520-makefile.patch
Patch1: xv-jumbo-20070520-imc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libtiff-devel libpng-devel jasper-devel libXt-devel desktop-file-utils

%package doc
Summary: Documentation files for xv image viewer
Group: Documentation

%description
A shareware program for displaying, grabbing, converting,
and otherwise manipulating graphic image files

%description doc
Documentation files for xv image viewer

%prep
%setup -q -n %{name}-%{vprog}
%setup -q -T -D -b 1 -n %{name}-%{vprog}
%{__patch} -p1 < ../%{name}-%{vprog}-jumbo-fix-enh-patch-%{vjumbo}.txt
%patch0 -p1
%patch1 -p1
%{__install} -m 0644 %{SOURCE2} .
# make doc files utf8-clean:
for F in README.jumbo copyright.h; do
  iconv -f iso88591 -t utf8 ${F} -o ${F}.utf8 && %{__mv} -f ${F}.utf8 ${F}
done

%build
#configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
desktop-file-install --vendor=livna --dir=%{buildroot}/%{_datadir}/applications %{SOURCE3}
%{__install} -D -m 0644 %{SOURCE4} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
# get rid of reduntant doc files:
%{__rm} -f docs/xvdocs.ps docs/xvtitle.ps docs/*.5 docs/*.man

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc DISTRIBUTE.txt copyright.h README README.jumbo
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/48x48/apps/*

%files doc
%defattr(-,root,root)
%doc BUGS CHANGELOG docs IDEAS README.pcd

%changelog
* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 3.10a.jumbopatch.20070520-6
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
