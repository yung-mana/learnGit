import boto3
client = boto3.client('sns')
response = client.publish(
            TopicArn='arn:aws:sns:region:xxxxxx:tes2',
         Message='THis is master From local machine!'
     )
