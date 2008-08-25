%define	major 2
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Audio time-stretching and pitch-shifting library
Name:		rubberband
Version:	1.2
Release:	%mkrel 1
License:	GPLv2
Group:		System/Libraries
URL:		http://www.breakfastquay.com/rubberband/
Source0:	http://www.breakfastquay.com/rubberband/files/%{name}-%{version}.tar.bz2
Source1:	http://www.breakfastquay.com/rubberband/usage.txt
Patch1:		%{name}-1.2-gcc43.patch
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkgconfig
BuildRequires:	vamp-plugin-sdk-devel
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n %{libname}
Summary:	Audio time-stretching and pitch-shifting library
Group:		System/Libraries
Obsoletes:	%{mklibname %{name} 0} < 1.2

%description -n %{libname}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n %{develname}
Summary:	Development files for rubberband
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname %{name} -d} < 1.2

%description -n	%{develname}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another. This
package contains files needed to develop with the rubberband library.

%prep
%setup -q
%patch1 -p1

cp %{SOURCE1} .

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mv %{buildroot}%{_libdir}/librubberband.so %{buildroot}%{_libdir}/librubberband.so.%{major}
ln -snf librubberband.so.%{major} %{buildroot}%{_libdir}/librubberband.so

# lib64 fix
perl -pi -e "s|/lib\b|/%{_lib}|g" %{buildroot}%{_libdir}/pkgconfig/rubberband.pc

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc usage.txt
%{_bindir}/rubberband

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/librubberband.so.%{major}*
%{_libdir}/ladspa/ladspa-rubberband.cat
%{_libdir}/ladspa/ladspa-rubberband.so
%{_datadir}/ladspa/rdf/ladspa-rubberband.rdf
%{_libdir}/vamp/vamp-rubberband.cat
%{_libdir}/vamp/vamp-rubberband.so

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/rubberband
%{_libdir}/librubberband.so
%{_libdir}/librubberband.a
%{_libdir}/pkgconfig/rubberband.pc
