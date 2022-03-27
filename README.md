# aur
AUR packages I maintain and co-maintain

# Downloads

I'm using the OpenSUSE Build Service to build binaries for these packages. You can download the built
binary directly or set up a repository for all my packages to be able to auto update. Both
options are available [here](https://software.opensuse.org//download.html?project=home%3Ajustkidding%3Aarch&package=ungoogled-chromium). (ungoogled-chromium example)

## OBS Repository

Add this line to your /etc/pacman.conf

```
[home_justkidding_arch_Arch]
Server = https://downloadcontent.opensuse.org/repositories/home:/justkidding:/arch/Arch/$arch
```

Then execute this commands as root

```
key=$(curl -fsSL https://downloadcontent.opensuse.org/repositories/home:justkidding:arch/Arch/$(uname -m)/home_justkidding_arch_Arch.key)
fingerprint=$(gpg --quiet --with-colons --import-options show-only --import --fingerprint <<< "${key}" | awk -F: '$1 == "fpr" { print $10 }')

pacman-key --init
pacman-key --add - <<< "${key}"
pacman-key --lsign-key "${fingerprint}"
```

After this you should be able to install any packages I maintain.

