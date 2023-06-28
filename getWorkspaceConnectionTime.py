import boto3
import time

DEFAULT_CONNECTION_TIME = 1672531200  # January 1, 2023, 00:00:00 in Unix timestamp

def lambda_handler(event, context):
    workspaces_list = get_workspaces()
    for workspace in workspaces_list:
        workspace_id = workspace['WorkspaceId']
        last_connection_time = get_last_connection_status(workspace_id)
        current_time = int(time.time())
        time_difference = current_time - last_connection_time
        #print(f"User last connected to WorkSpace {workspace_id} {time_difference} seconds ago.")
        print(f"User last connected to WorkSpace {workspace_id} {time_difference} seconds ago.")
        return {
                'statusCode': 200,
                'body': f'{time_difference}'
            }
        
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
    if connection_status_list:
        last_connection_timestamp = connection_status_list[0].get('LastKnownUserConnectionTimestamp')
        if last_connection_timestamp:
            return int(last_connection_timestamp // 1000)  # Convert from milliseconds to seconds
    return DEFAULT_CONNECTION_TIME  # Return default connection time in seconds since January 1, 2023
