$ kubectl autoscale deploy web --min=1 --max=3 --cpu-percent=5


To see the autoscale setup run following command:
$ kubectl get hpa


Check metrics >
$ kubectl top pod <<pod name>>

Hit URL in loop
$ while true; do curl http://192.168.99.100:30588; done

Scale up when load increase. Scale down when decrease.

Uses metrics server.
 
