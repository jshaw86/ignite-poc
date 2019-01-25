# Steps

### Apply Kubernetes Resources

NOTE: assumes you have a kubernetes environment provisioned could be a minikube env

1. kubectl apply -f kubernetes-resources/ignite-rbac.yaml -n ignite
2. kubectl apply -f kubernetes-resources/ignite-service.yaml -n ignite
3. kubectl apply -f kubernetes-resources/ignite-deployment.yaml -n ignite

### Test REST API
1. `export IGNITE_EP=\`minikube service ignite -n ignite --url | head -n 1\``
2. `curl $IGNITE_EP/ignite\?cmd\=top`
{"name":"default","mode":"PARTITIONED","sqlSchema":null}],"order":2,"attributes":null,"tcpAddresses":["172.17.0.9","127.0.0.1"]}],"sessionToken":null}
3. `curl $IGNITE_EP/ignite\?cmd\=getorcreate\&cacheName\=test`
{"successStatus":0,"error":null,"response":null,"sessionToken":null}
4. `curl $IGNITE_EP/ignite\?cmd\=put\&key\=key\&val\=value\&cacheName\=test`
{"successStatus":0,"affinityNodeId":"fd33b3b0-1388-4b81-b972-39b55bd8f589","error":null,"response":true,"sessionToken":null}
5. `curl $IGNITE_EP/ignite\?cmd\=get\&key\=key\&cacheName\=test`
{"successStatus":0,"affinityNodeId":"fd33b3b0-1388-4b81-b972-39b55bd8f589","error":null,"sessionToken":null,"response":"value"}

### Test SQL

NOTE: pyignite requires python3 so make sure you have python3 virtualenv setup beforehand

1. `export IGNITE_SQL=\`minikube service ignite -n ignite --url | head -n 2 | tail -n 1\``
2. `pip install -r requirements.txt`
3. `python ignite-sql.py` 

### TODO

1. Figure out binary types in python: https://stackoverflow.com/questions/54340289/pyignite-serialize-and-de-serialize-complex-types
