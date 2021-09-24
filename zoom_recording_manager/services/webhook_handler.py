from zoom_recording_manager import models, helpers
import json
from . import RecordingHandler

class WebhookHandler(object):
    def capture_webhook(self, jsonData):
        new_webhook_log = models.ZoomWebhook(
            payload=json.dumps(jsonData), processed=False
        )
        
        helpers.save(new_webhook_log)
        
        recording_handler = RecordingHandler()
        # recording_handler.upload_recording()
        
        return