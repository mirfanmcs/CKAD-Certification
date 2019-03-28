Run NFS server in docker container. In prod it will be dedicated NFS server. 
The NFS server exposes two directories, data-0001 and data-0002. In the next steps, this is used to store data.

docker run -d --net=host \
   --privileged --name nfs-server \
   katacoda/contained-nfs-server:centos7 \
   /exports/data-0001 /exports/data-0002


Create Persistent Volumes:
kubectl create -f pv.yaml


View the contents of the files using cat pv.yaml

Once created, view all PersistentVolumes in the cluster using kubectl get pv


Create claims. 

kubectl create -f pvc.yaml

View the contents of the files using cat pvc.yaml 

Once created, view all PersistentVolumesClaims in the cluster using kubectl get pvc.


Launch pod.

kubectl create -f pod.yaml


Use the command below to view the definition of the Pods.

cat pod.yaml 

You can see the status of the Pods starting using kubectl get pods

If a Persistent Volume Claim is not assigned to a Persistent Volume, then the Pod will be in Pending mode until it becomes available. In the next step, we'll read/write data to the volume.


To test the HTTP server, write a 'Hello World' index.html homepage. In this scenario, we know the HTTP directory will be based on data-0001.

docker exec -it nfs-server bash -c "echo 'Hello World' > /exports/data-0001/index.html"

Based on the IP of the Pod, when accessing the Pod, it should return the expected response.

ip=$(kubectl get pod www -o yaml |grep podIP | awk '{split($0,a,":"); print a[2]}'); echo $ip

curl $ip

Update Data
When the data on the NFS share changes, then the Pod will read the newly updated data.

docker exec -it nfs-server bash -c "echo 'Hello NFS World' > /exports/data-0001/index.html"

curl $ip

        127.0.0.1

	inet 192.168.1.7 netmask 0xffffff00 broadcast 192.168.1.255
	inet 192.168.99.1 netmask 0xffffff00 broadcast 192.168.99.255
