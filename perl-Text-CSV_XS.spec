%define module Text-CSV_XS
%define name perl-%{module}
%define version 0.58
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Comma-separated values manipulation routines
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tgz
Buildrequires: perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Text-CSV_XS is a Perl module that provides facilities for the composition
and decomposition of comma-separated values.  An instance of the Text::CSV
class can combine fields into a CSV string and parse a CSV string into
fields.

%prep 
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc MANIFEST ChangeLog README
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
%{_mandir}/*/*

