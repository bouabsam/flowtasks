from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize database (empty for now)
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    
    # Initialize database with app
    db.init_app(app)
    
    # Health check endpoint (kept for testing)
    @app.route('/health')
    def health():
        return {'status': 'ok', 'message': 'FlowTasks API running'}, 200
    
    # Register blueprints (routes)
    from app.routes.projects import projects_bp
    app.register_blueprint(projects_bp, url_prefix='/api/projects')

    # ✅ ADD THIS LINE
    from app.routes.tasks import tasks_bp
    app.register_blueprint(tasks_bp, url_prefix='/api')

    # Add with the other blueprint registrations        
    from app.routes.views import views_bp
    app.register_blueprint(views_bp, url_prefix='/')


    
    return app