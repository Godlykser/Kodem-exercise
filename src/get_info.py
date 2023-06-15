from kubernetes import client, config
import json

def get_info():
    """
    get the requested info from all workloads in cluster
    """
    config.load_kube_config() # load local config file
    v1 = client.CoreV1Api() # create api object
    info = [] # list to store info
    
    pods = v1.list_pod_for_all_namespaces(watch=False) # all pods in all namespaces
    deployments = v1.list_deployment_for_all_namespaces(watch=False) # all deployments in all namespaces
    
    get_pod_info(info, pods)
    # iterate through all pods and get info
    return info

def get_pod_info(info, pods):
    for pod in pods.items:
        workload = {
            "name": pod.metadata.name,
            "type": "pod",
            "namespace": pod.metadata.namespace,
            "uid": pod.metadata.uid
        }
    info.append(workload)
    

def main():
    """
    Main function
    """
    info = get_info()
    json_info = json.dumps(info, indent=4)
    print(json_info)

if __name__ == "__main__":
    main()