import boto3
client = boto3.client('sns')
response = client.publish(
            TopicArn='arn:aws:sns:us-east-1:567470064584:tes2',
         Message='hello there\nThis is a second line'
     )