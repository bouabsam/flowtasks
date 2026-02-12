from app import create_app, db
from app.models.project import Project
from app.models.task import Task
import os

app = create_app()

with app.app_context():
    # Drop all tables
    db.drop_all()
    print("🗑️ Dropped all tables")
    
    # Create all tables
    db.create_all()
    print("✅ Created all tables")
    
    # Create sample project
    project = Project(
        name="FlowTasks MVP",
        description="Build the task manager app"
    )
    db.session.add(project)
    db.session.commit()
    print(f"✅ Created project: {project.name}")
    
    # Create sample tasks
    tasks = [
        Task(title="Setup database", status="done", project_id=project.id),
        Task(title="Create Project model", status="done", project_id=project.id),
        Task(title="Create Task model", status="done", project_id=project.id),
        Task(title="Build API endpoints", status="doing", project_id=project.id),
        Task(title="Add authentication", status="todo", project_id=project.id),
        Task(title="Deploy to production", status="todo", project_id=project.id),
    ]
    
    for task in tasks:
        db.session.add(task)
    
    db.session.commit()
    print(f"✅ Added {len(tasks)} tasks")
    
    print("\n📊 Database ready with sample data!")