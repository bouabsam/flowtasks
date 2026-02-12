from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()
        print("✅ Database initialized!")
    
    app.run(debug=True)