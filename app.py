from flask import Flask, jsonify
import os
import psycopg2 # Para simular la conexión a la DB

app = Flask(__name__)

# --- Configuración de Base de Datos (para simular migraciones) ---
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'mydatabase')
DB_USER = os.getenv('DB_USER', 'myuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'mypassword')

def init_db():
    conn = None
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                content VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        print("Tabla 'messages' asegurada/creada.")
        cur.close()
    except Exception as e:
        print(f"Error al inicializar la DB: {e}")
    finally:
        if conn:
            conn.close()

# --- Rutas de la aplicación ---
@app.route('/')
def hello():
    return jsonify(message="Hello from our CI/CD Docker App!", version="1.0.0")

@app.route('/status')
def status():
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD, connect_timeout=3)
        conn.close()
        db_status = "Connected"
    except Exception as e:
        db_status = f"Failed to connect: {e}"
    return jsonify(app_status="Running", db_connection=db_status)

if __name__ == '__main__':
    init_db() # Intenta inicializar la DB al iniciar la app
    app.run(host='0.0.0.0', port=5000)