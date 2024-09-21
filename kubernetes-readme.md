getting current context

```bash
  kubectl config current-context
```

```bash
  kubectl create deployment mynginx1 --image=nginx
```

```bash
 kubectl delete deploy mynginx1
```

## for getting pods

```bash
 kubectl get pods
 kubectl get pods -o wide
 kubectl get pods -n kube-public
```

## for create starting pods from a yaml

```bash
kubectl create -f myapp.yaml

```

```bash
kubectl describe pod myapp-pod
```

## basically ssh to the pod

```bash
kubectl exec -it myapp-pod -- bash
```

# for myapp-1.yaml

```bash
kubectl exec -it init-demo -- /bin/bash
curl localhost
```

## delete the pod

```bash
kubectl delete -f myapp.yaml
```

## this was a lesson for myapp-2 learned about port forwading in kubernetes and also selectors

```bash
 kubectl get po -o wide
 kubectl get ep myservice

 kubectl port-forward service/myservice 8080:80
```
