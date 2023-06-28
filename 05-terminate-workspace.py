import boto3

def lambda_handler(event, context):
    
    workspace_id = event['workspace_id']
    workspaces_client = boto3.client('workspaces')
    
    try:
        response = workspaces_client.terminate_workspaces(
            TerminateWorkspaceRequests=[
                {
                    'WorkspaceId': workspace_id
                },
            ]
        )
        return {
            'statusCode': 200,
            'body': 'Workspace terminated successfully'
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': f'Error terminating workspace: {e}'
        }
