from flask import Flask
from datasource.db_session import engine
from entities.model import Base
from controllers.routes import client_bp

app= Flask(__name__)

# Create Tables
Base.metadata.create_all(engine)

# Register routes
app.register_blueprint(client_bp)

if __name__=="__main__":
    app.run(debug=False, port=8082)