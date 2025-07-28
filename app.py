from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from ORCA.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            # Coleta dos dados do formulário
            modelo = request.form['Modelo']
            registro = request.form['Registro']
            comprimento = float(request.form['Comprimento'])
            largura = float(request.form['Largura'])
            moldura = request.form['Moldura']
            pintura = request.form['Pintura']
            
            # Monta DataFrame com as variáveis esperadas
            data = pd.DataFrame([{
                'Modelo': modelo,
                'Registro': registro,
                'Comprimento': comprimento,
                'Largura': largura,
                'Moldura': moldura,
                'Pintura': pintura,
                'Area': comprimento * largura,
                'Comprimento/Largura': comprimento / largura if largura != 0 else 0,
                'Produto': 'GRELHA DE ALETAS FIXAS'
            }])

            print("COLUNAS NA PREDIÇÃO:", data.columns.tolist())

            obj = PredictionPipeline()
            predict = obj.predict(data)
            valor = round(float(predict[0]), 2)
            return render_template('results.html', prediction=f"R$ {valor:,.2f}")

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)