```bash
pip install ansible-run
ansible-run
# drop into a shell with ansible and friends pre-installed
```

### Environment Variable

* `AWS_*`
* `ANSIBLE_*`

### Volumes
* `/ssh` (for use with [whilp/ssh-agent](https://github.com/whilp/ssh-agent))
* `/var/run/docker.sock` (so that docker can talk to itself)
* `~/.aws`
* `~/.ansible`
* `/work`
* `$PWD`