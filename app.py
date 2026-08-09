from flask import Flask 

app = Flask(__name__)

@app.route('/')
def inicio():
    return "¡Hola mundo! Mi primera página web en Render con Python"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)