tag := $(shell git tag --points-at HEAD )
ifdef tag
else
  tag := $(shell git describe --abbrev=0 --tags)-debug
endif

.DEFAULT_GOAL := push
ANSIBLE_VERSION ?= 2.6.5
ANSIBLE_EXTRAS_VERSION ?= 1.2
ANSIBLE_DEPLOY_VERSION ?= 2.5.4
ANSIBLE_RUN_VERSION = ?= 3.3
ANSIBLE_VERSION ?= 2.6.5
SYSTOOLS_VERSION ?= 3.4
IMAGE ?= moshloop/ansible-run
BASE ?= ubuntu:18.04

.PHONY: push
push: *
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASS)
	docker tag $(IMAGE) $(IMAGE):$(tag)
	docker push $(IMAGE):$(tag)
	docker tag $(IMAGE) $(IMAGE):latest
	docker push $(IMAGE):latest

.PHONY: ubuntu
ubuntu: *
	$(shell cat Dockerfile.ubuntu | sed 's/%FROM%/$(BASE)/' > Dockerfile)
	 docker build ./ -t $(IMAGE) --build-arg ANSIBLE_VERSION=$(ANSIBLE_VERSION)  --build-arg ANSIBLE_RUN_VERSION=$(ANSIBLE_RUN_VERSION) --build-arg ANSIBLE_EXTRAS_VERSION=$(ANSIBLE_EXTRAS_VERSION) --build-arg ANSIBLE_DEPLOY_VERSION=$(ANSIBLE_DEPLOY_VERSION)  --build-arg SYSTOOLS_VERSION=$(SYSTOOLS_VERSION)  --build-arg PACKAGES="$(shell cat ubuntu-packages.txt | tr '\r\n' ' ')"
	 make push

PHONY: centos
centos: *
		$(shell cat Dockerfile.centos | sed 's/%FROM%/$(BASE)/' > Dockerfile)
	 docker build ./ -t $(IMAGE) --build-arg ANSIBLE_VERSION=$(ANSIBLE_VERSION) --build-arg ANSIBLE_RUN_VERSION=$(ANSIBLE_RUN_VERSION) --build-arg  ANSIBLE_EXTRAS_VERSION=$(ANSIBLE_EXTRAS_VERSION) --build-arg ANSIBLE_DEPLOY_VERSION=$(ANSIBLE_DEPLOY_VERSION)  --build-arg SYSTOOLS_VERSION=$(SYSTOOLS_VERSION)  --build-arg PACKAGES="$(shell cat centos-packages.txt | tr '\r\n' ' ')"
	 make push
