#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	CheckDeps
Summary:	Test::CheckDeps - Check for presence of dependencies
Summary(pl.UTF-8):	Test::CheckDeps - sprawdzanie obecności zależności
Name:		perl-Test-CheckDeps
Version:	0.010
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c1893b187e9b2efee7d40b1799218576
URL:		http://search.cpan.org/dist/Test-CheckDeps/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-CPAN-Meta >= 2.120920
BuildRequires:	perl-CPAN-Meta-Check >= 0.007
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds a test that assures all dependencies have been
installed properly. If requested, it can bail out all testing on
error.

%description -l pl.UTF-8
Ten moduł dodaje test sprawdzający, czy wszystkie zależności zostały
właściwie zainstalowane. Jeśli tego zażądano, może przerwać testy w
przypadku błędu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/CheckDeps.pm
%{_mandir}/man3/Test::CheckDeps.3pm*
