from zoom_recording_manager import db

class ZoomWebhook(db.Model):
    __tablename__ = "zoom_webhook"
    id = db.Column(db.Integer, primary_key=True)
    payload = db.Column(db.Text)
    processed = db.Column(db.Boolean, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_onupdate=db.func.now(), server_default=db.func.now()
    )
