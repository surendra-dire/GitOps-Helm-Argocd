# ArgoCD Setup #

# Step - 1 : Helm ArgoCD Instllation #

**Step 1**: Add the ArgoCD Helm Repository
helm repo add argo https://argoproj.github.io/argo-helm  
helm repo update  

**Step2**: Create a Namespace for ArgoCD  
kubectl create namespace argocd  

**Step 3**: Install ArgoCD Using Helm  
helm install argocd argo/argo-cd --namespace argocd  

**Step 4**: Verify the Installation
kubectl get pods -n argocd

**Step 5**: Expose the ArgoCD Server
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'    

Note: In Minikube, LoadBalancer will not return a real external IP unless you use a tunnel (minikube tunnel) or port forwarding (preferred for quick access).  

kubectl get svc -n argocd argocd-server    

Access the application:
http://external-ip

**Port-Forwarding (Temporary Local Access) - In case of minikube**  
kubectl port-forward svc/argocd-server -n argocd 8080:443  
https://localhost:8080  

**Login to ArgoCD: Retrieve the Initial Admin Password:**    

kubectl get secret -n argocd argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d  [linux]    
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($_)) } [windows -minikube]    
Username- admin    
Pasword-     

**Enable the Ingress controller, in case of minikube, it deploys NGINX Ingress Controller in the ingress-nginx namespace** 
minikube addons enable ingress  

# Step - 2 : Configure ArgoCD from CLI #



