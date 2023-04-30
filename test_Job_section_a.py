import unittest
from unittest.mock import patch
from io import BytesIO
from datetime import datetime

from Job_section_a import download_and_upload_newspapers


class TestDownloadAndUploadNewspapers(unittest.TestCase):
    @patch('Job_section_a.urllib.request.urlopen')
    @patch('Job_section_a.boto3.client')

    def test_download_and_upload_newspapers(self, mock_client, mock_urlopen):
        mock_web_content = b'This is a mock web page.'
        mock_urlopen.return_value = BytesIO(mock_web_content)

        download_and_upload_newspapers()

        # comprueba que put_object se ha llamado con los parámetros correctos para cada periódico
        expected_calls = [
            ('El_Espectador', b'This is a mock web page.'),
            ('Publimetro', b'This is a mock web page.'),
            ('El_Tiempo', b'This is a mock web page.')
        ]
        for i, (args, kwargs) in enumerate(mock_client.return_value.put_object.call_args_list):
            self.assertEqual(kwargs['Bucket'], 'buck-eriodicos')
            self.assertEqual(kwargs['Key'], f'headlines/raw/{expected_calls[i][0]}-{datetime.now().strftime("%Y-%m-%d")}.html')