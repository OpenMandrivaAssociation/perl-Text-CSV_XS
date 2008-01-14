%define name perl-Text-CSV_XS
%define module Text-CSV_XS
%define version 0.31
%define release %mkrel 2

Name:		%{name}
Summary:	Text-CSV_XS module for Perl (String_Lang_Text_Proc/Text)
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{module}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-buildroot
Buildrequires: perl-devel

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc MANIFEST ChangeLog README
%{perl_vendorarch}/Text/*
%{perl_vendorarch}/auto/Text/*
%{_mandir}/*/*

