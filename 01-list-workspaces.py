import boto3

def lambda_handler(event, context):
    workspaces_list = get_workspaces()
    # do something with the list of workspaces, such as print or return it
    print(workspaces_list)
    
def get_workspaces():
    client = boto3.client('workspaces')
    response = client.describe_workspaces()
    workspaces_list = response['Workspaces']
    # do something with the list of workspaces, such as print or return it
    return workspaces_list
