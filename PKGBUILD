# Maintainer: Swix

pkgname=gog-terraria
pkgver=1.4.2.3.47102
pkgrel=1
epoch=1

_gogrel=47102
_gamename=${pkgname#gog-}
_gamename=${_gamename//-/_}
_setupname="setup_${_gamename}_${pkgver}_${_gogrel}.sh"

pkgdesc="The very world is at your fingertips as you fight for survival, fortune, and glory."
url="http://terraria.org/"
license=('custom')
arch=('x86_64')
depends=('sdl2')
makedepends=('libarchive')
optdepends=('firejail: Automatically sandbox this application from your OS')
source=("${_setupname}::gogdownloader://${_gamename}/en3installer0"
        "${pkgname}.desktop"
        "$pkgname"
        "$pkgname.profile")

# bsdtar is really cool but I want to control what I'm extracting
noextract=("${_setupname}")
sha256sums=('f85b08cada31dc31d93f3440c5a661623f9aee06d19bfdc23e909959107ce00d'
            '815bf359c2828cdefee1e33a978a84a2ebb538450197a5792b62e382ae3e3093'
            'ce9c75ce912e6c1c081e7fb9f0a4b49c8cf2274e82da4ead1cab6ab9c527cd79'
            '9ec20a7515dd54a518da4fab006e0b2313deff1c341a3bd163f0e1305b6be5b6')


# You need to download the gog.com installer file manually or with lgogdownloader.
DLAGENTS+=("gogdownloader::/usr/bin/echo %u - This is is not a real URL, you need to download the GOG file manually to \"$PWD/${_setupname}\" or setup a gogdownloader:// DLAGENT. Read this PKGBUILD for more information.")
#DLAGENTS+=("gogdownloader::/usr/bin/lgogdownloader --download-file=%u -o %o")

# Prevent compressing final package
PKGEXT='.pkg.tar'

prepare(){
    datasource="${_setupname}"

    offset=`sed -n '/.*offset=.*head/{s/.*head -n \([0-9]*\).*/\1/p;q}' "$datasource"`
    toskip=`sed -n '/filesizes=/{s/.*="\([0-9]*\)"/\1/p;q}' "$datasource"`

    mkdir "${srcdir}/terraria"
    tail -n+$(($offset+1)) "$datasource" | tail -c+$(($toskip+1)) | bsdtar -C "${srcdir}/terraria" -xvf- 2> /dev/null
}

package(){
    pushd "${srcdir}/terraria/data/noarch"

    # Install game
    install -d "${pkgdir}/opt/${pkgname}/"
    install -d "${pkgdir}/opt/${pkgname}/support"
    install -d "${pkgdir}/usr/bin/"

    cp -r "game/" "${pkgdir}/opt/${pkgname}/"
    find "${pkgdir}/opt/${pkgname}/" -type d -exec chmod 755 "{}" \;
    install -Dm755 "start.sh" \
        "${pkgdir}/opt/${pkgname}/"
    install -Dm755 support/*.{sh,shlib} -t \
        "${pkgdir}/opt/${pkgname}/support"
    install -Dm644 gameinfo \
        "${pkgdir}/opt/${pkgname}/gameinfo"

    # Desktop integration
    install -Dm644 "support/icon.png" \
        "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
    install -Dm644 "docs/End User License Agreement.txt" \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 "${srcdir}/${pkgname}.desktop" \
        "${pkgdir}/usr/share/applications/${pkgname}.desktop"
    install -Dm755 "${srcdir}/${pkgname}" \
        "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 "${srcdir}/${pkgname}.profile" \
        "${pkgdir}/opt/${pkgname}/${pkgname}.profile"

    # Fix permissions
    chmod +x "${pkgdir}/opt/${pkgname}/game/Terraria"{,Server}{,.bin.x86_64}

    popd
}
