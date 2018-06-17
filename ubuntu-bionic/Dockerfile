FROM ubuntu:bionic
ENV ANSIBLE_CONFIG /etc/ansible/ansible.cfg
ARG ANSIBLE_VERSION=2.4.4
ENV DEBIAN_FRONTEND=noninteractive
ADD ansible.cfg /etc/ansible/ansible.cfg
RUN apt-get update && \
    apt-get install -y python-setuptools python-pip python-dev build-essential jq libkrb5-dev krb5-user wget openssh-client sshpass  && \
    pip install ansible==$ANSIBLE_VERSION awscli aws-sudo s3cmd boto pandevice f5-sdk pywinrm[kerberos] pywinrm[credssp] certifi urllib3==1.22 jmespath && \
    wget -O /usr/bin/docker https://master.dockerproject.org/linux/x86_64/docker && \
    chmod +x /usr/bin/*
    # wget -O /usr/bin/fireviz https://github.com/moshloop/fireviz/releases/download/0.1/fireviz  && \
    # wget -O /usr/bin/kops https://github.com/kubernetes/kops/releases/download/1.9.1/kops-linux-amd64 && \
    # wget -O /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/1.10/bin/linux/amd64/kubectl && \


ENTRYPOINT bash


