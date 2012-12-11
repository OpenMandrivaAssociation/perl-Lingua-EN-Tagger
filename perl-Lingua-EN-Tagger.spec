%define upstream_name    Lingua-EN-Tagger
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Part-of-speech tagger for English natural language processing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(Lingua::Stem)
BuildRequires:	perl(Memoize)
BuildRequires:	perl(Memoize::ExpireLRU)
BuildRequires:	perl(Storable)

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.160.0-3mdv2011.0
+ Revision: 658861
- rebuild for updated spec-helper

* Sun Oct 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 586230
- Usage of serialized data structures make the package arch-dependant

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 552389
- update to 0.16

* Wed Apr 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.1
+ Revision: 532706
- import perl-Lingua-EN-Tagger


* Wed Apr 07 2010 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist
