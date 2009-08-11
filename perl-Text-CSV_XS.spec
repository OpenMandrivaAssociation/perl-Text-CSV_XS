%define upstream_name    Text-CSV_XS
%define upstream_version 0.67

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	Comma-separated values manipulation routines
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tgz

Buildrequires: perl-devel
Buildroot:%{_tmppath}/%{name}-%{version}-%{release}

%description
Text-CSV_XS is a Perl module that provides facilities for the composition
and decomposition of comma-separated values.  An instance of the Text::CSV
class can combine fields into a CSV string and parse a CSV string into
fields.

%prep 
%setup -q -n %{upstream_name}-%{upstream_version}

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
