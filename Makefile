PHONY: all
all: dr-up dr-up-b dr-build dr-clean

HELM_TEMPLATES_DIR ?= helm/templates

dr-up:
	docker compose up

dr-up-b:
	make dr-build
	make dr-up

dr-build:
	docker compose build

dr-clean:
	docker compose stop
	docker compose rm

compose-convert:
	kompose convert -o ${HELM_TEMPLATES_DIR}

kube-apply:
	cd ${HELM_TEMPLATES_DIR} \
	&& kubectl apply -R -f .
