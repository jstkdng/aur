# [archlinux-docker][] [![ci-badge][]][ci] [![gitter-badge][]][gitter]

[archlinux-docker]: https://github.com/2m/archlinux-docker
[ci]:               https://github.com/2m/archlinux-docker/actions
[ci-badge]:         https://github.com/2m/archlinux-docker/workflows/ci/badge.svg
[gitter]:           https://gitter.im/2m/general
[gitter-badge]:     https://badges.gitter.im/2m/general.svg

This is a Dockerfile that builds on top of the official Arch Linux ([archlinux/base][]) base image and adds features for convenient Arch Linux package building.

[archlinux/base]: https://hub.docker.com/r/archlinux/base

## Features

* rebuilds the image in [Docker Hub][] whenever the base image is updated
* on every image build the `mirrorlist` is switched to the [Arch Linux Archive][] repositories of the date the base image was built
* contains `yay` to easily build AUR packages
* contains other tools for general maintenance, like `grep`, `difftools`, etc.

[Docker Hub]:         https://hub.docker.com/r/martynas/archlinux/builds
[Arch Linux Archive]: https://wiki.archlinux.org/index.php/Arch_Linux_Archive

## Usage

This Docker image is currently used by the following projects:

* [2m/arch-pkgbuild-builder][] — Arch Linux PKGBUILD GitHub builder action

[2m/arch-pkgbuild-builder]: https://github.com/2m/arch-pkgbuild-builder
