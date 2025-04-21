from flask import Flask, render_template

from cliente_dao import ClienteDAO

app = Flask(__name__)

titulo_app = 'Zona Fit (GYM)'

@app.route('/') # url: http://localhost:5000
@app.route('/index')
def index():
    app.logger.debug('Servidor site flask')
    #recuperamos los clientes de la bd

    cliente_db = ClienteDAO.seleccionar()

    return render_template('index.html', titulo=titulo_app, clientes=cliente_db)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)