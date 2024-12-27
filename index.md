---
layout: home
title: HA-Lizard RPM Repository
---

## How to Use

### The Easy Way

1. Download the latest HA-Lizard YUM configuration RPM from [our repository](https://github.com/ha-lizard/repo/releases/latest/).
2. Install the HA-Lizard YUM configuration RPM using the `rpm` command.
3. Install or update the `ha-lizard` and `iscsi-ha` packages using the `yum` command.

**Note:** The repositories are **disabled by default** to prevent automatic updates. You must **enable** the repository each time you install or update packages.

```bash
rpm -ivh https://github.com/ha-lizard/repo/releases/latest/download/ha-lizard-repo-__VERSION__-__RELEASE__.x86_64.rpm
yum --enablerepo=ha-lizard* install ha-lizard iscsi-ha
```

#### Testing Unstable Versions

To test an **UNSTABLE** version, you can enable the **testing repository** by adding the **--enablerepo** flag to the yum command:

```bash
yum --enablerepo=testing-ha-lizard install ha-lizard iscsi-ha
```

### The Manual Way

#### Configuring Yum Repositories

Create a repository file at `/etc/yum.repos.d/ha-lizard.repo` with the following content:

```bash
[ha-lizard]
name=HA-Lizard RPM Repository
baseurl=https://ha-lizard.github.io/repo/stable/
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-HA-LIZARD-25

[ha-lizard-epel]
name=Extra Packages for Enterprise Linux 7 - $basearch
metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=$basearch&infra=$infra&content=$contentdir
failovermethod=priority
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

[testing-ha-lizard]
name=HA-Lizard UNSTABLE RPM Repository
baseurl=https://ha-lizard.github.io/repo/unstable/
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-HA-LIZARD-25
```

#### Importing the GPG Key

To ensure package authenticity, download and copy the HA-Lizard GPG key to `/etc/pki/rpm-gpg/RPM-GPG-KEY-HA-LIZARD-25`

```bash
{% include gpg_public_key.asc %}
```

#### Installing HA-Lizard Packages

Once the repositories and GPG key are set up, you can install the ha-lizard and iscsi-ha packages by running:

```bash
yum --enablerepo=ha-lizard* install ha-lizard iscsi-ha
```

## Available RPMs

<h2>Stable RPMs</h2>
<ul>
  {% for rpm in site.data.stable_rpms %}
  <li><a href="{{ site.baseurl }}/stable/{{ rpm.name }}">{{ rpm.name }}</a></li>
{% endfor %}

</ul>

<h2>Unstable RPMs</h2>
<ul>
  {% for rpm in site.data.unstable_rpms %}
  <li><a href="{{ site.baseurl }}/unstable/{{ rpm.name }}">{{ rpm.name }}</a></li>
{% endfor %}
</ul>
