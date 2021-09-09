from app import db

class ShortedUrl(db.Model):
    
    
    __tablename__ = 'shortedUrls'

    id = db.Column(
        db.Integer, 
        primary_key=True, 
        autoincrement=True, 
        unique=True
    )

    url = db.Column(db.Text)
    uuid = db.Column(db.Text, unique=True)

    def __init__(self, url, uuid):
        self.url = url
        self.uuid = uuid
