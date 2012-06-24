Summary:	A library of sound-related functions
Summary(pl):	Biblioteka funkcji zwi�zanych z d�wi�kiem
Name:		sndlib
# based on sndlib.h.in and actual tarball date
Version:	20.2.20061225
Release:	1
# sndins included in sources is LGPL'd, but not packaged
License:	free (see COPYING)
Group:		Libraries
Source0:	ftp://ccrma-ftp.stanford.edu/pub/Lisp/%{name}.tar.gz
# Source0-md5:	440f882dfcbcfe6fca25ece552b1c048
URL:		http://ccrma.stanford.edu/software/snd/sndlib/
BuildRequires:	guile-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The sndlib library is a collection of sound file and audio hardware
handlers written in C and running currently on SGI (either audio
library), Sun, OSS or ALSA (Linux and others), MacOS X, HPUX, and
Windows systems. It provides relatively straightforward access to many
sound file headers and data types, and most of the features of the
audio hardware.

%description -l pl
Biblioteka sndlib to zbi�r funkcji obs�uguj�cych pliki d�wi�kowe i
sprz�t napisanych w C i dzia�aj�cych aktualnie na systemach SGI (z
dowoln� bibliotek� d�wi�kow�), Sun, OSS, ALSA (na Linuksie i innych
systemach), MacOS X, HPUX i Windows. Udost�pnia w miar� prosty dost�p
do wielu funkcji i typ�w danych zwi�zanych z plikami d�wi�kowymi oraz
wi�kszo�ci mo�liwo�ci sprz�tu d�wi�kowego.

%package devel
Summary:	Header files for sndlib library
Summary(pl):	Pliki nag��wkowe biblioteki sndlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for sndlib library.

%description devel -l pl
Pliki nag��wkowe biblioteki sndlib.

%package static
Summary:	Static sndlib library
Summary(pl):	Statyczna biblioteka sndlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static sndlib library.

%description static -l pl
Statyczna biblioteka sndlib.

%prep
%setup -q -n %{name}

%build
%configure
%{__make} \
	SO_LD="%{__cc} -Wl,-soname=libsndlib.so"

%install
rm -rf $RPM_BUILD_ROOT

# SO_LD because library is relinked (wrong makefile rule)
%{__make} install \
	SO_LD="%{__cc} -Wl,-soname=libsndlib.so" \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING HISTORY.sndlib README.sndlib *.html
%attr(755,root,root) %{_libdir}/libsndlib.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sndlib-config
%{_includedir}/sndlib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsndlib.a
