#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Audio-Musepack
Version  : 1.0.1
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/D/DA/DANIEL/Audio-Musepack-1.0.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DANIEL/Audio-Musepack-1.0.1.tar.gz
Summary  : 'An object-oriented interface to Musepack file information and APE tag fields.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Audio-Musepack-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Audio::Scan)
BuildRequires : perl(Module::Install)

%description
Audio::Musepack version 1.0
=======================
how to install the module, any machine dependencies it may have (for
example C compilers and installed libraries) and any other information
that should be provided before the module is installed.

%package dev
Summary: dev components for the perl-Audio-Musepack package.
Group: Development
Provides: perl-Audio-Musepack-devel = %{version}-%{release}
Requires: perl-Audio-Musepack = %{version}-%{release}

%description dev
dev components for the perl-Audio-Musepack package.


%package perl
Summary: perl components for the perl-Audio-Musepack package.
Group: Default
Requires: perl-Audio-Musepack = %{version}-%{release}

%description perl
perl components for the perl-Audio-Musepack package.


%prep
%setup -q -n Audio-Musepack-1.0.1
cd %{_builddir}/Audio-Musepack-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Audio::APE.3
/usr/share/man/man3/Audio::Musepack.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
