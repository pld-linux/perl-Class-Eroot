%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Eroot
Summary:	Class::Eroot perl module
Summary(pl):	Modu³ perla Class::Eroot
Name:		perl-Class-Eroot
Version:	19960603
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Eroot is a simple object persistence engine that can persist
any datatype. Some objects will need to have an extra method or two
added to their classes, but this is probably the exception rather than
the rule.

%description -l pl
Class::Eroot to prosty mechanizm przechowywania obiektów, który mo¿e
przechowaæ dowolny typ danych. Niektóre obiekty potrzebuj± dodatkowej
metody czy dwóch dodanych do swoich klas, ale to bardziej wyj±tek ni¿
zasada.

%prep
%setup -q -n %{pdir}-%{pnam}

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
