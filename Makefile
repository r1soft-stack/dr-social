:PHONY all

dr-setup:
	

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