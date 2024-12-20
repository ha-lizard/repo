%define version      __VERSION__
%define release      __RELEASE__

Name:           ha-lizard-repo
Version:        %{version}
Release:        %{release}
Summary:        Repository configuration for HA-Lizard packages
Packager:       HA-Lizard Team
Group:          Productivity/Clustering/HA
BuildArch:      x86_64
License:        GPLv3
URL:            https://www.ha-lizard.com
Source0:        ha-lizard-repo.tar.gz

%description
This package provides the repository configuration for HA-Lizard packages,
as well as the GPG key used to verify those packages. It simplifies the
process of enabling and managing the HA-Lizard repository for users.

Key Features:
* Easy repository setup for HA-Lizard packages
* Includes EPEL 7 repository to allow DRBD and TGT packages
* Includes GPG key for package verification
* Compatible with YUM and DNF package managers

%prep
# Preparing the build environment by unpacking the source tarball
echo "Preparing build environment."
%setup -q -c

%build
# No build steps required, placeholder section
echo "Building skipped."

%install
# Cleaning the buildroot directory to ensure a clean build
rm -rf %{buildroot}
# mkdir -p %{buildroot}%{docdir}

# Install the repository file into the yum configuration directory
install -Dpm 644 rpm/ha-lizard.repo %{buildroot}%{_sysconfdir}/yum.repos.d/ha-lizard.repo
# Install the GPG keys into the appropriate system directory
install -Dpm 644 rpm/RPM-GPG-KEY-HA-LIZARD-25 %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-HA-LIZARD-25
install -Dpm 644 rpm/RPM-GPG-KEY-EPEL-7 %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
# Install the GPL License file into the documentation directory
install -Dpm 644 LICENSE %{buildroot}%{_docdir}/%{name}/LICENSE

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/LICENSE
%config(noreplace) /etc/yum.repos.d/ha-lizard.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-HA-LIZARD-25
/etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

# INFO: Do not put anything after the changelog macro. github actions will add the changelog there.
%changelog
