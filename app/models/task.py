from app import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    status = db.Column(db.String(20), default='todo')  # todo, doing, done
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign key - connects each task to ONE project
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    
    # Relationship - gives us task.project and project.tasks
    project = db.relationship('Project', backref='tasks')
    
    def to_dict(self):
        """Convert task to JSON-friendly dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'project_id': self.project_id
        }