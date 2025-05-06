from datetime import datetime

from app.init import db


class Detection(db.Model):
    __tablename__ = 'detection'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text)  # LONGTEXT对应SQLAlchemy的Text类型
    picture_url = db.Column(db.String(255))
    result = db.Column(db.Text)  # LONGTEXT对应SQLAlchemy的Text类型
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Detection {self.id}>'