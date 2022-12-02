FROM archlinux:base-devel

LABEL maintainer="jk@vin.ovh"

# create build user
RUN useradd --create-home build
RUN echo "build ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# configure default gpg key server to a more reliable one
COPY gpg.conf /home/build/.gnupg/gpg.conf
RUN chown -R build:build /home/build/.gnupg
RUN chmod 700 /home/build/.gnupg
RUN chmod 600 /home/build/.gnupg/gpg.conf

# add OpenSUSE Build Service repository
COPY add-obs-repo.sh /tmp/add-obs-repo.sh
RUN /tmp/add-obs-repo.sh

# update keyring first
RUN yes | pacman -Sy archlinux-keyring

# update and install packages
RUN yes | pacman -Syu git wget python-jinja python-srcinfo

USER build
WORKDIR /home/build

# install yay which can be used to install AUR dependencies
#RUN git clone https://aur.archlinux.org/yay.git
#RUN cd yay && makepkg --syncdeps --install --rmdeps --noconfirm
#RUN cd .. && rm -rf yay

# switch back to root for regular usage
USER root
WORKDIR /

# slim image
RUN yes | pacman -Scc

