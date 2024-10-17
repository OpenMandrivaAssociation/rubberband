%define         major        2
%define         libname      %mklibname %{name}
%define         oldlibname      %mklibname %{name} 2
%define         develname    %mklibname -d %{name}

%define         vampdir      %{_libdir}/vamp
%define         ladspadir    %{_libdir}/ladspa
%define         pkgconfdir   %{_libdir}/pkgconfig

Summary:        Audio time-stretching and pitch-shifting library
Name:           rubberband
Version:        3.3.0
Release:        1
License:        GPLv2
Group:          System/Libraries
URL:            https://www.breakfastquay.com/rubberband/
Source0:        http://www.breakfastquay.com/rubberband/files/%{name}-%{version}.tar.bz2
Source1:        http://www.breakfastquay.com/rubberband/usage.txt

BuildRequires:  meson
BuildRequires:  atomic-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  ladspa-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(vamp-sdk)
Requires:       %{libname} = %{version}-%{release}

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n %{libname}
Summary:        Audio time-stretching and pitch-shifting library
Group:          System/Libraries
%rename  %{oldlibname}

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
export LDFLAGS="%{optflags} -latomic"
%meson -Djni=disabled
%meson_build

%install
%meson_install

%files
%doc usage.txt CHANGELOG
%{_bindir}/rubberband
%{_bindir}/rubberband-r3

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
%{_libdir}/lv2/rubberband.lv2/
%pkgconfdir/rubberband.pc
