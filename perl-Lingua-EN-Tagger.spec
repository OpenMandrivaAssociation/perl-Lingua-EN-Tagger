%define upstream_name    Lingua-EN-Tagger
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Part-of-speech tagger for English natural language processing
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Spec)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(Lingua::Stem)
BuildRequires: perl(Memoize)
BuildRequires: perl(Memoize::ExpireLRU)
BuildRequires: perl(Storable)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The module is a probability based, corpus-trained tagger that assigns POS
tags to English text based on a lookup dictionary and a set of probability
values. The tagger assigns appropriate tags based on conditional
probabilities - it examines the preceding tag to determine the appropriate
tag for the current word. Unknown words are classified according to word
morphology or can be set to be treated as nouns or other parts of speech.

The tagger also extracts as many nouns and noun phrases as it can, using a
set of regular expressions.

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
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


