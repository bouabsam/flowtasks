from flask import Blueprint, request, jsonify
from app import db
from app.models.task import Task
from app.models.project import Project

tasks_bp = Blueprint('tasks', __name__)

# Get all tasks for a specific project
@tasks_bp.route('/project/<int:project_id>/tasks', methods=['GET'])
def get_tasks(project_id):
    # Check if project exists
    project = Project.query.get(project_id)
    if not project:
        return {'error': 'Project not found'}, 404
    
    tasks = Task.query.filter_by(project_id=project_id).all()
    return jsonify([t.to_dict() for t in tasks]), 200

# Create a task in a project
@tasks_bp.route('/project/<int:project_id>/tasks', methods=['POST'])
def create_task(project_id):
    # Check if project exists
    project = Project.query.get(project_id)
    if not project:
        return {'error': 'Project not found'}, 404
    
    data = request.get_json()
    
    # Validation
    if not data or 'title' not in data:
        return {'error': 'Task title is required'}, 400
    
    # Create task
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'todo'),
        project_id=project_id
    )
    
    db.session.add(task)
    db.session.commit()
    
    return jsonify(task.to_dict()), 201

# Get single task
@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return {'error': 'Task not found'}, 404
    
    return jsonify(task.to_dict()), 200

# Update a task
@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return {'error': 'Task not found'}, 404
    
    data = request.get_json()
    
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'status' in data:
        task.status = data['status']
    
    db.session.commit()
    
    return jsonify(task.to_dict()), 200

# Delete a task
@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return {'error': 'Task not found'}, 404
    
    db.session.delete(task)
    db.session.commit()
    
    return {'message': 'Task deleted successfully'}, 200