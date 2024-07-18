%undefine _debugsource_packages
%define modname	Text-CSV_XS

Summary:	Comma-separated values manipulation routines
Name:		perl-%{modname}
Version:	1.55
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{modname}
Source0:	https://cpan.metacpan.org/modules/by-module/Text/%{modname}-%{version}.tgz
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
Obsoletes:	%{name} = 1.460.0-1

%description
Text-CSV_XS is a Perl module that provides facilities for the composition
and decomposition of comma-separated values.  An instance of the Text::CSV
class can combine fields into a CSV string and parse a CSV string into
fields.

%prep 
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc MANIFEST ChangeLog README
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
%{_mandir}/man3/*
