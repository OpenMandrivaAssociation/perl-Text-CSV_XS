%define upstream_name    Text-CSV_XS
%define upstream_version 0.76

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Comma-separated values manipulation routines
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tgz

BuildRequires: perl-devel

%description
Text-CSV_XS is a Perl module that provides facilities for the composition
and decomposition of comma-separated values.  An instance of the Text::CSV
class can combine fields into a CSV string and parse a CSV string into
fields.

%prep 
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc MANIFEST ChangeLog README
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.760.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.760.0-1mdv2011.0
+ Revision: 596679
- update to 0.76

* Tue Jul 20 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.730.0-2mdv2011.0
+ Revision: 556165
- rebuild for perl 5.12

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.730.0-1mdv2011.0
+ Revision: 552664
- update to 0.73

* Tue Mar 16 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.720.0-1mdv2010.1
+ Revision: 521633
- update to 0.72

* Fri Feb 19 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.710.0-2mdv2010.1
+ Revision: 508052
- resubmit
- update to 0.71

* Wed Dec 09 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.700.0-1mdv2010.1
+ Revision: 475398
- update to 0.70

* Sat Nov 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.690.0-1mdv2010.1
+ Revision: 462462
- update to 0.69

* Tue Aug 11 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.670.0-2mdv2010.0
+ Revision: 414985
- update to 0.67

* Sun Jul 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.650.0-2mdv2010.0
+ Revision: 395343
- rebuild for automatic version extraction

* Mon Jul 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.650.0-1mdv2010.0
+ Revision: 392900
- update to 0.65
- using %%perl_convert_version
- fixed license field

* Mon May 11 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.64-1mdv2010.0
+ Revision: 374375
- update to new version 0.64

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.58-1mdv2009.1
+ Revision: 318304
- update to new version 0.58

* Thu Jul 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.52-1mdv2009.0
+ Revision: 233434
- new version

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.31-2mdv2008.1
+ Revision: 151406
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2008.0
+ Revision: 55844
- update to new version 0.31

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2008.0
+ Revision: 46698
- update to new version 0.30

* Thu Jun 28 2007 Olivier Thauvin <nanardon@mandriva.org> 0.29-1mdv2008.0
+ Revision: 45434
- 0.29

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.23-11mdv2008.0
+ Revision: 23804
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.23-10mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.23-9mdk
- Fix Previous mistake

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.23-8mdk
- Fix url 
- remove -q 
- Fix BuildRequires
- %%mkrel

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.23-7mdk
- Rebuild for new perl

* Sat Oct 11 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.23-6mdk
- rebuild for new perl
- add Artistic into License tag
- remove $RPM_OPT_FLAGS and PREFIX
- some macrosfification and cosmetic spec changes

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.23-5mdk
- rebuild for new auto{prov,req}

