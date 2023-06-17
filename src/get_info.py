from kubernetes import client, config
import json

WORKLOAD_TYPES = [
    "Deployment",
    "StatefulSet",
    "DaemonSet",
    "Job",
    "CronJob",
    "ReplicaSet",
    "ReplicationController",
]


def get_info():
    """
    get the requested info from all workloads in cluster
    """
    config.load_incluster_config()  # load local config file and create api access objects
    v1 = client.CoreV1Api()
    info = []
    # set to store info

    # get info from all workloads
    get_pod_info(info, v1)

    return info


def get_pod_info(info, v1):
    """
    get info from all pods in cluster
    """
    # get all pods
    pods = v1.list_pod_for_all_namespaces(watch=False)
    # iterate through all pods and get info
    for pod in pods.items:
        try:
            workload = {
                "name": pod.metadata.owner_references[0].name,
                "type": pod.metadata.owner_references[0].kind,
                "namespace": pod.metadata.namespace,
                "uid": pod.metadata.owner_references[0].uid,
            }
            if workload["type"] in WORKLOAD_TYPES:
                info.append(workload)
        except:
            continue


def main():
    """
    Main function
    """
    info = get_info()
    # removes duplicates
    info = [dict(t) for t in {tuple(d.items()) for d in info}]
    # prints to log
    print(json.dumps(info, indent=4))


if __name__ == "__main__":
    main()
