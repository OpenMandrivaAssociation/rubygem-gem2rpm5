# Generated from gem2rpm5-0.6.1.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	gem2rpm5

Summary:	Generate rpm specfiles from gems
Name:		rubygem-%{rbname}

Version:	0.6.3
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby                     
URL:		http://wiki.mandriva.com/en/Policies/Ruby
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Generate source rpms and rpm spec files from a Ruby Gem. The spec file is
adapted to first of all follow Mandriva Linux packaging guidelines, using
rpm5's gem_helper, while following the gem as much as necessary to remain
compatible without the bloat.

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/gem2rpm5
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/gem2rpm5
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.template
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.template
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/AUTHORS
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
