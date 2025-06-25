# Helm-Argocd

**ArgoCD Instllation:**

Step 1: Add the ArgoCD Helm Repository
helm repo add argo https://argoproj.github.io/argo-helm  
helm repo update  

Step2: Create a Namespace for ArgoCD  
kubectl create namespace argocd  

Step 3: Install ArgoCD Using Helm  
helm install argocd argo/argo-cd --namespace argocd  

Step 4: Verify the Installation
kubectl get pods -n argocd

Step 5: Expose the ArgoCD Server
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'  

Note: In Minikube, LoadBalancer will not return a real external IP unless you use a tunnel (minikube tunnel) or port forwarding (preferred for quick access).

kubectl get svc -n argocd argocd-server  

Access the application : 
Visit https://<EXTERNAL-IP> 

Port-Forwarding (Temporary Local Access) - In case of minikube
kubectl port-forward svc/argocd-server -n argocd 8080:443
https://localhost:8080

Login to ArgoCD: Retrieve the Initial Admin Password:  
kubectl get secret -n argocd argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d  [linux]
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($_)) } [windows -minikube]
Username- admin  
Pasword-   





kubectl port-forward svc/argocd-server -n argocd 8080:443
kubectl port-forward svc/petapp-service 8080:8080

minikube addons enable ingress

# Step - 1 : Create EKS Management Host in AWS #

1) Launch new Ubuntu VM using AWS Ec2 ( t2.micro )	  
2) Connect to machine and install kubectl using below commands  
```
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin
kubectl version --short --client
```
3) Install AWS CLI latest version using below commands 
```
sudo apt install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
