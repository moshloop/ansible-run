FROM centos:centos7.3.1611
ARG ANSIBLE_VERSION=2.4.4.0
RUN rpm -i https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum install -y  net-tools nano git unzip zip tar gzip bzip2 psmisc bash lsof wget expect tree dos2unix xmlstarlet ruby psutils ruby-devel bats initscripts redhat-lsb-core gcc gcc-c++ python-pip nmap-ncat openssl jq sshpass openssh-client which  krb5-libs krb5-devel python-devel

RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install ansible==$ANSIBLE_VERSION awscli botocore crudini certifi aws-sudo s3cmd boto pandevice f5-sdk pywinrm[kerberos] pywinrm[credssp] certifi urllib3==1.22 jmespath
RUN rpm -i https://packages.chef.io/files/stable/inspec/2.2.16/el/7/inspec-2.2.16-1.el7.x86_64.rpm

RUN wget -q -O /usr/bin/gosu https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 && \
    ln -s /usr/bin/gosu /usr/bin/sudo && \
    wget -q -O /usr/bin/waiter https://github.com/moshloop/waiter/releases/download/1.1/waiter && \
    wget -q -O /usr/bin/docker https://master.dockerproject.org/linux/x86_64/docker && \
    chmod +x /usr/bin/*

ENV container=docker
ADD entrypoint.sh /etc/entrypoint.sh
ADD hosts /etc/ansible/hosts

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN systemctl mask dev-mqueue.mount dev-hugepages.mount \
    systemd-remount-fs.service sys-kernel-config.mount \
    sys-kernel-debug.mount sys-fs-fuse-connections.mount \
    display-manager.service graphical.target systemd-logind.service \
    network network-online

VOLUME /run /tmp
ADD dbus.service /etc/systemd/system/dbus.service
RUN systemctl enable dbus.service

RUN localedef -i en_US -f UTF-8 en_US.UTF-8

CMD /lib/systemd/systemd --system
