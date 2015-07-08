#### An Ambari Stack for Redis
Ambari stack for easily installing and managing Redis on HDP cluster


###Assumptions

- Ambari is installed and running. If not, you can use sandbox VM Image provided by [Hortonworks website](http://hortonworks.com/products/hortonworks-sandbox/)
- No previous installations of Redis exist. If there any, you can either remove it or rename it.

Follow given step to install and manage Redis using Ambari.

####Connect to the VM via SSH (password hadoop for sandbox image) and start Ambari server
```
ssh root@ambari.machine
```

####To deploy the Redis, run below
```
cd /var/lib/ambari-server/resources/stacks/HDP/2.2/services
git clone https://github.com/nikunjness/redis-ambari.git   
```

####Restart Ambari
#####on sandbox
```sudo service ambari restart```

#####on non-sandbox
```sudo service ambari-server restart```


####Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard:

On bottom left -> Actions -> Add service -> check Redis -> Next -> Next -> Next -> Deploy

![Image](../master/screenshots/addservice.png?raw=true)
![Image](../master/screenshots/assignmaster.png?raw=true)
![Image](../master/screenshots/customizeservice.png?raw=true)
![Image](../master/screenshots/install.png?raw=true)
![Image](../master/screenshots/installed.png?raw=true)
![Image](../master/screenshots/review.png?raw=true)
![Image](../master/screenshots/summary.png?raw=true)

####On successful deployment you will see the Redis as part of Ambari stack and will be able to start/stop the service from here:

![Image](../master/screenshots/redissummary.png?raw=true)
 
####You can see the parameters you configured under 'Configs' tab 
![Image](../master/screenshots/redisconfig.png?raw=true)

####Use Redis

- Check the contents of the redis log file we specified

```
# cat /var/log/redis.log
Starting redis: [  OK  ]
```

- Check status of Redis 
```
# service redis status
redis-server (pid  8175) is running...
``` 
- One benefit to wrapping the component in Ambari service is that you can now monitor/manage this service remotely via REST API

```
export SERVICE=REDIS
export PASSWORD=admin
export AMBARI_HOST="your_ambari_hostname"
export CLUSTER="your_ambari_cluster_name"

#get service status
curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X GET http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

#start service
curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Start $SERVICE via REST"}, "Body": {"ServiceInfo": {"state": "STARTED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

#stop service
curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Stop $SERVICE via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE
```

#### Remove Redis

- To remove the Redis: 
  - Stop the service via Ambari
  - Delete the service
  
    ```
    curl -u admin:admin -i -H 'X-Requested-By: ambari' -X DELETE http://replace_with_your_ambari_hostname.com:8080/api/v1/clusters/ambari_cluster_name/services/REDIS
    ```
  - Remove artifacts 
  
    ```
    rm -rf /var/lib/ambari-server/resources/stacks/HDP/2.2/services/redis-ambari
    ```
  - Restart Ambari
    ```
    service ambari restart
    ```
    
###References:
https://github.com/abajwa-hw/ntpd-stack


    