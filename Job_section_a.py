import boto3
import urllib.request
from datetime import datetime

# Periodicos considerados c:
content_to__download = [
    ('El_Espectador', 'https://www.elespectador.com/'),
    ('Publimetro', 'https://www.publimetro.co/'),
    ('El_Tiempo', 'https://www.eltiempo.com')
]

#Test github workflow
def download_and_upload_newspapers():
    client = boto3.client("s3")
    bucket = 'buck-eriodicos'

    date = datetime.now()
    for name, url in content_to__download:
        try:
            response = urllib.request.urlopen(url)
        except Exception as e:
            print(f"Error occurred while downloading {name}: {e}")
            continue
        webContent = response.read().decode('UTF-8')
        client.put_object(Body=webContent, Bucket=bucket,
                            Key=f'headlines/raw/{name}-{date.strftime("%Y-%m-%d")}.html')


download_and_upload_newspapers()
