tag := $(shell git tag --points-at HEAD )
ifdef tag
else
  tag := $(shell git describe --abbrev=0 --tags)-debug
endif

.DEFAULT_GOAL := push
ANSIBLE_VERSION := 2.6.5
SYSTOOLS_VERSION := 3.1
IMAGE := moshloop/ansible-run
BASE := ubuntu:18.04

.PHONY: push
push: build
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASS)
	docker tag $(IMAGE) $(IMAGE):$(tag)
	docker push $(IMAGE):$(tag)
	docker tag $(IMAGE) $(IMAGE):latest
	docker push $(IMAGE):latest

.PHONY: build
build:
	$(shell cat Dockerfile.template | sed 's/%FROM%/$(BASE)/' > Dockerfile)
	 docker build ./ -t $(IMAGE) --build-arg ANSIBLE_VERSION=$(ANSIBLE_VERSION) --build-arg SYSTOOLS_VERSION=$(SYSTOOLS_VERSION)  --build-arg PACKAGES="$(shell cat ubuntu-packages.txt | tr '\r\n' ' ')"

.PHONY: all
all: *
	make BASE=ubuntu:16.04 IMAGE=moshloop/docker-ubuntu1604-ansible
	make BASE=ubuntu:18.04 IMAGE=moshloop/docker-ubuntu1604-ansible
	make BASE=debian:stretch IMAGE=moshloop/docker-debian-ansible