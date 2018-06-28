# Ansible Runner

A wrapper that runs ansible in a docker container to eliminate python dependency hell, bundles the dependencies needed for the following modules:

* aws
* azure
* vmware
* bigip
* panos
* win

### ansible-run
```bash
pip install ansible-run
ansible-run
# drop into a shell with ansible and friends pre-installed
```

**Environment Variables:**
* `AWS_*` environment variables

**Volumes:**
* `/ssh` (for use with [whilp/ssh-agent](https://github.com/whilp/ssh-agent))
* `/var/run/docker.sock` (so that docker can talk to itself)
* `~/.aws`
* `~/.ansible`
* `/work`
* `$PWD`

### ansible-role
```bash
ansible-role moshloop.java # cross-platform install of java
```

### ansible-test

`ansible-test` will test a playbook using a docker container:

```bash
ansible-test playbook.yml # defaults to centos7
image=ubuntu1804 ansible-test playbook.yml
```

The playbook will be tested for idempotency by running it a 2nd time and ensuring nothing is marked as changed, disable it with:
```bash
idempotency=false ansible-test playbook.yml
```

Once the playbook is run any [InSpec](https://www.inspec.io) (.rb) or [bats](https://github.com/sstephenson/bats) (.bats) tests found with the same name (e.g. `playbook.rb`) will be executed.

See it in action [here](https://github.com/moshloop/ansible-java/tree/master/tests)
