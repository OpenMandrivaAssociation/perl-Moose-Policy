%define module   Moose-Policy
%define version    0.03
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Moose-mounted police
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Moose/%{module}-%{version}.tar.gz
BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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


