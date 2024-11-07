from enum import Enum

from database import database as db


class TaskStatus(str, Enum):
    unassigned = "Unassigned"
    in_progress = "In Progress"
    completed = "Completed"


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.Enum(TaskStatus))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def as_dict(self):
        return {'id': self.id,
                'title': self.title,
                'status': self.status,
                'assignee': self.user.username if self.user else None,
                }
