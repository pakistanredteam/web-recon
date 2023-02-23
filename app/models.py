from app import db

class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    last_scan = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Website {self.url}>'
