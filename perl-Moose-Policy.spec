%define upstream_name    Moose-Policy
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Moose-mounted police
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Moose/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
This module allows you to specify your project-wide or even company-wide
Moose meta-policy. 

Most all of Moose's features can be customized through the use of custom
metaclasses, however fiddling with the metaclasses can be hairy.
Moose::Policy removes most of that hairiness and makes it possible to
cleanly contain a set of meta-level customizations in one easy to use
module.

This is still an release of this module and it should not be considered to
be complete by any means. It is very basic implemenation at this point and
will likely get more feature-full over time, as people request features. So
if you have a suggestion/need/idea, please speak up.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 659084
- update to new version 0.05
- rebuild for updated spec-helper

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 472194
- update to 0.04

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2010.0
+ Revision: 430507
- rebuild

* Sat Jul 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
+ Revision: 234135
- import perl-Moose-Policy


* Sat Jul 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
- initial mdv release, generated with cpan2dist
