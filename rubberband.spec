%define	major 0
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Audio time-stretching and pitch-shifting library
Name:		rubberband
Version:	1.0.1
Release:	%mkrel 1
License:	GPL
Group:		System/Libraries
URL:		http://www.breakfastquay.com/rubberband/
Source0:	http://www.breakfastquay.com/rubberband/files/rubberband-%{version}.tar.bz2
Source1:	http://www.breakfastquay.com/rubberband/usage.txt
Patch0:		rubberband-soname.diff
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkgconfig
BuildRequires:	vamp-plugin-sdk-devel
Requires:	%{libname} = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n	%{libname}
Summary:	Audio time-stretching and pitch-shifting library
Group:          System/Libraries

%description -n	%{libname}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n	%{develname}
Summary:	Development files for rubberband
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n	%{develname}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another. This
package contains files needed to develop with the rubberband library.

%prep

%setup -q
%patch0 -p0

cp %{SOURCE1} .

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

make \
    INSTALL_BINDIR=%{buildroot}%{_bindir} \
    INSTALL_INCDIR=%{buildroot}%{_includedir}/rubberband \
    INSTALL_LIBDIR=%{buildroot}%{_libdir} \
    INSTALL_VAMPDIR=%{buildroot}%{_libdir}/vamp \
    INSTALL_LADSPADIR=%{buildroot}%{_libdir}/ladspa \
    INSTALL_PKGDIR=%{buildroot}%{_libdir}/pkgconfig \
    install

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
%defattr(-,root,root,-)
%doc usage.txt
%{_bindir}/rubberband

%files -n %{libname}
%defattr(-,root,root,-)
%doc COPYING README
%{_libdir}/librubberband.so.%{major}
%{_libdir}/ladspa/ladspa-rubberband.cat
%{_libdir}/ladspa/ladspa-rubberband.so
%{_libdir}/vamp/vamp-rubberband.cat
%{_libdir}/vamp/vamp-rubberband.so

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/rubberband
%{_libdir}/librubberband.so
%{_libdir}/librubberband.a
%{_libdir}/pkgconfig/rubberband.pc

