#!/usr/bin/env python3

import requests
import subprocess

def jfrogUpload():
    url = "http://18.204.207.55:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.3-SNAPSHOT.jar"
    file_path = "/var/lib/jenkins/workspace/Java_Project/target/kubernetes-configmap-reload-0.0.3-SNAPSHOT.jar"
    username = 'admin'
    password = 'Admin123'

    with open(file_path,'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)
    if response.status_code == 201:
        print("\nPUT request was successful!")
    else:
        print("PUT request failed with status code(response.status_code)")
        print("Response content:")
        print(response.text)

def mvnBuild():
   maven_command = "mvn clean install -DskipTests"

try:
    print("\nMaven build completed succesfully.")
except subprocess.CalledProcessError as e:
       print(f"Error: Maven build failed with exit code (e.returncode)")

def main():
    mvnBuild()
    jfrogUpload()

########################

if __name__ == "__main__":
    main()

