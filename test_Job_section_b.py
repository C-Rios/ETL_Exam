import boto3
import datetime
import unittest
from Job_section_b import get_objects, csv_parse

content_to__download = [
    ('El_Espectador', 'https://www.elespectador.com/'),
    ('Publimetro', 'https://www.publimetro.co/'),
    ('El_Tiempo', 'https://www.eltiempo.com')
]
bucket_name = 'buck-eriodicos'

class TestScript(unittest.TestCase):

    def test_get_objects(self):
        bucket_name = 'test-bucket'
        content_to_download = [
            ('Test1', 'https://www.test1.com/'),
            ('Test2', 'https://www.test2.com/')
        ]

        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)

        # Hace un mock de S3 y hace el get
        class MockBucketObject:
            def __init__(self, body):
                self.body = body

            def get(self):
                return {'Body': self.body}

        # Mock el método bucket.Object() para devolver el mock BucketObject
        def mock_bucket_object(key):
            # Extract the name and date from the key
            name, date = key.split('/')[2].split('-')
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            
            body = f"This is a test object for {name} on {date}"
            
            return MockBucketObject(body)

        bucket.Object = mock_bucket_object

        objects = get_objects()

        self.assertEqual(len(objects), 3)

    def test_csv_parse(self):
        info = [
            ('category1', 'title1', 'link1'),
            ('category2', 'title2', 'link2'),
            ('category3', 'title3', 'link3')
        ]

        csv_result = csv_parse(info)

        expected_csv = "categoria, titulo, link\n" \
                       "category1, title1, link1\n" \
                       "category2, title2, link2\n" \
                       "category3, title3, link3\n"
        self.assertEqual(csv_result, expected_csv)


if __name__ == '__main__':
    unittest.main()