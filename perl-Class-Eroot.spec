%define		pdir	Class
%define		pnam	Eroot
%include	/usr/lib/rpm/macros.perl
Summary:	Class::Eroot - an eternal root to handle persistent objects
Summary(pl.UTF-8):	Class::Eroot - wieczny "korzeń" do przechowywania trwałych obiektów
Name:		perl-Class-Eroot
Version:	19960603
Release:	12
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71e3a3aafb41275605816c0b547fd403
URL:		http://search.cpan.org/dist/Class-Eroot/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Eroot is a simple object persistence engine that can persist
any datatype. Some objects will need to have an extra method or two
added to their classes, but this is probably the exception rather than
the rule.

%description -l pl.UTF-8
Class::Eroot to prosty mechanizm przechowywania obiektów, który może
przechować dowolny typ danych. Niektóre obiekty potrzebują dodatkowej
metody czy dwóch dodanych do swoich klas, ale to bardziej wyjątek niż
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
