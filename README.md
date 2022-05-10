# Deploying a Flask API and MySQL server on Kubernetes

This repo contains code that 
1) Deploys a MySQL server on a Kubernetes cluster
2) Attaches a persistent volume to it, so the data remains contained if pods are restarting
3) Deploys a Flask API  in the MySQL database

## Prerequisites
1. Have `Docker` and the `Kubernetes CLI` (`kubectl`) installed together with `Minikube` (https://kubernetes.io/docs/tasks/tools/)
2. There are 3 components in this deployment:
    Kubernetes cluster
    MySQL running on Kubernetes cluster
    Simple Rest API Application running on Kubernetes cluster and able to use MySQL running on the same cluster

## Getting started
1. Clone the repository
2. Configure `Docker` to use the `Docker daemon` in your kubernetes cluster via your terminal: `eval $(minikube docker-env)`
3. Pull the latest mysql image from `Dockerhub`: `Docker pull mysql`
4. Build a kubernetes-api image with the Dockerfile in this repo: `Docker build . -t flask-api`

## Secrets
`Kubernetes Secrets` can store and manage sensitive information. For this example we will define a password for the
`root` user of the `MySQL` server using the `Opaque` secret type. For more info: https://kubernetes.io/docs/concepts/configuration/secret/

1. Encode your password in your terminal: `echo -n Pa$$word1234 | base64`
2. Add the output to the `flakapi-secrets.yml` file at the `db_root_password` field

## config map 

Use config-map.yaml to define values of environment variables that will be used in the API application
You should add the correct value for MYSQL_ROOT_HOST
Use the output of the following command

## Deployments
Get the secrets, persistent volume in place and apply the deployments for the `MySQL` database and `Flask API`

1. Add the secrets to your `kubernetes cluster`: `kubectl apply -f secrets.yaml`
2. Add the config-map to your `kubernetes cluster`: `kubectl apply -f config-map.yaml`
3. Create the `persistent volume` and `persistent volume claim` for the database: `kubectl apply -f mysql-pv.yaml`
4. Create the `MySQL` deployment: `kubectl apply -f mysql-deployment.yaml`
5. Create the `Flask API` deployment: `kubectl apply -f deployment.yaml`

You can check the status of the pods, services and deployments.

## Creating database and schema
The API can only be used if the proper database and schemas are set. This can be done via the terminal.
1. Connect to your `MySQL database` by setting up a temporary pod as a `mysql-client`: 
   `kubectl run -it --rm --image=mysql --restart=Never mysql-client -- mysql --host mysql --password=<super-secret-password>`
   make sure to enter the (decoded) password specified in the `flaskapi-secrets.yml`
2. Create the database and table
   1. `CREATE DATABASE mydb;`
    2. `USE mydb;`
    3. `CREATE TABLE IF NOT EXISTS scores(score INT);`
    
## Expose the API
The API can be accessed by exposing it using minikube: `minikube service flask-service`. This will return a `URL`. If you paste this to your browser you will see the `Hello Devops 123` message. You can use this `service_URL` to make requests to the `API`


