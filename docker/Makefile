NAME        := 'bioxydyn/antsbin'
DOCKER_USER := 'bioxydyn'
TAG    := $$(git describe --always)
IMG    := ${NAME}:${TAG}
LATEST := ${NAME}:latest

build:
	@docker build -t ${IMG} .
	@docker tag ${IMG} ${LATEST}
	rm -rf /tmp/antsbin
	mkdir /tmp/antsbin
	docker run -it -v /tmp/antsbin/:/mnt/data bioxydyn/antsbin:latest sh -c "cp /temp/antsbin/dist/* /mnt/data/"
	cp /tmp/antsbin/* .
	# results are now in cwd
	# if on aws you could copy with something like  scp -i dev-keys.pem ubuntu@123.456.123.2:/home/ubuntu/antsbin/docker/antsbin-0.1.1-cp36-cp36m-linux_x86_64.whl .
