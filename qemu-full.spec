%global debug_package %{nil}
%global latest_release %(curl 'https://download.qemu.org/' 2>/dev/null | sed -e 's|<[^>]*>||g' -e 's/\.xz.*/.xz/' | egrep '^qemu-.*xz' | egrep -v 'rc[0-9]+' | sort -V | tail -1 | sed -e 's/^qemu-//' -e 's/\.tar.xz$//')

Name:           qemu-full
Version:        %{latest_release}
Release:        1%{?dist}
Summary:        QEMU is a FAST! processor emulator
License:        GPLv2+ and LGPLv2+ and BSD
URL:            http://www.qemu.org/
Source0:        https://download.qemu.org/qemu-%{version}.tar.xz

%define	_prefix	/opt/qemu-%{version}

# Group 'Development Tools'
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconf-m4
BuildRequires:  pkgconf-pkg-config
BuildRequires:  redhat-rpm-config
BuildRequires:  rpm-build
BuildRequires:  rpm-sign
BuildRequires:  strace
BuildRequires:  asciidoc
BuildRequires:  byacc
BuildRequires:  ctags
BuildRequires:  diffstat
BuildRequires:  git
BuildRequires:  intltool
BuildRequires:  jna
BuildRequires:  ltrace
BuildRequires:  patchutils
BuildRequires:  perl-Fedora-VSP
BuildRequires:  perl-generators
BuildRequires:  pesign
BuildRequires:  source-highlight
BuildRequires:  systemtap
BuildRequires:  valgrind
BuildRequires:  valgrind-devel

# from https://wiki.qemu.org/Hosts/Linux
BuildRequires:  capstone-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libfdt-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdrm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libiscsi-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libnfs-devel
BuildRequires:  libslirp-devel
BuildRequires:  libxml2-devel
BuildRequires:  lzo-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  pixman-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-sphinx
BuildRequires:  SDL2-devel
BuildRequires:  snappy-devel
BuildRequires:  spice-server-devel
BuildRequires:  systemd-devel
BuildRequires:  virglrenderer-devel
BuildRequires:  vte291-devel
BuildRequires:  zlib-devel

Requires:       capstone
Requires:       git
Requires:       glib2
Requires:       gtk3
Requires:       libcurl
Requires:       libdrm
Requires:       libepoxy
Requires:       libfdt
Requires:       libslirp
Requires:       mesa-libgbm
Requires:       ncurses
Requires:       pixman
Requires:       pulseaudio-libs
Requires:       python3
Requires:       SDL2
Requires:       virglrenderer
Requires:       vte291
Requires:       zlib

%description
QEMU is a generic and open source processor emulator which achieves a good
emulation speed by using dynamic translation. QEMU has two operating modes:

 * Full system emulation. In this mode, QEMU emulates a full system (for
   example a PC), including a processor and various peripherials. It can be
   used to launch different Operating Systems without rebooting the PC or
   to debug system code.
 * User mode emulation. In this mode, QEMU can launch Linux processes compiled
   for one CPU on another CPU.

As QEMU requires no host kernel patches to run, it is safe and easy to use.

%prep
%setup -n qemu-%{version}

%build
./configure --prefix=/opt/qemu-%{version} --enable-plugins
#./configure --prefix=%{buildroot}/usr
#./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
install -m 0755 -d %{_buildrootdir}/opt/qemu-%{version}/share/doc/qemu
install -m 0644 %{_builddir}/qemu-%{version}/LICENSE %{buildroot}/opt/qemu-%{version}/share/doc/qemu/LICENSE
install -m 0644 %{_builddir}/qemu-%{version}/MAINTAINERS %{buildroot}/opt/qemu-%{version}/share/doc/qemu/MAINTAINERS

#mv %{_buildrootdir}/qemu-%{version}-%{release}.%{_arch} %{_buildrootdir}/qemu52-%{version}-%{release}.%{_arch}

%files
%defattr(-,root,root,-)
%{_bindir}/elf2dmp
%{_bindir}/qemu-aarch64
%{_bindir}/qemu-aarch64_be
%{_bindir}/qemu-alpha
%{_bindir}/qemu-arm
%{_bindir}/qemu-armeb
%{_bindir}/qemu-cris
%{_bindir}/qemu-edid
%{_bindir}/qemu-ga
%{_bindir}/qemu-hppa
%{_bindir}/qemu-i386
%{_bindir}/qemu-img
%{_bindir}/qemu-io
%{_bindir}/qemu-keymap
%{_bindir}/qemu-m68k
%{_bindir}/qemu-microblaze
%{_bindir}/qemu-microblazeel
%{_bindir}/qemu-mips
%{_bindir}/qemu-mips64
%{_bindir}/qemu-mips64el
%{_bindir}/qemu-mipsel
%{_bindir}/qemu-mipsn32
%{_bindir}/qemu-mipsn32el
%{_bindir}/qemu-nbd
%{_bindir}/qemu-nios2
%{_bindir}/qemu-or1k
%{_bindir}/qemu-ppc
%{_bindir}/qemu-ppc64
%{_bindir}/qemu-ppc64le
%{_bindir}/qemu-pr-helper
%{_bindir}/qemu-riscv32
%{_bindir}/qemu-riscv64
%{_bindir}/qemu-s390x
%{_bindir}/qemu-sh4
%{_bindir}/qemu-sh4eb
%{_bindir}/qemu-sparc
%{_bindir}/qemu-sparc32plus
%{_bindir}/qemu-sparc64
%{_bindir}/qemu-storage-daemon
%{_bindir}/qemu-system-aarch64
%{_bindir}/qemu-system-alpha
%{_bindir}/qemu-system-arm
%{_bindir}/qemu-system-avr
%{_bindir}/qemu-system-cris
%{_bindir}/qemu-system-hppa
%{_bindir}/qemu-system-i386
%{_bindir}/qemu-system-m68k
%{_bindir}/qemu-system-microblaze
%{_bindir}/qemu-system-microblazeel
%{_bindir}/qemu-system-mips
%{_bindir}/qemu-system-mips64
%{_bindir}/qemu-system-mips64el
%{_bindir}/qemu-system-mipsel
%{_bindir}/qemu-system-moxie
%{_bindir}/qemu-system-nios2
%{_bindir}/qemu-system-or1k
%{_bindir}/qemu-system-ppc
%{_bindir}/qemu-system-ppc64
%{_bindir}/qemu-system-riscv32
%{_bindir}/qemu-system-riscv64
%{_bindir}/qemu-system-rx
%{_bindir}/qemu-system-s390x
%{_bindir}/qemu-system-sh4
%{_bindir}/qemu-system-sh4eb
%{_bindir}/qemu-system-sparc
%{_bindir}/qemu-system-sparc64
%{_bindir}/qemu-system-tricore
%{_bindir}/qemu-system-x86_64
%{_bindir}/qemu-system-xtensa
%{_bindir}/qemu-system-xtensaeb
%{_bindir}/qemu-x86_64
%{_bindir}/qemu-xtensa
%{_bindir}/qemu-xtensaeb
%{_datadir}/applications/qemu.desktop
%{_datadir}/icons/hicolor/16x16/apps/qemu.png
%{_datadir}/icons/hicolor/24x24/apps/qemu.png
%{_datadir}/icons/hicolor/32x32/apps/qemu.png
%{_datadir}/icons/hicolor/32x32/apps/qemu.bmp
%{_datadir}/icons/hicolor/48x48/apps/qemu.png
%{_datadir}/icons/hicolor/64x64/apps/qemu.png
%{_datadir}/icons/hicolor/128x128/apps/qemu.png
%{_datadir}/icons/hicolor/256x256/apps/qemu.png
%{_datadir}/icons/hicolor/512x512/apps/qemu.png
%{_datadir}/icons/hicolor/scalable/apps/qemu.svg
%{_datadir}/locale/bg/LC_MESSAGES/qemu.mo
%{_datadir}/locale/de_DE/LC_MESSAGES/qemu.mo
%{_datadir}/locale/fr_FR/LC_MESSAGES/qemu.mo
%{_datadir}/locale/hu/LC_MESSAGES/qemu.mo
%{_datadir}/locale/it/LC_MESSAGES/qemu.mo
%{_datadir}/locale/sv/LC_MESSAGES/qemu.mo
%{_datadir}/locale/tr/LC_MESSAGES/qemu.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/qemu.mo
%dir %{_datadir}/qemu
%{_datadir}/qemu/trace-events-all
%{_datadir}/qemu/edk2-aarch64-code.fd
%{_datadir}/qemu/edk2-arm-code.fd
%{_datadir}/qemu/edk2-arm-vars.fd
%{_datadir}/qemu/edk2-i386-code.fd
%{_datadir}/qemu/edk2-i386-secure-code.fd
%{_datadir}/qemu/edk2-i386-vars.fd
%{_datadir}/qemu/edk2-x86_64-code.fd
%{_datadir}/qemu/edk2-x86_64-secure-code.fd
%dir %{_datadir}/qemu/keymaps
%{_datadir}/qemu/keymaps/ar
%{_datadir}/qemu/keymaps/bepo
%{_datadir}/qemu/keymaps/cz
%{_datadir}/qemu/keymaps/da
%{_datadir}/qemu/keymaps/de
%{_datadir}/qemu/keymaps/de-ch
%{_datadir}/qemu/keymaps/en-gb
%{_datadir}/qemu/keymaps/en-us
%{_datadir}/qemu/keymaps/es
%{_datadir}/qemu/keymaps/et
%{_datadir}/qemu/keymaps/fi
%{_datadir}/qemu/keymaps/fo
%{_datadir}/qemu/keymaps/fr
%{_datadir}/qemu/keymaps/fr-be
%{_datadir}/qemu/keymaps/fr-ca
%{_datadir}/qemu/keymaps/fr-ch
%{_datadir}/qemu/keymaps/hr
%{_datadir}/qemu/keymaps/hu
%{_datadir}/qemu/keymaps/is
%{_datadir}/qemu/keymaps/it
%{_datadir}/qemu/keymaps/ja
%{_datadir}/qemu/keymaps/lt
%{_datadir}/qemu/keymaps/lv
%{_datadir}/qemu/keymaps/mk
%{_datadir}/qemu/keymaps/nl
%{_datadir}/qemu/keymaps/no
%{_datadir}/qemu/keymaps/pl
%{_datadir}/qemu/keymaps/pt
%{_datadir}/qemu/keymaps/pt-br
%{_datadir}/qemu/keymaps/ru
%{_datadir}/qemu/keymaps/th
%{_datadir}/qemu/keymaps/tr
%{_datadir}/qemu/keymaps/sl
%{_datadir}/qemu/keymaps/sv
%dir %{_datadir}/qemu/vhost-user
%{_datadir}/qemu/vhost-user/50-qemu-gpu.json
%{_datadir}/qemu/bios.bin
%{_datadir}/qemu/bios-256k.bin
%{_datadir}/qemu/bios-microvm.bin
%{_datadir}/qemu/qboot.rom
%{_datadir}/qemu/sgabios.bin
%{_datadir}/qemu/vgabios.bin
%{_datadir}/qemu/vgabios-cirrus.bin
%{_datadir}/qemu/vgabios-stdvga.bin
%{_datadir}/qemu/vgabios-vmware.bin
%{_datadir}/qemu/vgabios-qxl.bin
%{_datadir}/qemu/vgabios-virtio.bin
%{_datadir}/qemu/vgabios-ramfb.bin
%{_datadir}/qemu/vgabios-bochs-display.bin
%{_datadir}/qemu/vgabios-ati.bin
%{_datadir}/qemu/openbios-sparc32
%{_datadir}/qemu/openbios-sparc64
%{_datadir}/qemu/openbios-ppc
%{_datadir}/qemu/QEMU,tcx.bin
%{_datadir}/qemu/QEMU,cgthree.bin
%{_datadir}/qemu/pxe-e1000.rom
%{_datadir}/qemu/pxe-eepro100.rom
%{_datadir}/qemu/pxe-ne2k_pci.rom
%{_datadir}/qemu/pxe-pcnet.rom
%{_datadir}/qemu/pxe-rtl8139.rom
%{_datadir}/qemu/pxe-virtio.rom
%{_datadir}/qemu/efi-e1000.rom
%{_datadir}/qemu/efi-eepro100.rom
%{_datadir}/qemu/efi-ne2k_pci.rom
%{_datadir}/qemu/efi-pcnet.rom
%{_datadir}/qemu/efi-rtl8139.rom
%{_datadir}/qemu/efi-virtio.rom
%{_datadir}/qemu/efi-e1000e.rom
%{_datadir}/qemu/efi-vmxnet3.rom
%{_datadir}/qemu/qemu-nsis.bmp
%{_datadir}/qemu/bamboo.dtb
%{_datadir}/qemu/canyonlands.dtb
%{_datadir}/qemu/petalogix-s3adsp1800.dtb
%{_datadir}/qemu/petalogix-ml605.dtb
%{_datadir}/qemu/multiboot.bin
%{_datadir}/qemu/linuxboot.bin
%{_datadir}/qemu/linuxboot_dma.bin
%{_datadir}/qemu/kvmvapic.bin
%{_datadir}/qemu/pvh.bin
%{_datadir}/qemu/s390-ccw.img
%{_datadir}/qemu/s390-netboot.img
%{_datadir}/qemu/slof.bin
%{_datadir}/qemu/skiboot.lid
%{_datadir}/qemu/palcode-clipper
%{_datadir}/qemu/u-boot.e500
%{_datadir}/qemu/u-boot-sam460-20100605.bin
%{_datadir}/qemu/qemu_vga.ndrv
%{_datadir}/qemu/edk2-licenses.txt
%{_datadir}/qemu/hppa-firmware.img
%{_datadir}/qemu/opensbi-riscv32-generic-fw_dynamic.bin
%{_datadir}/qemu/opensbi-riscv64-generic-fw_dynamic.bin
%{_datadir}/qemu/opensbi-riscv32-generic-fw_dynamic.elf
%{_datadir}/qemu/opensbi-riscv64-generic-fw_dynamic.elf
%{_datadir}/qemu/npcm7xx_bootrom.bin
%dir %{_datadir}/qemu/firmware
%{_datadir}/qemu/firmware/50-edk2-i386-secure.json
%{_datadir}/qemu/firmware/50-edk2-x86_64-secure.json
%{_datadir}/qemu/firmware/60-edk2-aarch64.json
%{_datadir}/qemu/firmware/60-edk2-arm.json
%{_datadir}/qemu/firmware/60-edk2-i386.json
%{_datadir}/qemu/firmware/60-edk2-x86_64.json
%dir %{_docdir}/qemu
%dir %{_docdir}/qemu/interop
%dir %{_docdir}/qemu/interop/_static
%doc %{_docdir}/qemu/interop/_static/pygments.css
%doc %{_docdir}/qemu/interop/_static/ajax-loader.gif
%doc %{_docdir}/qemu/interop/_static/basic.css
%doc %{_docdir}/qemu/interop/_static/comment-bright.png
%doc %{_docdir}/qemu/interop/_static/comment-close.png
%doc %{_docdir}/qemu/interop/_static/comment.png
%doc %{_docdir}/qemu/interop/_static/doctools.js
%doc %{_docdir}/qemu/interop/_static/documentation_options.js
%doc %{_docdir}/qemu/interop/_static/down-pressed.png
%doc %{_docdir}/qemu/interop/_static/down.png
%doc %{_docdir}/qemu/interop/_static/file.png
%doc %{_docdir}/qemu/interop/_static/jquery-3.2.1.js
%doc %{_docdir}/qemu/interop/_static/jquery.js
%doc %{_docdir}/qemu/interop/_static/minus.png
%doc %{_docdir}/qemu/interop/_static/plus.png
%doc %{_docdir}/qemu/interop/_static/searchtools.js
%doc %{_docdir}/qemu/interop/_static/underscore-1.3.1.js
%doc %{_docdir}/qemu/interop/_static/underscore.js
%doc %{_docdir}/qemu/interop/_static/up-pressed.png
%doc %{_docdir}/qemu/interop/_static/up.png
%doc %{_docdir}/qemu/interop/_static/websupport.js
%doc %{_docdir}/qemu/interop/_static/alabaster.css
%doc %{_docdir}/qemu/interop/_static/custom.css
%doc %{_docdir}/qemu/interop/bitmaps.html
%doc %{_docdir}/qemu/interop/dbus.html
%doc %{_docdir}/qemu/interop/dbus-vmstate.html
%doc %{_docdir}/qemu/interop/index.html
%doc %{_docdir}/qemu/interop/live-block-operations.html
%doc %{_docdir}/qemu/interop/pr-helper.html
%doc %{_docdir}/qemu/interop/qemu-ga.html
%doc %{_docdir}/qemu/interop/qemu-ga-ref.html
%doc %{_docdir}/qemu/interop/qemu-qmp-ref.html
%doc %{_docdir}/qemu/interop/vhost-user.html
%doc %{_docdir}/qemu/interop/vhost-user-gpu.html
%doc %{_docdir}/qemu/interop/vhost-vdpa.html
%doc %{_docdir}/qemu/interop/genindex.html
%doc %{_docdir}/qemu/interop/search.html
%doc %{_docdir}/qemu/interop/.buildinfo
%doc %{_docdir}/qemu/interop/searchindex.js
%doc %{_docdir}/qemu/interop/objects.inv
%dir %{_docdir}/qemu/tools
%dir %{_docdir}/qemu/tools/_static
%doc %{_docdir}/qemu/tools/_static/pygments.css
%doc %{_docdir}/qemu/tools/_static/ajax-loader.gif
%doc %{_docdir}/qemu/tools/_static/basic.css
%doc %{_docdir}/qemu/tools/_static/comment-bright.png
%doc %{_docdir}/qemu/tools/_static/comment-close.png
%doc %{_docdir}/qemu/tools/_static/comment.png
%doc %{_docdir}/qemu/tools/_static/doctools.js
%doc %{_docdir}/qemu/tools/_static/documentation_options.js
%doc %{_docdir}/qemu/tools/_static/down-pressed.png
%doc %{_docdir}/qemu/tools/_static/down.png
%doc %{_docdir}/qemu/tools/_static/file.png
%doc %{_docdir}/qemu/tools/_static/jquery-3.2.1.js
%doc %{_docdir}/qemu/tools/_static/jquery.js
%doc %{_docdir}/qemu/tools/_static/minus.png
%doc %{_docdir}/qemu/tools/_static/plus.png
%doc %{_docdir}/qemu/tools/_static/searchtools.js
%doc %{_docdir}/qemu/tools/_static/underscore-1.3.1.js
%doc %{_docdir}/qemu/tools/_static/underscore.js
%doc %{_docdir}/qemu/tools/_static/up-pressed.png
%doc %{_docdir}/qemu/tools/_static/up.png
%doc %{_docdir}/qemu/tools/_static/websupport.js
%doc %{_docdir}/qemu/tools/_static/alabaster.css
%doc %{_docdir}/qemu/tools/_static/custom.css
%doc %{_docdir}/qemu/tools/index.html
%doc %{_docdir}/qemu/tools/qemu-img.html
%doc %{_docdir}/qemu/tools/qemu-nbd.html
%doc %{_docdir}/qemu/tools/qemu-pr-helper.html
%doc %{_docdir}/qemu/tools/qemu-trace-stap.html
%doc %{_docdir}/qemu/tools/virtfs-proxy-helper.html
%doc %{_docdir}/qemu/tools/virtiofsd.html
%doc %{_docdir}/qemu/tools/genindex.html
%doc %{_docdir}/qemu/tools/search.html
%doc %{_docdir}/qemu/tools/.buildinfo
%doc %{_docdir}/qemu/tools/searchindex.js
%doc %{_docdir}/qemu/tools/objects.inv
%dir %{_docdir}/qemu/specs
%dir %{_docdir}/qemu/specs/_static
%doc %{_docdir}/qemu/specs/_static/pygments.css
%doc %{_docdir}/qemu/specs/_static/ajax-loader.gif
%doc %{_docdir}/qemu/specs/_static/basic.css
%doc %{_docdir}/qemu/specs/_static/comment-bright.png
%doc %{_docdir}/qemu/specs/_static/comment-close.png
%doc %{_docdir}/qemu/specs/_static/comment.png
%doc %{_docdir}/qemu/specs/_static/doctools.js
%doc %{_docdir}/qemu/specs/_static/documentation_options.js
%doc %{_docdir}/qemu/specs/_static/down-pressed.png
%doc %{_docdir}/qemu/specs/_static/down.png
%doc %{_docdir}/qemu/specs/_static/file.png
%doc %{_docdir}/qemu/specs/_static/jquery-3.2.1.js
%doc %{_docdir}/qemu/specs/_static/jquery.js
%doc %{_docdir}/qemu/specs/_static/minus.png
%doc %{_docdir}/qemu/specs/_static/plus.png
%doc %{_docdir}/qemu/specs/_static/searchtools.js
%doc %{_docdir}/qemu/specs/_static/underscore-1.3.1.js
%doc %{_docdir}/qemu/specs/_static/underscore.js
%doc %{_docdir}/qemu/specs/_static/up-pressed.png
%doc %{_docdir}/qemu/specs/_static/up.png
%doc %{_docdir}/qemu/specs/_static/websupport.js
%doc %{_docdir}/qemu/specs/_static/alabaster.css
%doc %{_docdir}/qemu/specs/_static/custom.css
%doc %{_docdir}/qemu/specs/acpi_hest_ghes.html
%doc %{_docdir}/qemu/specs/acpi_hw_reduced_hotplug.html
%doc %{_docdir}/qemu/specs/index.html
%doc %{_docdir}/qemu/specs/ppc-spapr-numa.html
%doc %{_docdir}/qemu/specs/ppc-spapr-xive.html
%doc %{_docdir}/qemu/specs/ppc-xive.html
%doc %{_docdir}/qemu/specs/tpm.html
%doc %{_docdir}/qemu/specs/genindex.html
%doc %{_docdir}/qemu/specs/search.html
%doc %{_docdir}/qemu/specs/.buildinfo
%doc %{_docdir}/qemu/specs/searchindex.js
%doc %{_docdir}/qemu/specs/objects.inv
%dir %{_docdir}/qemu/system
%dir %{_docdir}/qemu/system/arm
%doc %{_docdir}/qemu/system/arm/aspeed.html
%doc %{_docdir}/qemu/system/arm/collie.html
%doc %{_docdir}/qemu/system/arm/cpu-features.html
%doc %{_docdir}/qemu/system/arm/digic.html
%doc %{_docdir}/qemu/system/arm/gumstix.html
%doc %{_docdir}/qemu/system/arm/integratorcp.html
%doc %{_docdir}/qemu/system/arm/mps2.html
%doc %{_docdir}/qemu/system/arm/musca.html
%doc %{_docdir}/qemu/system/arm/musicpal.html
%doc %{_docdir}/qemu/system/arm/nseries.html
%doc %{_docdir}/qemu/system/arm/nuvoton.html
%doc %{_docdir}/qemu/system/arm/orangepi.html
%doc %{_docdir}/qemu/system/arm/palm.html
%doc %{_docdir}/qemu/system/arm/raspi.html
%doc %{_docdir}/qemu/system/arm/realview.html
%doc %{_docdir}/qemu/system/arm/sbsa.html
%doc %{_docdir}/qemu/system/arm/stellaris.html
%doc %{_docdir}/qemu/system/arm/sx1.html
%doc %{_docdir}/qemu/system/arm/versatile.html
%doc %{_docdir}/qemu/system/arm/vexpress.html
%doc %{_docdir}/qemu/system/arm/virt.html
%doc %{_docdir}/qemu/system/arm/xlnx-versal-virt.html
%doc %{_docdir}/qemu/system/arm/xscale.html
%dir %{_docdir}/qemu/system/i386
%doc %{_docdir}/qemu/system/i386/microvm.html
%doc %{_docdir}/qemu/system/i386/pc.html
%dir %{_docdir}/qemu/system/s390x
%doc %{_docdir}/qemu/system/s390x/3270.html
%doc %{_docdir}/qemu/system/s390x/bootdevices.html
%doc %{_docdir}/qemu/system/s390x/css.html
%doc %{_docdir}/qemu/system/s390x/protvirt.html
%doc %{_docdir}/qemu/system/s390x/vfio-ap.html
%doc %{_docdir}/qemu/system/s390x/vfio-ccw.html
%dir %{_docdir}/qemu/system/_static
%doc %{_docdir}/qemu/system/_static/pygments.css
%doc %{_docdir}/qemu/system/_static/ajax-loader.gif
%doc %{_docdir}/qemu/system/_static/basic.css
%doc %{_docdir}/qemu/system/_static/comment-bright.png
%doc %{_docdir}/qemu/system/_static/comment-close.png
%doc %{_docdir}/qemu/system/_static/comment.png
%doc %{_docdir}/qemu/system/_static/doctools.js
%doc %{_docdir}/qemu/system/_static/documentation_options.js
%doc %{_docdir}/qemu/system/_static/down-pressed.png
%doc %{_docdir}/qemu/system/_static/down.png
%doc %{_docdir}/qemu/system/_static/file.png
%doc %{_docdir}/qemu/system/_static/jquery-3.2.1.js
%doc %{_docdir}/qemu/system/_static/jquery.js
%doc %{_docdir}/qemu/system/_static/minus.png
%doc %{_docdir}/qemu/system/_static/plus.png
%doc %{_docdir}/qemu/system/_static/searchtools.js
%doc %{_docdir}/qemu/system/_static/underscore-1.3.1.js
%doc %{_docdir}/qemu/system/_static/underscore.js
%doc %{_docdir}/qemu/system/_static/up-pressed.png
%doc %{_docdir}/qemu/system/_static/up.png
%doc %{_docdir}/qemu/system/_static/websupport.js
%doc %{_docdir}/qemu/system/_static/alabaster.css
%doc %{_docdir}/qemu/system/_static/custom.css
%doc %{_docdir}/qemu/system/build-platforms.html
%doc %{_docdir}/qemu/system/cpu-hotplug.html
%doc %{_docdir}/qemu/system/deprecated.html
%doc %{_docdir}/qemu/system/gdb.html
%doc %{_docdir}/qemu/system/images.html
%doc %{_docdir}/qemu/system/index.html
%doc %{_docdir}/qemu/system/invocation.html
%doc %{_docdir}/qemu/system/ivshmem.html
%doc %{_docdir}/qemu/system/keys.html
%doc %{_docdir}/qemu/system/license.html
%doc %{_docdir}/qemu/system/linuxboot.html
%doc %{_docdir}/qemu/system/managed-startup.html
%doc %{_docdir}/qemu/system/monitor.html
%doc %{_docdir}/qemu/system/mux-chardev.html
%doc %{_docdir}/qemu/system/net.html
%doc %{_docdir}/qemu/system/pr-manager.html
%doc %{_docdir}/qemu/system/qemu-block-drivers.html
%doc %{_docdir}/qemu/system/qemu-cpu-models.html
%doc %{_docdir}/qemu/system/qemu-manpage.html
%doc %{_docdir}/qemu/system/quickstart.html
%doc %{_docdir}/qemu/system/security.html
%doc %{_docdir}/qemu/system/target-arm.html
%doc %{_docdir}/qemu/system/target-avr.html
%doc %{_docdir}/qemu/system/target-i386.html
%doc %{_docdir}/qemu/system/target-m68k.html
%doc %{_docdir}/qemu/system/target-mips.html
%doc %{_docdir}/qemu/system/target-ppc.html
%doc %{_docdir}/qemu/system/target-rx.html
%doc %{_docdir}/qemu/system/target-s390x.html
%doc %{_docdir}/qemu/system/target-sparc.html
%doc %{_docdir}/qemu/system/target-sparc64.html
%doc %{_docdir}/qemu/system/target-xtensa.html
%doc %{_docdir}/qemu/system/targets.html
%doc %{_docdir}/qemu/system/tls.html
%doc %{_docdir}/qemu/system/usb.html
%doc %{_docdir}/qemu/system/virtio-net-failover.html
%doc %{_docdir}/qemu/system/virtio-pmem.html
%doc %{_docdir}/qemu/system/vnc-security.html
%doc %{_docdir}/qemu/system/genindex.html
%doc %{_docdir}/qemu/system/search.html
%doc %{_docdir}/qemu/system/.buildinfo
%doc %{_docdir}/qemu/system/searchindex.js
%doc %{_docdir}/qemu/system/objects.inv
%dir %{_docdir}/qemu/user
%dir %{_docdir}/qemu/user/_static
%doc %{_docdir}/qemu/user/_static/pygments.css
%doc %{_docdir}/qemu/user/_static/ajax-loader.gif
%doc %{_docdir}/qemu/user/_static/basic.css
%doc %{_docdir}/qemu/user/_static/comment-bright.png
%doc %{_docdir}/qemu/user/_static/comment-close.png
%doc %{_docdir}/qemu/user/_static/comment.png
%doc %{_docdir}/qemu/user/_static/doctools.js
%doc %{_docdir}/qemu/user/_static/documentation_options.js
%doc %{_docdir}/qemu/user/_static/down-pressed.png
%doc %{_docdir}/qemu/user/_static/down.png
%doc %{_docdir}/qemu/user/_static/file.png
%doc %{_docdir}/qemu/user/_static/jquery-3.2.1.js
%doc %{_docdir}/qemu/user/_static/jquery.js
%doc %{_docdir}/qemu/user/_static/minus.png
%doc %{_docdir}/qemu/user/_static/plus.png
%doc %{_docdir}/qemu/user/_static/searchtools.js
%doc %{_docdir}/qemu/user/_static/underscore-1.3.1.js
%doc %{_docdir}/qemu/user/_static/underscore.js
%doc %{_docdir}/qemu/user/_static/up-pressed.png
%doc %{_docdir}/qemu/user/_static/up.png
%doc %{_docdir}/qemu/user/_static/websupport.js
%doc %{_docdir}/qemu/user/_static/alabaster.css
%doc %{_docdir}/qemu/user/_static/custom.css
%doc %{_docdir}/qemu/user/index.html
%doc %{_docdir}/qemu/user/main.html
%doc %{_docdir}/qemu/user/genindex.html
%doc %{_docdir}/qemu/user/search.html
%doc %{_docdir}/qemu/user/.buildinfo
%doc %{_docdir}/qemu/user/searchindex.js
%doc %{_docdir}/qemu/user/objects.inv
%doc %{_docdir}/qemu/index.html
%license %{_docdir}/qemu/LICENSE
%doc %{_docdir}/qemu/MAINTAINERS
%doc %{_mandir}/man8/qemu-ga.8
%doc %{_mandir}/man8/qemu-nbd.8
%doc %{_mandir}/man8/qemu-pr-helper.8
%doc %{_mandir}/man7/qemu-ga-ref.7
%doc %{_mandir}/man7/qemu-qmp-ref.7
%doc %{_mandir}/man7/qemu-block-drivers.7
%doc %{_mandir}/man7/qemu-cpu-models.7
%doc %{_mandir}/man1/qemu-img.1
%doc %{_mandir}/man1/qemu.1
%{_libexecdir}/qemu-bridge-helper
%{_libexecdir}/vhost-user-gpu

%changelog
* Fri Feb 26 2021 <alexander@redhat.com>
- Initial revision of package
