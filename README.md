# qemu
My custom package of the full build of qemu for RHEL/CentOS

## Building the binary RPM
This process is covered well in the
[Red Hat Enterprise Linux docs](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/packaging_and_distributing_software/index#building-binary-rpms_building-rpms)
but in a nutshell it's this (for RHEL 8+) ...

    sudo subscription-manager repos \
        --enable=rhel-8-for-x86_64-baseos-rpms \
        --enable=rhel-8-for-x86_64-appstream-rpms \
        --enable=codeready-builder-for-rhel-8-x86_64-rpms

    sudo yum -y install git rpmdevtools yum-utils \
        https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

    cd
    rpmdev-setuptree

    git clone https://github.com/ajacocks/qemu.git
    cp qemu/qemu5.spec rpmbuild/SPECS/

    cd rpmbuild/SOURCES/
    curl -LO https://download.qemu.org/qemu-5.2.0.tar.xz

    cd ~/rpmbuild/SPECS/
    sudo yum-builddep qemu5.spec
    rpmbuild -bb qemu5.spec

The built RPM is located in ...

    ~/rpmbuild/RPMS/x86_64/qemu52-5.2.0-1.el8.x86_64.rpm

