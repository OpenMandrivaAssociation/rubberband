%define         major        2
%define         libname      %mklibname %{name} %{major}
%define         develname    %mklibname -d %{name}

%define         vampdir      %{_libdir}/vamp
%define         ladspadir    %{_libdir}/ladspa
%define         pkgconfdir   %{_libdir}/pkgconfig

Summary:        Audio time-stretching and pitch-shifting library
Name:           rubberband
Version:        1.9.0
Release:        1
License:        GPLv2
Group:          System/Libraries
URL:            http://www.breakfastquay.com/rubberband/
Source0:        http://www.breakfastquay.com/rubberband/files/%{name}-%{version}.tar.bz2
Source1:        http://www.breakfastquay.com/rubberband/usage.txt

BuildRequires:  pkgconfig(fftw3)
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig
BuildRequires:  vamp-plugin-sdk-devel
Requires:       %{libname} = %{version}-%{release}

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n %{libname}
Summary:        Audio time-stretching and pitch-shifting library
Group:          System/Libraries

%description -n %{libname}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n %{develname}
Summary:        Development files for rubberband
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another. This
package contains files needed to develop with the rubberband library.

%prep
%setup -q
cp %{SOURCE1} .
%autopatch -p1

%build
autoreconf -fiv

%configure --libdir=%{_libdir}
%make_build all

%install
%make_install  INSTALL_LIBDIR="%{_libdir}" INSTALL_VAMPDIR="%vampdir" INSTALL_LADSPADIR="%ladspadir" INSTALL_PKGDIR="%pkgconfdir"

%files
%doc usage.txt CHANGELOG
%{_bindir}/rubberband

%files -n %{libname}
%{_libdir}/librubberband.so.%{major}{,.*}
%ladspadir/*.cat
%ladspadir/*.so
%vampdir/*.cat
%vampdir/*.so
%{_datadir}/ladspa/rdf/ladspa-rubberband.rdf


%files -n %{develname}
%{_includedir}/rubberband
%{_libdir}/*.so
%{_libdir}/*.a
%pkgconfdir/rubberband.pc
