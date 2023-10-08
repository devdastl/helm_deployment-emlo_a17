# helm_deployment-emlo_a17
This project focuses on deploying three services to perform GPT2 based inference. This project is a part of assignment from EMLO.

## Introduction
This project uses Helm to deploy three services:
- FastAPI based web service
- GPT2 inference server
- Redis DataBase for caching

We will use two different namespace for two isolated deployment. This project uses Makefile to further simlipy imlementation.
## Deployment overview
First lets go through the overview and flow of deployment. Below is the flow diagram representing our target deployment workflow:
<img src="deploy_wf.png" alt= “” width="" height="">
<br>

Lets go through few important points:
- We are using single Node based deployemnt using minikube.
- We have two isolated and identical deployments on two different namespace `dev` & `pro`
- We have two different ingress and persistant volume as they can't be isolated via namespace.
- We have `web-server`, `gpt-inference-server` and `redis database.`
    - web-server has single pod replica
    - gpt-inference-server has two replica of pod 
    - single pod for redis database.

## Way to deploy & dependency

### Testing deployment via docker-compose

### Deployment via minikube kubectl

### Deployment via Helm 

### Output