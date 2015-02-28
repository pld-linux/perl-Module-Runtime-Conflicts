#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Runtime-Conflicts
%include	/usr/lib/rpm/macros.perl
Summary:	Module::Runtime::Conflicts - Provide information on conflicts for Module::Runtime
Name:		perl-Module-Runtime-Conflicts
Version:	0.001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	310e525981ac1338f247626b8ce53dff
URL:		http://search.cpan.org/dist/Module-Runtime-Conflicts/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Module::Build::Tiny)
BuildRequires:	perl-Dist-CheckConflicts
BuildRequires:	perl-Module-Runtime
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides conflicts checking for Module::Runtime, which had
a recent release that broke some versions of Moose. It is called from
Moose::Conflicts and moose-outdated.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Module/Runtime
%{_mandir}/man3/*
