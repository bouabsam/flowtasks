from app import create_app, db
from app.models.project import Project

app = create_app()

with app.app_context():
    # Create a sample project
    project = Project(
        name="Learn Flask API",
        description="Building my first real backend",
        status="active"
    )
    
    # Add to database
    db.session.add(project)
    db.session.commit()
    
    print("✅ Added project to database!")
    
    # Show all projects
    all_projects = Project.query.all()
    for p in all_projects:
        print(f"- {p.id}: {p.name} ({p.status})")