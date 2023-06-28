import boto3
import datetime

def lambda_handler(event, context):
    
    workspace_id = event['workspace_id']
    time_threshold = event.get('time_threshold', 60) # default to 60 minutes
    workspaces_client = boto3.client('workspaces')
    
    try:
        response = workspaces_client.describe_workspaces_connection_status(
            WorkspaceIds=[workspace_id]
        )
        connection_status = response['WorkspacesConnectionStatus'][0]
        
        #if connection_status['ConnectionState'] != 'CONNECTED':
        #    return {
        #        'statusCode': 200,
        #        'body': 'Workspace is not currently connected'
        #    }
        
        last_connection_time = connection_status['LastKnownUserConnectionTimestamp']
        time_since_last_connection = (datetime.datetime.now(datetime.timezone.utc) - last_connection_time).total_seconds() / 60
        
        if time_since_last_connection > time_threshold:
            return {
                'statusCode': 200,
                'body': f'Time since last connection ({time_since_last_connection:.2f} minutes) exceeds threshold of {time_threshold} minutes'
            }
        else:
            return {
                'statusCode': 200,
                'body': f'Time since last connection: {time_since_last_connection:.2f} minutes'
            }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': f'Error getting connection status: {e}'
        }
