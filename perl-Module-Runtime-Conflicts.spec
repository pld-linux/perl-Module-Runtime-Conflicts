#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Runtime-Conflicts
Summary:	Module::Runtime::Conflicts - provide information on conflicts for Module::Runtime
Summary(pl.UTF-8):	Module::Runtime::Conflicts - dostarczanie informacji o konfliktach dla Module::Runtime
Name:		perl-Module-Runtime-Conflicts
Version:	0.003
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	67aaf699072063cc00c5b6afd4c67a6f
URL:		https://metacpan.org/release/Module-Runtime-Conflicts
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Dist-CheckConflicts
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Test-Simple >= 0.88
%endif
Conflicts:	perl-Elasticsearch < 1.00
Conflicts:	perl-Moose < 2.1202
Conflicts:	perl-MooseX-NonMoose < 0.24
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides conflicts checking for Module::Runtime, which had
a recent release that broke some versions of Moose. It is called from
Moose::Conflicts and moose-outdated.

%description -l pl.UTF-8
Ten moduł zapewnia sprawdzanie konfliktów dla Module::Runtime, htórego
niedawne wydanie zepsuło niektóre wersje Moose. Moduł jest wywoływany
z Moose::Conflicts oraz moose-outdated.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Module/Runtime
%{perl_vendorlib}/Module/Runtime/Conflicts.pm
%{_mandir}/man3/Module::Runtime::Conflicts.3pm*
