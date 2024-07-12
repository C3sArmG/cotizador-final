from flask import Flask, render_template, request, jsonify
import cotizador

def crear_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/cotizar', methods=['POST'])
    def cotizar():
        data = request.form
        nombre_cliente = request.form.get('nombreCliente')
        pvp_mercado = request.form.get('pvp_mercado').replace(',', '')
        kilometraje = request.form.get('kilometraje').replace(',', '')
        rotacion = request.form['rotacion'].lower()

        # Validar si los valores de pvp_mercado y kilometraje son numéricos
        if not pvp_mercado.replace('.', '', 1).isdigit() or not kilometraje.replace('.', '', 1).isdigit():
            return jsonify({'error': 'Los valores de PVP Mercado y Kilometraje deben ser numéricos.'}), 400

        pvp_mercado = float(pvp_mercado)
        kilometraje = float(kilometraje)

        valor_final = cotizador.cotizar_auto(pvp_mercado, kilometraje, rotacion)
        valor_partepago = cotizador.valor_partepago(valor_final)

        response = {
            'nombreCliente': nombre_cliente,
            'valor_final': valor_final,
            'valor_partepago': valor_partepago
        }

        return jsonify(response) 
    return app

if __name__ == "__main__":
    app=crear_app()
    app.run()


























#from flask import Flask, render_template, request
#import cotizador

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')

#@app.route('/cotizar', methods=['POST'])
#def cotizar():
 #   marca = request.form['marca']
  #  modelo = request.form['modelo']
   # version = request.form['version']
   # año = int(request.form['año'])
   ## pvp_mercado = float(request.form['pvp_mercado'])
   # kilometraje = int(request.form['kilometraje'])
   # rotacion = request.form['rotacion'].lower()


    #valor_final = cotizador.cotizar_auto(pvp_mercado, kilometraje, rotacion)
    #return valor_final

#if __name__ == "__main__":
 #   app.run(debug=True)


