from flask import Flask, redirect , request
import requests
import json
from flask import jsonify
import flask_monitoringdashboard as dashboard

app = Flask(__name__)

dashboard.config.init_from(file='/home/gpelizario/Python/flask/config.cfg')

cabecalho = {'x-api-key': '8e6b6a96-2f0d-408e-a6cd-7e5fda61ce6b'}

dashboard.bind(app)

@app.route('/home')
def home():
    return "Case Cat Api"

@app.route('/')
def info():
    name = request.args['name']

    requisicao = requests.get('https://api.thecatapi.com/v1/breeds/search?q='+ name,
                          headers=cabecalho)
    
    dicionario_info_raca = json.loads(requisicao.text)[0]
    nome_gato = (dicionario_info_raca["name"])
    origem_gato = (dicionario_info_raca["country_code"])
    temp_gato = (dicionario_info_raca["temperament"])
    desc_gato = (dicionario_info_raca["description"])

    return  jsonify(nome=nome_gato,origem=origem_gato,temperamento=temp_gato,descricao=desc_gato)

@app.route('/oculos')
def oculos():

    fantasia = requests.get('https://api.thecatapi.com/v1/images/search?category_ids=4',
                            headers=cabecalho)

    for i in json.loads(fantasia.text):
        fantasia_cat = (i['url'])
        return "Essas são as fotos de gatos de oculos {}".format(fantasia_cat)

@app.route('/hat')
def hat ():

    chapeu = requests.get('https://api.thecatapi.com/v1/images/search?category_ids=1',
                            headers=cabecalho)

    for i in json.loads(chapeu.text):
        hat_cat = (i['url'])
        return "Essas são as fotos de gatos de chápeu {}".format(hat_cat)

app.run(host='0.0.0.0', port=5000)



