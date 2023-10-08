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
```
ame:                   web-serve-dev
Namespace:              dev
CreationTimestamp:      Sun, 08 Oct 2023 22:12:08 +0530
Labels:                 app=web-serve-dev
                        app.kubernetes.io/managed-by=Helm
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: gpt-server-dev
                        meta.helm.sh/release-namespace: default
Selector:               app=web-serve-dev
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=web-serve-dev
  Containers:
   web-serve-dev:
    Image:      default/emlo-web-server:assignment17-v1
    Port:       80/TCP
    Host Port:  0/TCP
    Limits:
      cpu:     500m
      memory:  200Mi
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config-v1.0'>          Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config-v1.0'>              Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret-v1.0'>           Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-config-v1.0'>  Optional: false
    Mounts:              <none>
  Volumes:               <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   web-serve-dev-7df744b96d (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  10m   deployment-controller  Scaled up replica set web-serve-dev-7df744b96d to 1
```
### 3. kubectl describe deployment 
```
Name:                   redis-db-dev
Namespace:              dev
CreationTimestamp:      Sun, 08 Oct 2023 22:12:08 +0530
Labels:                 app.kubernetes.io/managed-by=Helm
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: gpt-server-dev
                        meta.helm.sh/release-namespace: default
Selector:               app=redis-db-dev,role=master
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=redis-db-dev
           role=master
  Containers:
   redis-master:
    Image:      redis:7.2.1
    Port:       6379/TCP
    Host Port:  0/TCP
    Command:
      redis-server
    Args:
      --requirepass
      $(REDIS_PASSWORD)
    Limits:
      cpu:     200m
      memory:  200Mi
    Environment:
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1.0'>  Optional: false
    Mounts:            <none>
  Volumes:
   redis-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  redis-pvc
    ReadOnly:   false
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   redis-db-dev-6467998c4d (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  12m   deployment-controller  Scaled up replica set redis-db-dev-6467998c4d to 1
```
#### 4. kubectl describe pod model-serve-dev-78cbc74cbd-bwmx5 -n dev
```ame:             model-serve-dev-78cbc74cbd-bwmx5
Namespace:        dev
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 08 Oct 2023 22:12:08 +0530
Labels:           app=model-serve-dev
                  pod-template-hash=78cbc74cbd
Annotations:      <none>
Status:           Running
IP:               10.244.0.96
IPs:
  IP:           10.244.0.96
Controlled By:  ReplicaSet/model-serve-dev-78cbc74cbd
Containers:
  model-serve-dev:
    Container ID:   docker://12579e6a7511cc9ad1c1e55e7c4ce0dacd5e3f97ebb9b390937f7950d86f0b3c
    Image:          default/emlo-model-server:assignment17-v1
    Image ID:       docker://sha256:f05fc18f92e925e67ed7ca904a464491992b9a972dcc8fc14d9835e763d579c3
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 08 Oct 2023 22:12:10 +0530
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  1000Mi
    Requests:
      cpu:     500m
      memory:  1000Mi
    Environment:
      REDIS_HOST:       <set to the key 'hostname' of config map 'redis-config-v1.0'>         Optional: false
      REDIS_PORT:       <set to the key 'port' of config map 'redis-config-v1.0'>             Optional: false
      REDIS_PASSWORD:   <set to the key 'db_password' in secret 'redis-secret-v1.0'>          Optional: false
      GPT_MODEL:        <set to the key 'gpt_model' of config map 'model-config-v1.0'>        Optional: false
      TOKENIZER_MODEL:  <set to the key 'tokenizer_model' of config map 'model-config-v1.0'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6tbhn (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-6tbhn:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  3m45s  default-scheduler  Successfully assigned dev/model-serve-dev-78cbc74cbd-bwmx5 to minikube
  Normal  Pulled     3m43s  kubelet            Container image "default/emlo-model-server:assignment17-v1" already present on machine
  Normal  Created    3m43s  kubelet            Created container model-serve-dev
  Normal  Started    3m43s  kubelet            Started container model-serve-dev
```
#### 5. kubectl describe pod redis-db-dev-6467998c4d-pl54t -n dev
```
Name:             redis-db-dev-6467998c4d-pl54t
Namespace:        dev
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 08 Oct 2023 22:12:26 +0530
Labels:           app=redis-db-dev
                  pod-template-hash=6467998c4d
                  role=master
Annotations:      <none>
Status:           Running
IP:               10.244.0.97
IPs:
  IP:           10.244.0.97
Controlled By:  ReplicaSet/redis-db-dev-6467998c4d
Containers:
  redis-master:
    Container ID:  docker://daaf66be763f2dcb591adfe54190bc92cc687266e2c85e82f383b45d9ade0bf2
    Image:         redis:7.2.1
    Image ID:      docker://sha256:da63666bbe9aec9bd719f3f54c70bbda8c34d059385c4102a37c30d2fa0d7daa
    Port:          6379/TCP
    Host Port:     0/TCP
    Command:
      redis-server
    Args:
      --requirepass
      $(REDIS_PASSWORD)
    State:          Running
      Started:      Sun, 08 Oct 2023 22:12:28 +0530
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     200m
      memory:  200Mi
    Requests:
      cpu:     200m
      memory:  200Mi
    Environment:
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1.0'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xdj47 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  redis-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  redis-pvc
    ReadOnly:   false
  kube-api-access-xdj47:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason            Age                    From               Message
  ----     ------            ----                   ----               -------
  Warning  FailedScheduling  6m10s (x2 over 6m13s)  default-scheduler  0/1 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod..
  
  Normal   Scheduled         5m55s                  default-scheduler  Successfully assigned dev/redis-db-dev-6467998c4d-pl54t to minikube
  Normal   Pulled            5m54s                  kubelet            Container image "redis:7.2.1" already present on machine
  Normal   Created           5m54s                  kubelet            Created container redis-master
  Normal   Started           5m53s                  kubelet            Started container redis-master
```
#### 6. kubectl describe pod web-serve-dev-7df744b96d-vj6rd -n dev
```
ame:             web-serve-dev-7df744b96d-vj6rd
Namespace:        dev
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 08 Oct 2023 22:12:09 +0530
Labels:           app=web-serve-dev
                  pod-template-hash=7df744b96d
Annotations:      <none>
Status:           Running
IP:               10.244.0.94
IPs:
  IP:           10.244.0.94
Controlled By:  ReplicaSet/web-serve-dev-7df744b96d
Containers:
  web-serve-dev:
    Container ID:   docker://735a467870c31cbf34c7d904ed0815038ec008bcf69e1e37ec0cad559656682b
    Image:          default/emlo-web-server:assignment17-v1
    Image ID:       docker://sha256:9005ee64daffcb4ae13cf9a5e6d6194cb855e29e9c36043f9cca26dca1327a14
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 08 Oct 2023 22:12:11 +0530
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  200Mi
    Requests:
      cpu:     500m
      memory:  200Mi
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config-v1.0'>          Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config-v1.0'>              Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret-v1.0'>           Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-config-v1.0'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-nwrl9 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-nwrl9:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  10m    default-scheduler  Successfully assigned dev/web-serve-dev-7df744b96d-vj6rd to minikube
  Normal  Pulled     10m    kubelet            Container image "default/emlo-web-server:assignment17-v1" already present on machine
  Normal  Created    10m    kubelet            Created container web-serve-dev
  Normal  Started    9m59s  kubelet            Started container web-serve-dev
```
#### 7. kubectl describe ingress web-serve-dev -n dev
```
Name:             web-serve-dev
Labels:           app.kubernetes.io/managed-by=Helm
Namespace:        dev
Address:          192.168.49.2
Ingress Class:    nginx
Default backend:  <default>
Rules:
  Host            Path  Backends
  ----            ----  --------
  mykube-app.com  
                  /   web-serve-dev:8000 (10.244.0.94:80)
Annotations:      meta.helm.sh/release-name: gpt-server-dev
                  meta.helm.sh/release-namespace: default
Events:
  Type    Reason  Age                From                      Message
  ----    ------  ----               ----                      -------
  Normal  Sync    13m (x2 over 14m)  nginx-ingress-controller  Scheduled for sync
```
#### 8. kubectl top pod -n dev
```
NAME                               CPU(cores)   MEMORY(bytes)   
model-serve-dev-78cbc74cbd-bwmx5   172m         259Mi           
model-serve-dev-78cbc74cbd-l2swm   164m         277Mi           
redis-db-dev-6467998c4d-pl54t      3m           9Mi             
web-serve-dev-7df744b96d-vj6rd     3m           50Mi      
```
#### 9. kubectl top node
```
NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
minikube   619m         15%    1777Mi          22% 
```

#### 10. kubectl get all -A -o yaml
```
tems:
- apiVersion: v1
  kind: Pod
  metadata:
    creationTimestamp: "2023-10-08T16:42:08Z"
    generateName: model-serve-dev-78cbc74cbd-
    labels:
      app: model-serve-dev
      pod-template-hash: 78cbc74cbd
    name: model-serve-dev-78cbc74cbd-bwmx5
    namespace: dev
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: model-serve-dev-78cbc74cbd
      uid: 13d7a3d2-e19a-47dd-84c1-ada28787b526
    resourceVersion: "15157"
    uid: 859bed98-7921-4b33-a980-8ecddc6ba2a6
  spec:
    containers:
    - env:
      - name: REDIS_HOST
        valueFrom:
          configMapKeyRef:
            key: hostname
            name: redis-config-v1.0
      - name: REDIS_PORT
        valueFrom:
          configMapKeyRef:
            key: port
            name: redis-config-v1.0
      - name: REDIS_PASSWORD
        valueFrom:
          secretKeyRef:
            key: db_password
            name: redis-secret-v1.0
      - name: GPT_MODEL
        valueFrom:
          configMapKeyRef:
            key: gpt_model
            name: model-config-v1.0
      - name: TOKENIZER_MODEL
        valueFrom:
          configMapKeyRef:
            key: tokenizer_model
            name: model-config-v1.0
      image: default/emlo-model-server:assignment17-v1
      imagePullPolicy: Never
      name: model-serve-dev
      ports:
      - containerPort: 80
        protocol: TCP
      resources:
        limits:
          cpu: 500m
          memory: 1000Mi
....
....
- apiVersion: batch/v1
  kind: Job
  metadata:
    annotations:
      batch.kubernetes.io/job-tracking: ""
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"batch/v1","kind":"Job","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-patch","namespace":"ingress-nginx"},"spec":{"template":{"metadata":{"labels":{"app.kubernetes.io/component":"admission-webhook","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx"},"name":"ingress-nginx-admission-patch"},"spec":{"containers":[{"args":["patch","--webhook-name=ingress-nginx-admission","--namespace=$(POD_NAMESPACE)","--patch-mutating=false","--secret-name=ingress-nginx-admission","--patch-failure-policy=Fail"],"env":[{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}],"image":"registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b","imagePullPolicy":"IfNotPresent","name":"patch","securityContext":{"allowPrivilegeEscalation":false}}],"nodeSelector":{"kubernetes.io/os":"linux","minikube.k8s.io/primary":"true"},"restartPolicy":"OnFailure","securityContext":{"runAsNonRoot":true,"runAsUser":2000},"serviceAccountName":"ingress-nginx-admission"}}}}
    creationTimestamp: "2023-10-07T20:23:24Z"
    generation: 1
    labels:
      app.kubernetes.io/component: admission-webhook
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
    name: ingress-nginx-admission-patch
    namespace: ingress-nginx
    resourceVersion: "465"
    uid: 1654dee3-53b7-4be4-8548-6a4cfea73a52
  spec:
    backoffLimit: 6
    completionMode: NonIndexed
    completions: 1
    parallelism: 1
    selector:
      matchLabels:
        batch.kubernetes.io/controller-uid: 1654dee3-53b7-4be4-8548-6a4cfea73a52
    suspend: false
    template:
      metadata:
        creationTimestamp: null
        labels:
          app.kubernetes.io/component: admission-webhook
          app.kubernetes.io/instance: ingress-nginx
          app.kubernetes.io/name: ingress-nginx
          batch.kubernetes.io/controller-uid: 1654dee3-53b7-4be4-8548-6a4cfea73a52
          batch.kubernetes.io/job-name: ingress-nginx-admission-patch
          controller-uid: 1654dee3-53b7-4be4-8548-6a4cfea73a52
          job-name: ingress-nginx-admission-patch
        name: ingress-nginx-admission-patch
      spec:
        containers:
        - args:
          - patch
          - --webhook-name=ingress-nginx-admission
          - --namespace=$(POD_NAMESPACE)
          - --patch-mutating=false
          - --secret-name=ingress-nginx-admission
          - --patch-failure-policy=Fail
          env:
          - name: POD_NAMESPACE
            valueFrom:
              fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
          image: registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20230407@sha256:543c40fd093964bc9ab509d3e791f9989963021f1e9e4c9c7b6700b02bfb227b
          imagePullPolicy: IfNotPresent
          name: patch
          resources: {}
          securityContext:
            allowPrivilegeEscalation: false
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
        dnsPolicy: ClusterFirst
        nodeSelector:
          kubernetes.io/os: linux
          minikube.k8s.io/primary: "true"
        restartPolicy: OnFailure
        schedulerName: default-scheduler
        securityContext:
          runAsNonRoot: true
          runAsUser: 2000
        serviceAccount: ingress-nginx-admission
        serviceAccountName: ingress-nginx-admission
        terminationGracePeriodSeconds: 30
  status:
    completionTime: "2023-10-07T20:23:44Z"
    conditions:
    - lastProbeTime: "2023-10-07T20:23:44Z"
      lastTransitionTime: "2023-10-07T20:23:44Z"
      status: "True"
      type: Complete
    ready: 0
    startTime: "2023-10-07T20:23:32Z"
    succeeded: 1
    uncountedTerminatedPods: {}
kind: List
metadata:
  resourceVersion: ""
devesh@devesh-virtual-m
```