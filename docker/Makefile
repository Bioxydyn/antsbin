NAME        := 'bioxydyn/antsbin'
DOCKER_USER := 'bioxydyn'
TAG    := $$(git describe --always)
IMG    := ${NAME}:${TAG}
LATEST := ${NAME}:latest

build:
	@docker build -t ${IMG} .
	@docker tag ${IMG} ${LATEST}
