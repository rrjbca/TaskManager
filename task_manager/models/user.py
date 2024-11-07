from database import database as db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    tasks = db.relationship("Task", backref="user")

    def as_dict(self):
        return {'id': self.id,
                'username': self.username,
                'tasks': [t.id for t in self.tasks],
                }
