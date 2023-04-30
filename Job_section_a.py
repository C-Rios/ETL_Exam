import boto3
import urllib.request
from datetime import datetime

content_to__download = [
    ('El_Espectador', 'https://www.elespectador.com/'),
    ('Publimetro', 'https://www.publimetro.co/'),
    ('El_Tiempo', 'https://www.eltiempo.com')
]

def download_and_upload_newspapers():
    client = boto3.client("s3")
    bucket = 'buck-eriodicos'

    date = datetime.now()
    for name, url in content_to__download:
        response = urllib.request.urlopen(url)
        webContent = response.read().decode('UTF-8')
        client.put_object(Body=webContent, Bucket=bucket,
                            Key=f'headlines/raw/{name}-{date.strftime("%Y-%m-%d")}.html')

download_and_upload_newspapers()