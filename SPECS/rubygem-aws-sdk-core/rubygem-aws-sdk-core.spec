%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name aws-sdk-core

Name: rubygem-aws-sdk-core
Version:        3.22.1
Release:        2%{?dist}
Summary:        Provides API clients for AWS.
Group:          Development/Languages
License:        Apache 2.0
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/aws-sdk-core-%{version}.gem
%define sha1    aws-sdk-core=df2a4868ff82002b13ae1dd1b2210971dfa48f37
BuildRequires:  ruby

Requires: rubygem-aws-eventstream >= 1.0
Requires: rubygem-aws-partitions >= 1.0
Requires: rubygem-aws-sigv4 >= 1.0
Requires: rubygem-jmespath >= 1.0

%description
Provides API clients for AWS. This gem is part of the official AWS SDK for Ruby..

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
*   Mon Feb 4 2019 Sujay G <gsujay@vmware.com> 3.22.1-2
-   Increment the release version as part of ruby upgrade
*   Mon Jul 30 2018 Srinidhi Rao <srinidhir@vmware.com> 3.22.1-1
-   Initial build
