# Helm-Argocd

ArgoCD Instllation
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
kubectl get svc -n argocd argocd-server
Visit https://<EXTERNAL-IP> 
 Port-Forwarding (Temporary Local Access)
kubectl port-forward svc/argocd-server -n argocd 8080:443

Login to ArgoCD:
Retrieve the Initial Admin Password:
kubectl get secret -n argocd argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
Username- Admin
Pasword- 

