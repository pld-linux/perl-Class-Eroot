%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Eroot
Summary:	Class::Eroot - an eternal root to handle persistent objects
Summary(pl):	Class::Eroot - wieczny "korzeñ" do przechowywania trwa³ych obiektów
Name:		perl-Class-Eroot
Version:	19960603
Release:	10
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71e3a3aafb41275605816c0b547fd403
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Class/*.pm
%{_mandir}/man?/*
