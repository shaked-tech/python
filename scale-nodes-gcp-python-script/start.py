import base64, json
from googleapiclient import discovery

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None


def start_instance(compute, project, zone, instance):
    request = compute.instances().start(project=project, zone=zone, instance=instance)
    response = request.execute()
    print(response)
    # return response['status']


def stop_instance(compute, project, zone, instance):
    request = compute.instances().stop(project=project, zone=zone, instance=instance)
    response = request.execute()
    print(response)
    # return response['status']


def start_stop_cluster(container, project, zone, cluster, nodePools, nodeCount):
    path_format = "projects/%s/locations/%s/clusters/%s/nodePools/%s" % (project, zone, cluster, nodePools)

    set_node_pool_size_request_body = {
      "nodeCount": nodeCount,
    }
    request = container.projects().locations().clusters().nodePools().setSize(name=path_format, body=set_node_pool_size_request_body)
    response = request.execute()
    print(response)



def main(): ### event , context
    # authentication
    # compute = discovery.build('compute', 'v1')
    # container = discovery.build('container', 'v1')

    ## decoding and parsing job details
    # pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    # print("pub/sub message: " + pubsub_message)
    # parsed_pubsub_message = json.loads(pubsub_message)

    # action = parsed_pubsub_message['action']
    # project = parsed_pubsub_message['project']
    # zone = parsed_pubsub_message['zone']
    # cluster = parsed_pubsub_message['cluster']
    # nodePools = parsed_pubsub_message['nodePools']
    # instance = parsed_pubsub_message['instance']
    action = "start"
    project = "example"
    zone = "europe-west1-b"
    cluster = "demo-cluster"
    nodePools = "demo-private-node-pool"
    instance = "demo-jump-server"

    if (action == "start"):
        if (instance != ""):
            print("**%sing instance %s, In zone: %s in project: %s**" % (action, instance, zone, project))
            start_instance(compute, project, zone, instance)
            print("Machine %s started." % (instance))
        else:
            print("skipping: %sing instance" % (action))

        if (cluster != ""):
            print("**%sing cluster %s, In zone: %s in project: %s**" % (action, cluster, zone, project))
            start_stop_cluster(container, project, zone, cluster, nodePools, 1)
            print("Cluster %s started." % (cluster))
        else:
            print("skipping: %sing cluster" % (action))

    elif(action == "stop"):
        if (instance != ""):
            print("**%sping instance %s, In zone: %s in project: %s**" % (action, instance, zone, project))
            stop_instance(compute, project, zone, instance)
            print("Machine %s stopped." % (instance))
        else:
            print("skipping: %sing instance" % (action))

        if (cluster != ""):
            print("**%sping cluster %s, In zone: %s in project: %s**" % (action, cluster, zone, project))
            start_stop_cluster(container, project, zone, cluster, nodePools, 0)
            print("Cluster %s stopped." % (cluster))
        else:
            print("skipping: %sing cluster" % (action))

    else:
        print("action unrecognized")


if __name__ == "__main__": #### 
    main()


# PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
# # Date of machine is set to (GMT+0)
# # scale-up develop-cluster monday-friday at 06:00 jerusalem time (GMT+2), 8:30 Kolkata time (GMT+5:30)
# 00 03 * * 1-5 echo y | gcloud container clusters resize develop-cluster --node-pool develop-private-node-pool --num-nodes=1 --zone asia-east1-a

# # scale-down develop-cluster monday-friday at 22:00 jerusalem time (GMT+2), 00:30 Kolkata time (GMT+5:30)
# 00 19 * * 1-5 echo y | gcloud container clusters resize develop-cluster --node-pool develop-private-node-pool --num-nodes=0 --zone asia-east1-a

# ---

# # Date of machine is set to (GMT+0)
# # scale-up demo-cluster sunday-thursday at 09:00 jerusalem time (GMT+2), 11:30 Kolkata time (GMT+5:30)
# 00 06 * * 0-4 echo y | gcloud container clusters resize demo-cluster --node-pool demo-private-node-pool --num-nodes=1 --zone europe-west1-b

# # scale-down demo-cluster sunday-thursday at 18:00 jerusalem time (GMT+2), 20:30 Kolkata time (GMT+5:30)
# 53 15 * * 0-4 echo y | gcloud container clusters resize demo-cluster --node-pool demo-private-node-pool --num-nodes=1 --zone europe-west1-b