import boto3

def send_email_notification(event, context):
    # Get the email, subject, and message from the event payload
    email = event['email']
    subject = event['subject']
    message = event['message']
    
    # Create a new SES client
    ses_client = boto3.client('ses')
    
    # Send email
    response = ses_client.send_email(
        Destination={
            'ToAddresses': [
                email,
            ],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source='CHANGE_ME',
        
    )
    
    return response

def lambda_handler(event, context):
    return send_email_notification(event, context)
