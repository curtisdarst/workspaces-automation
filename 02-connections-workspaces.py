import boto3
import datetime

def lambda_handler(event, context):
    workspaces_list = get_workspaces()
    for workspace in workspaces_list:
        workspace_id = workspace['WorkspaceId']
        last_connection_time = get_last_connection_status(workspace_id)
        print(f"User last connected to WorkSpace {workspace_id} at {last_connection_time}")
        
def get_workspaces():
    client = boto3.client('workspaces')
    response = client.describe_workspaces()
    workspaces_list = response['Workspaces']
    return workspaces_list

def get_last_connection_status(workspace_id):
    client = boto3.client('workspaces')
    response = client.describe_workspaces_connection_status(
        WorkspaceIds=[workspace_id]
    )
    connection_status_list = response['WorkspacesConnectionStatus']
    last_connection_timestamp = connection_status_list[0]['LastKnownUserConnectionTimestamp']
    last_connection_datetime = datetime.datetime.fromtimestamp(last_connection_timestamp / 1000)
    return last_connection_datetime
