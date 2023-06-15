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
    # iterate through all pods and get info
    for pod in pods.items:
        workload = (str(pod.metadata.name), 
                    str(pod.kind), 
                    str(pod.metadata.namespace), 
                    str(pod.metadata.uid))
        # if workload not in info, add it
        info.append(workload)
    return info

def to_json(info):
    """
    convert info into json format
    """
    return json.dumps(info)

def main():
    """
    Main function
    """
    info = get_info()
    json_info = to_json(info)
    return(json_info)

if __name__ == "__main__":
    main()