import boto3

bucket_name = 'aws-glue-assets-551620806533-us-east-1'

client = boto3.client('s3')

f = open('Job_section_a.py', 'r').read()
client.put_object(Body=f, Bucket=bucket_name,
                      Key=f'scripts/Job_section_a.py')

f = open('Job_section_b.py', 'r').read()
client.put_object(Body=f, Bucket=bucket_name,
                      Key=f'scripts/Job_section_b.py')