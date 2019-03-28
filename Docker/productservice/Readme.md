product-service-docker
========================
This is the sample REST Spring boot microservice application to be deployed in Kubernetes minikube cluster.


To build the docker image run following command in the directory where Dockerfile is located:
`$ docker build -t productservice .`

To run the container locally run the following command:
`$ docker run -p 8080:8080 productservice`

To run the container with environment variables:
`$ docker run \
-e APPLICATION_NAME='my app' \
-e COMPANY_NAME='my company' \
-e COMPANY_ADDRESS='my company address' \
-e APPLICATION_SECRET_1='my app secret 1' \
-e APPLICATION_SECRET_2='my app secret 2' \
-p 8080:8080 productservice`


Tag the image using following command:
`$ docker tag productservice:latest mirfanmcs/productservice`

Push the image to docker hub:
`$ docker push mirfanmcs/productservice`

Run following command to create ConfigMap:
`$ kubectl create -f productservice-configMap.yml`

Run following command to see created ConfigMap:
`$ kubectl get configmaps product-service-config -o yaml`

Run following command to create Secret:
`$ kubectl create -f productservice-secret.yml`

Run following command to see created Secret:
`$ kubectl get secrets product-service-secret -o yaml`

Run following command to create Deployment:
`$ kubectl create -f productservice-deployment.yml`

Run following command to create Service:
`$ kubectl create -f productservice-service.yml`

Run the following command to run the service:
`$ minikube service productservicesrv`

OR get the VM IP using following command:
`$ minikube ip`

Run the following command to get service's exposed post:
`$ kubectl get service productservicesrv`

Enter the IP with the exposed port in the browser URL.
For example:
http://192.168.99.100:32568//api/product


Run the following command to scale the application (pods) to 4:
`$ kubectl scale deployment productserviceapp --replicas=4`

Run the following command to create all objects:
`$ kubectl apply -f productservice-all-deploy.yml`