%include	/usr/lib/rpm/macros.perl
Summary:	Class::Eroot perl module
Summary(pl):	Modu³ perla Class::Eroot
Name:		perl-Class-Eroot
Version:	19960603
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Class/Class-Eroot-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Eroot is a simple object persistence engine that can persist any
datatype.  Some objects will need to have an extra method or two added to
their classes, but this is probably the exception rather than the rule.

%prep
%setup -q -n Class-Eroot

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_sitelib}/Class

install Eroot.pm $RPM_BUILD_ROOT%{perl_sitelib}
install Template.pm $RPM_BUILD_ROOT%{perl_sitelib}/Class

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/*.pm
%dir %{perl_sitelib}/Class
%{perl_sitelib}/Class/*.pm
