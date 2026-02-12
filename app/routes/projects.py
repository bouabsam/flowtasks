from flask import Blueprint, request, jsonify
from app import db
from app.models.project import Project

# Create blueprint
projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/', methods=['GET'])
def get_projects():
    """Get all projects"""
    projects = Project.query.all()
    return jsonify([p.to_dict() for p in projects]), 200

@projects_bp.route('/', methods=['POST'])
def create_project():
    """Create a new project"""
    data = request.get_json()
    
    # Validation
    if not data or 'name' not in data:
        return {'error': 'Project name is required'}, 400
    
    # Create project
    project = Project(
        name=data['name'],
        description=data.get('description', ''),
        status=data.get('status', 'active')
    )
    
    # Save to database
    db.session.add(project)
    db.session.commit()
    
    return jsonify(project.to_dict()), 201

@projects_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Get a single project by ID"""
    project = Project.query.get(project_id)
    
    if not project:
        return {'error': 'Project not found'}, 404
    
    return jsonify(project.to_dict()), 200

@projects_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update a project"""
    project = Project.query.get(project_id)
    
    if not project:
        return {'error': 'Project not found'}, 404
    
    data = request.get_json()
    
    # Update fields if provided
    if 'name' in data:
        project.name = data['name']
    if 'description' in data:
        project.description = data['description']
    if 'status' in data:
        project.status = data['status']
    
    db.session.commit()
    
    return jsonify(project.to_dict()), 200

@projects_bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a project"""
    project = Project.query.get(project_id)
    
    if not project:
        return {'error': 'Project not found'}, 404
    
    db.session.delete(project)
    db.session.commit()
    
    return {'message': 'Project deleted successfully'}, 200