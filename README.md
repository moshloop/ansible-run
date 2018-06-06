# Ansible Runner

A wrapper that runs ansible in a docker container to eliminate python dependency hell.

Supports:

* AWS
    - Any `AWS_*` environment variables will be passed through
    - `~/.aws` will be mounted
* Palo Alto
* WinRM (Kerberos + CredSSP)
* Fireviz
* Kops


### ssh-agent

Works well with [whilp/ssh-agent](https://github.com/whilp/ssh-agent) to keep allow ansible access to `ssh-agent`

```bash
docker run -u 1001 -d -v ssh:/ssh --name=ssh-agent whilp/ssh-agent:latest
docker run -u 1001 --rm -v ssh:/ssh -v $HOME:$HOME -it whilp/ssh-agent:latest ssh-add $HOME/.ssh/id_rsa
```