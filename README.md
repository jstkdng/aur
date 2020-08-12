# aur
AUR packages I maintain and co-maintain

# Downloads

I'm using the OpenSUSE Build Service to build binaries for these packages. You can download them
from the OBS itself or from a mirror of the OBS I maintain. You could also configure a repository
on your `/etc/pacman.conf` to keep everything updated.

First, add my public key to pacman's key database.

```bash
$ sudo pacman-key -r 3DEA62513C8035383A245A12E5786B42E8E5D565
$ sudo pacman-key --lsign-key 3DEA62513C8035383A245A12E5786B42E8E5D565
```

Then, add these lines to the end of your `/etc/pacman.conf` file

```
[jk-aur]
Server = https://repo.vin.ovh/arch/$arch
```

Finally, update pacman's repository database: `sudo pacman -Sy`

*TODO: Add configuration for OBS's repository*
