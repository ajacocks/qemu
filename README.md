# qemu
My custom package of the full build of qemu for RHEL/CentOS

## Building the binary RPM
This process is covered well in the
[Red Hat Enterprise Linux docs](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/packaging_and_distributing_software/index#building-binary-rpms_building-rpms)
but in a nutshell it's this (for RHEL 8+) ...

```
sudo subscription-manager repos \
    --enable=rhel-8-for-x86_64-baseos-rpms \
    --enable=rhel-8-for-x86_64-appstream-rpms \
    --enable=codeready-builder-for-rhel-8-x86_64-rpms

sudo yum -y install git rpmdevtools yum-utils \
    https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

cd
rpmdev-setuptree

git clone https://github.com/ajacocks/qemu.git
cp qemu/qemu-full.spec rpmbuild/SPECS/

cd ~/rpmbuild/SPECS/
spectool -g -R qemu-full.spec

sudo dnf builddep qemu-full.spec
rpmbuild -bb qemu-full.spec
```

The built RPM is located here:

````
~/rpmbuild/RPMS/x86_64/qemu-full-5.2.0-1.el8.x86_64.rpm
````

