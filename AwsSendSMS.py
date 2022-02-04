import boto3
client = boto3.client('sns')
response = client.publish(
            TopicArn='dfedfc',
         Message='This is a new branch!!'
     )