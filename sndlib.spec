Summary:	A library of sound-related functions
Summary(pl.UTF-8):   Biblioteka funkcji związanych z dźwiękiem
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

%description -l pl.UTF-8
Biblioteka sndlib to zbiór funkcji obsługujących pliki dźwiękowe i
sprzęt napisanych w C i działających aktualnie na systemach SGI (z
dowolną biblioteką dźwiękową), Sun, OSS, ALSA (na Linuksie i innych
systemach), MacOS X, HPUX i Windows. Udostępnia w miarę prosty dostęp
do wielu funkcji i typów danych związanych z plikami dźwiękowymi oraz
większości możliwości sprzętu dźwiękowego.

%package devel
Summary:	Header files for sndlib library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki sndlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for sndlib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sndlib.

%package static
Summary:	Static sndlib library
Summary(pl.UTF-8):   Statyczna biblioteka sndlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static sndlib library.

%description static -l pl.UTF-8
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
