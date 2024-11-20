---
layout: home
title: HA-Lizard RPM Repository
---

## How to Use

Add the following to your `/etc/yum.repos.d/ha-lizard.repo`:

```bash
[ha-lizard]
name=HA-Lizard RPM Repository
baseurl=https:///ha-lizard.github.io/repo/stable/
enabled=1
gpgcheck=1
gpgkey=https:///ha-lizard.github.io/repo/gpg_key.asc
```

## GPG Key

```bash
{% include gpg_public_key.asc %}
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
