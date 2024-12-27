# Changelog

## [Unreleased]

## [1.0.0] - 2024-12-27

- Rename job names for better clarity: 'Generate YUM repo and HA repo static pages.'
- Modify RPM listing for stable and unstable RPMs to exclude source RPMs and sort them numerically.
- Add version and release extraction step, including prerelease handling, from GitHub tag and commit count.
- Update `ha-lizard.repo` to include testing repository for unstable RPMs.
- Update `index.md` documentation:
  - Add detailed instructions for the easy way to install packages with YUM.
  - Include a section for testing unstable versions using the testing repository.
  - Modify `ha-lizard.repo` configuration instructions with updated repository setup.
  - Add instructions for importing the GPG key.
  - Include instructions for installing HA-Lizard packages once repositories and GPG key are set up.

## [1.0.0-rc1] - 2024-12-20

- Added an RPM spec file for the repository.
- Added YUM repository configuration and GPG keys for the RPM package.
- Implemented a GitHub workflow to create and sign the HA-Lizard repository RPM.
- Added the GPG public key for EPEL 7.
- Added the GPG public key for HA-Lizard.
- Added a new GitHub Actions workflow to build, sign yum repo configuration SRPM and RPM on release.
- Add CHANGELOG.md (this file).
