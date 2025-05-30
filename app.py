from flask import Flask
from routes.admin import admin_bp
from routes.participants import participants_bp
from routes.login import login_bp
from routes.event_type import event_type_bp
from routes.event_info import event_info_bp
from config import get_config

def create_app():
    """Application factory function"""
    # Get configuration
    config_obj = get_config()
    
    # Create Flask app
    app = Flask(__name__)
    
    # Configure the app
    app.config.from_object(config_obj)
    app.secret_key = config_obj.SECRET_KEY
    
    # Register blueprints
    app.register_blueprint(admin_bp)
    app.register_blueprint(participants_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(event_type_bp)
    app.register_blueprint(event_info_bp)
    
    return app

# Create the application instance
app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config.get('DEBUG', False))
