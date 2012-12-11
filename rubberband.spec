%define		major		2
%define		libname		%mklibname %{name} %{major}
%define		develname	%mklibname -d %{name}

Summary:	Audio time-stretching and pitch-shifting library
Name:		rubberband
Version:	1.7.0
Release:	1
License:	GPLv2
Group:		System/Libraries
URL:		http://www.breakfastquay.com/rubberband/
Source0:	http://www.breakfastquay.com/rubberband/files/%{name}-%{version}.tar.bz2
Source1:	http://www.breakfastquay.com/rubberband/usage.txt
Patch1:		rubberband-1.5.0-mk.patch
# incorrect version in configure.ac (harmless) and .pc.in (could be bad
# if a consumer strictly requires 1.5.0 functionality);
# e-mailed to author
Patch2:		rubberband-1.7.0-fix_ver.patch
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig
BuildRequires:	vamp-plugin-sdk-devel
Requires:	%{libname} = %{version}-%{release}

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n %{libname}
Summary:	Audio time-stretching and pitch-shifting library
Group:		System/Libraries

%description -n %{libname}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n %{develname}
Summary:	Development files for rubberband
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another. This
package contains files needed to develop with the rubberband library.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%__cp %{SOURCE1} .

%build
autoreconf -fiv
%__sed -i 's|{exec_prefix}/lib|{exec_prefix}/%{_lib}|' rubberband.pc.in
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

# lib64 fix
%__perl -pi -e "s|/lib\b|/%{_lib}|g" %{buildroot}%{_libdir}/pkgconfig/rubberband.pc

%files
%doc usage.txt CHANGELOG
%{_bindir}/rubberband

%files -n %{libname}
%{_libdir}/librubberband.so.%{major}*
%{_libdir}/ladspa/ladspa-rubberband.cat
%{_libdir}/ladspa/ladspa-rubberband.so
%{_datadir}/ladspa/rdf/ladspa-rubberband.rdf
%{_libdir}/vamp/vamp-rubberband.cat
%{_libdir}/vamp/vamp-rubberband.so

%files -n %{develname}
%{_includedir}/rubberband
%{_libdir}/librubberband.so
%{_libdir}/librubberband.a
%{_libdir}/pkgconfig/rubberband.pc


%changelog
* Sun Feb 05 2012 Andrey Bondrov <abondrov@mandriva.org> 1.7.0-1
+ Revision: 771204
- New version 1.7.0, update patches, drop no longer needed stuff from spec

* Mon Oct 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.0-1
+ Revision: 704059
- update to new version 1.6.0
- sync patches with Fedora

* Sun Aug 29 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.0-1mdv2011.0
+ Revision: 574019
- update to new version 1.5.0
- drop patch 1
- rediff patch 2
- Patch3: fix wrong versions

* Wed Mar 24 2010 Caio Begotti <caio1982@mandriva.org> 1.3-3mdv2010.1
+ Revision: 527211
- bump for a new gcc fix which makes it linkable with the new vamp-plugin-sdk

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Mar 17 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3-1mdv2009.1
+ Revision: 356967
- update to new version 1.3

* Mon Aug 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2-1mdv2009.0
+ Revision: 275857
- Patch2: fix installation on x86_64
- update to new version 1.2
- bump major
- drop patch 0, fixed upstream
- Patch1: fix compiling with gcc43
- obsolete old major library
- spec file clean

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2008.1
+ Revision: 182979
- import rubberband


* Sun Mar 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2008.1
- initial Mandriva release

* Wed Feb 20 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.1-3
- rebuild for new version of vamp-plugins-sdk (1.1b)
- fixed typo that meant the pkgconfig file was not being installed

* Fri Dec 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 1.0.1-1
- initial build.
