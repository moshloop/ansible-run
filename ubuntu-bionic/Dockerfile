FROM ubuntu:bionic
ENV ANSIBLE_CONFIG /etc/ansible/ansible.cfg
ENV DEBIAN_FRONTEND=noninteractive
ADD ansible.cfg /etc/ansible/ansible.cfg
RUN apt-get update && \
    apt-get install -y python-setuptools python-pip python-dev build-essential jq libkrb5-dev krb5-user wget openssh-client && \
    wget -O /usr/bin/fireviz https://github.com/moshloop/fireviz/releases/download/0.1/fireviz  && \
    wget -O /usr/bin/kops https://github.com/kubernetes/kops/releases/download/1.9.1/kops-linux-amd64 && \
    # wget -O /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/1.10/bin/linux/amd64/kubectl && \
    chmod +x /usr/bin/* && \
    pip install ansible awscli aws-sudo s3cmd boto pandevice f5-sdk pywinrm[kerberos] pywinrm[credssp]


ENTRYPOINT bash