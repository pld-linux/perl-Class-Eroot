%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Eroot
Summary:	Class::Eroot perl module
Summary(pl):	Modu³ perla Class::Eroot
Name:		perl-Class-Eroot
Version:	19960603
Release:	9
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Class::Eroot");' \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Class/*.pm
%{_mandir}/man?/*
