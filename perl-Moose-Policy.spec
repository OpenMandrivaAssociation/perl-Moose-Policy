%define upstream_name    Moose-Policy
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Moose-mounted police
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Moose/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
