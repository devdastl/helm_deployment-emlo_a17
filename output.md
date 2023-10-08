#### 1. kubectl describe deployment model-serve-dev -n dev
```
Name:                   model-serve-dev
Namespace:              dev
CreationTimestamp:      Sun, 08 Oct 2023 17:40:47 +0530
Labels:                 app.kubernetes.io/managed-by=Helm
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: gpt-server-dev
                        meta.helm.sh/release-namespace: default
Selector:               app=model-serve-dev
Replicas:               2 desired | 2 updated | 2 total | 2 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=model-serve-dev
  Containers:
   model-serve-dev:
    Image:      default/emlo-model-server:assignment17-v1
    Port:       80/TCP
    Host Port:  0/TCP
    Limits:
      cpu:     500m
      memory:  1000Mi
    Environment:
      REDIS_HOST:       <set to the key 'hostname' of config map 'redis-config-v1.0'>         Optional: false
      REDIS_PORT:       <set to the key 'port' of config map 'redis-config-v1.0'>             Optional: false
      REDIS_PASSWORD:   <set to the key 'db_password' in secret 'redis-secret-v1.0'>          Optional: false
      GPT_MODEL:        <set to the key 'gpt_model' of config map 'model-config-v1.0'>        Optional: false
      TOKENIZER_MODEL:  <set to the key 'tokenizer_model' of config map 'model-config-v1.0'>  Optional: false
    Mounts:             <none>
  Volumes:              <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   model-serve-dev-78cbc74cbd (2/2 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  3m47s  deployment-controller  Scaled up replica set model-serve-dev-78cbc74cbd to 2
```

#### 2. kubectl describe deployment web-serve-dev -n dev