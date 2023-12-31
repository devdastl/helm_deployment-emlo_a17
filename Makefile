USERNAME = default
PROJECT = emlo
TAG = assignment17-v1

#setup make commands
help:
	@echo "Makefile supported commands:"
	@echo "build-image: Build image from Dockerfile"
	@echo "start-minikube: Run docker container in interactive mode"
	@echo "run-train: Run training on default config"

build-images:
	@echo "building docker image for web service"
	cd src/web-server-gpt && docker build -t ${USERNAME}/${PROJECT}-web-server:${TAG} .

	@echo "building docker image for gpt model service"
	cd src/model-server-gpt && docker build -t ${USERNAME}/${PROJECT}-model-server:${TAG} .


test-dockercompose:
	@echo "starting services with docker compose"
	@echo " service is will expose on localhost:8050 "
	docker compose -f test_docker_compose.yml up

start-minikube:
	@echo "starting minikube on docker"
	minikube start --driver=docker

	@echo "enabling required plugin for ingress"
	minikube addons enable ingress
	minikube addons enable ingress-dns


push-to-minikube:
	@echo "pushing web-server image to minikube"
	minikube image load ${USERNAME}/${PROJECT}-web-server:${TAG}

	@echo "pushing gpt-server image to minikube"
	minikube image load ${USERNAME}/${PROJECT}-model-server:${TAG}

	@echo "pushing redis-db image to minikube"
	minikube image load redis:7.2.1

create-kubectl-deployment:
	@echo "starting kubectl based deployment"
	minikube kubectl -- apply -f minikube_k8s_deployment/

kill-kubectl-deployment:
	@echo "Killing kubectl based deployment"
	minikube kubectl -- delete all --all
	minikube kubectl -- delete ingress web-server-ingress
	minikube kubectl -- delete pvc redis-pvc
	minikube kubectl -- delete pv redis-pv


create-namespace:
	@echo "creating namespace dev & prod"
	minikube kubectl -- create namespace dev
	minikube kubectl -- create namespace prod

create-helm-deployment:
	@echo "starting helm deployment in dev namspace"
	helm install gpt-server-dev helm_gpt_deployment/ \
	--values helm_gpt_deployment/values.yaml \
	-f helm_gpt_deployment/values-dev.yaml

	sleep 5s

	@echo "starting helm deployment in prod namspace"
	helm install gpt-server-prod helm_gpt_deployment/ \
	--values helm_gpt_deployment/values.yaml \
	-f helm_gpt_deployment/values-prod.yaml

kill-helm-deployment:
	@echo "kill and removing helm dev and pro deployment"
	helm uninstall gpt-server-dev gpt-server-prod



