%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Audio time-stretching and pitch-shifting library
Name:		rubberband
Version:	1.8.1
Release:	2
License:	GPLv2
Group:		System/Libraries
URL:		http://www.breakfastquay.com/rubberband/
Source0:	http://www.breakfastquay.com/rubberband/files/%{name}-%{version}.tar.bz2
Source1:	http://www.breakfastquay.com/rubberband/usage.txt
Patch1:		rubberband-1.5.0-mk.patch
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
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
%apply_patches

cp %{SOURCE1} .

%build
autoreconf -fiv
sed -i 's|{exec_prefix}/lib|{exec_prefix}/%{_lib}|' rubberband.pc.in
%configure
%make

%install
%makeinstall_std

# lib64 fix
perl -pi -e "s|/lib\b|/%{_lib}|g" %{buildroot}%{_libdir}/pkgconfig/rubberband.pc

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
