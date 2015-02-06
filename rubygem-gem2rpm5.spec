# Generated from gem2rpm5-0.6.1.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	gem2rpm5

Summary:	Generate rpm specfiles from gems
Name:		rubygem-%{rbname}

Version:	0.6.7
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://wiki.mandriva.com/en/Policies/Ruby
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	locales-en
BuildArch:	noarch

%description
Generate source rpms and rpm spec files from a Ruby Gem. The spec file is
adapted to first of all follow Mandriva Linux packaging guidelines, using
rpm5's gem_helper, while following the gem as much as necessary to remain
compatible without the bloat.

%prep
%setup -q

%build
export LC_ALL=en_US.UTF-8
%gem_build

%install
%gem_install

%files
%{_bindir}/gem2rpm5
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/AUTHORS
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/gem2rpm5
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.7-1
+ Revision: 774256
- don't add buildrequires on rake for building ruby extensions anymore as it's
  now provided by the ruby standard library

* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.6-1
+ Revision: 773462
- new version updated to work with ruby 1.9

* Wed Oct 05 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.5-1
+ Revision: 703092
- new version
- remove legacy rpm stuff
- remove duplicated file from %%files

* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.4-2
+ Revision: 643308
- fix group of -doc packages produced..

* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.4-1
+ Revision: 643305
- new release

* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.3-1
+ Revision: 643256
- ship docs with main package
- new release: 0.6.3
- fix URL
- new release 0.6.2:
  	o remove newline on top of spec
  	o use %%setup in stead of %%gem_unpack
  	o use doc/%%{name}-%%{version} rather than hardcoding it in %%files
- imported package rubygem-gem2rpm5


* Sun Oct 17 2010 Per Øyvind Karlsen <peroyvind@lappis> 0.6.1-1
- Initial package
