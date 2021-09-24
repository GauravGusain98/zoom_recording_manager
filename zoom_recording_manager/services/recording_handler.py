import requests, boto3
from zoom_recording_manager import app

class RecordingHandler(object):
    def get_file_name(self):
        filename = "rec1.txt"
        return filename

    def download_recording(self):
        return

    def upload_recording(self):
        s3 = boto3.resource(
                service_name='s3',
                region_name=app.config['REGION_NAME'],
                aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY']
            )
        filename = self.get_file_name()
        s3.Bucket(app.config['S3_BUCKET_NAME']).upload_file("/Users/gauravgusain/Documents/ColoredCow-Projects/ColoredCow-zoom-microservice/app/recordings/test.txt", f"Recordings/Townhall/{filename}")
        return

    def delete_recording_from_local(self):
        requests.delete('/meetings/{meetingId}/recordings/{recordingId}')
        return

    def delete_recording_from_zoom(self):
        return
