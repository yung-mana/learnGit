import boto3
client = boto3.client('sns')
response = client.publish(
            TopicArn='arn:aws:sns:us-east-1:567470064584:tes2',
         Message='THis is master From githum!!'
     )
