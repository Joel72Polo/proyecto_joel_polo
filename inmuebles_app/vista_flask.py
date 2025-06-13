from flask import Flask
from app.routes import routes_bp

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesario para usar flash

app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True)