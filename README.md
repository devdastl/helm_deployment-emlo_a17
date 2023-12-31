# Helm based deployment (EMLO assignment 17)
This project focuses on deploying three services to perform GPT2 based inference. This project is a part of assignment from EMLO.

## Introduction
This project uses Helm to deploy three services:
- FastAPI based web service
- GPT2 inference server
- Redis DataBase for caching

We will use two different namespace for two isolated deployment. This project uses Makefile to further simlipy imlementation.
## Deployment overview
First lets go through the overview and flow of deployment. Below is the flow diagram representing our target deployment workflow:
<img src="img/deploy_wf.png" alt= “” width="" height="">
<br>

Lets go through few important points:
- We are using single Node based deployemnt using minikube.
- We have two isolated and identical deployments on two different namespace `dev` & `pro`
- We have two different ingress and persistant volume as they can't be isolated via namespace.
- We have `web-server`, `gpt-inference-server` and `redis database.`
    - web-server has single pod replica
    - gpt-inference-server has two replica of pod 
    - single pod for redis database.

## Prerequisite
Below are few required Prerequisite to deploy this project:
- Minikube installed
- Docker and docker-compose
- Helm installed
- `make` to build project via Makefile

## Way to deploy & dependency
This project can be deployed in three different ways. We will go throught steps for each. this three different ways are:
- docker-compose: basic deployment to test correct working of required services.
- minikube-kubectl: kubectl based deploynment on default namespace.
- Helm: complex deployment using two namespaces, configs and helm values.

### 1. Testing deployment via docker-compose
Lets go through the first way of deployment by simply using docker compose, below are the steps:
1. Build docker images for the web and inference service. Run command `make build-images`. (Source code for the service in is `src/web-server-gpt` & `src/model-server-gpt`).
2. Start the services via docker compose. Run command `make test-dockercompose`. This will start all three services.
3. Open url `http://localhost:8050/docs` to access web-server api page. 
4. Add your text in the field and test the results.

Thats all! Now you can confirm that services and images are working as aspected.

### 2. Deployment via minikube kubectl
Now lets go throught kubectl based deployment on single default namespace.
1. First start minikube and enable necessary plugins like ingress. Run command `make start-minikube`. This will start minikube and enable addons.
2. Push built images to minikube registory. Run command `make push-to-minikube`
3. Now to start kubectl based deployment run following command `make kubectl-deployment`. This will take YAML files from `minikube_k8s_deployment/` and will start a deployment.
4. Check if all the pods are up and running, run this `minikube kubectl -- get pods`
5. Now access the ingress to run the inferernce:
    - if you are on Ubuntu then add output of `minikube ip` in `/etc/hosts` with domain `mykube-app.com`. Ex add `198.146.12.2    mykube-app.com`.
    - if you are on MAC then do the above and start minikube tunnel. `minikube tunnel`
6. Once you are able to access same api page on `mykube-app.com`. You can kill and remove this deployment. Run this command to easily remove it `make kill-kubectl-deployment`. It will run series of commands to remove all resources.

NOTE: Model-server pods can take some time to start as it will download the selected model.

### 3. Deployment via Helm 
Now lets go through Helm deployment on two different namespace i.e. dev and prod. Again we will be using make command to make the deployment easier.
1. Create two namespace dev and prod. Run `make create-namespace`. This will create two namespaces.
2. Now create the helm deployment from `helm_gpt_deployment/` directory. Run command `make create-helm-deployment`. This will create two deployments, one on dev and one on prod. Go through Makfile to know more on the commmands.
3. Now check `mykube-app.com/docs` and run inference. You have to follow step-5 of kubectl deployment to add another domain name `mykube-app-prod.com` so that you can access prod deployment as well.
4. Once done, you can kill the deployment by running `make kill-helm-deployment`.

### Inference output
Lest see how to use `mykube-app.com/docs` api page to perform inference.
1. Access the API page `http://mykube-app.com/docs`. You will see below page.
<img src="img/step-1.PNG" alt= “” width="" height="">
2. Try out first post api and add your text as shown below.
<img src="img/step-2.PNG" alt= “” width="" height="">
3. Execute and see the output text.
<img src="img/step-3.PNG" alt= “” width="" height="">
4. You can try it with same input and inference will be much faster as the data is been cached for faster inferece.
