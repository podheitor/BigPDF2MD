# Maintainer: Heitor Faria <heitofaria@gmail.com>

pkgname=bigpdf2md
pkgver=1.0
pkgrel=1
pkgdesc="Dolphin right-click option to convert PDF to Markdown using pymupdf4llm"
arch=('any')
url="https://github.com/podheitor/BigPDF2MD"
license=('GPL')
depends=('python' 'python-pip' 'libnotify' 'dolphin')
install=bigpdf2md.install
source=("$pkgname-$pkgver.tar.gz::https://github.com/podheitor/BigPDF2MD/archive/refs/heads/main.tar.gz")
sha256sums=('SKIP')

package() {
    cd "$srcdir/BigPDF2MD-main"
    
    # Create installation directory
    install -d "$pkgdir/opt/BigPDF2MD"
    
    # Copy scripts
    install -m755 convert.py "$pkgdir/opt/BigPDF2MD/"
    install -m755 run_convert.sh "$pkgdir/opt/BigPDF2MD/"
    
    # Modify run_convert.sh to use /opt path
    sed -i 's|PROJ_DIR=.*|PROJ_DIR="/opt/BigPDF2MD"|' "$pkgdir/opt/BigPDF2MD/run_convert.sh"
    
    # Install ServiceMenu for KDE Plasma 5 and 6
    install -d "$pkgdir/usr/share/kservices5/ServiceMenus"
    install -d "$pkgdir/usr/share/kio/servicemenus"
    
    # Update the Exec path in the desktop file
    sed -i 's|Exec=.*|Exec=/opt/BigPDF2MD/run_convert.sh "%f"|' pdf2md.desktop
    
    install -m644 pdf2md.desktop "$pkgdir/usr/share/kservices5/ServiceMenus/"
    install -m644 pdf2md.desktop "$pkgdir/usr/share/kio/servicemenus/"
}
