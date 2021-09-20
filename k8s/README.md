# Kubernetes
## Installations
[Minikube](https://minikube.sigs.k8s.io/) and [Kubernetes]( https://kubernetes.io/)  was installed for this lab using homebrew.
## Tasks
1. Deploy your application in the Kubernetes. Use the kubectl create command to create a Deployment:
    ![](images/kubectl-deploy.png)


2. Make your application accessible from outside the Kubernetes virtual network. Create a Service for it:
    ![](images/kubectl-service.png)
    ![](images/kubectl-running1.png)
    ![](images/kubectl-running.png)


3. Provide the output of `kubectl get pods,svc` command:
    ![](images/kubectl-svc.png)


4. Clean up. Remove deployment and service that you created: 
    ```bash
    kubectl delete deployment,svc currentmoscowtime
    ```
5. Use configuration files to deploy your
application. Create a deployment.yml manifest for it. Set up at least 3 replicas:
    ```bash
    kubectl apply -f deployment.yaml 
    ```
6. Create a service.yml manifest for your app: 
    ```bash
    kubectl apply -f service.yaml 
    ```
7. Provide the output of `kubectl get pods,svc` command:
    ![](images/kubectl-config.png)


8. Clean up. Remove deployment and service that you created: 
    ```bash
    kubectl delete deployment,svc currentmoscowtime
    ```
