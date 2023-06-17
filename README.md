# Kodem-exercise
The assignment is to write a workload that can be deployed on a cluster and print out all the workloads from the cluster in json. 
format containing:
- name of the resource
- type of the resource
- namespace of the resource
- uid of the resource

How to use:
- change directory to kodem-exercise
- run the command 'kubectl apply -f ./kubernetes/Jobs/get_info.yaml -o json'
- after job completes, run the command 'kubectl logs job/get-info' to print out the result
  or the command 'kubectl logs job/get-info > info.json' to print it to json file.