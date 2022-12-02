#!/bin/bash
cat >> "/etc/pacman.conf" << EOF
[home_justkidding_arch_Arch]
Server = https://downloadcontent.opensuse.org/repositories/home:/justkidding:/arch/Arch/\$arch
EOF

key=$(curl -fsSL https://download.opensuse.org/repositories/home:justkidding:arch/Arch/$(uname -m)/home_justkidding_arch_Arch.key)
fingerprint=$(gpg --quiet --with-colons --import-options show-only --import --fingerprint <<< "${key}" | awk -F: '$1 == "fpr" { print $10 }')

pacman-key --init
pacman-key --add - <<< "${key}"
pacman-key --lsign-key "${fingerprint}"
