import json
from os import environ

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from database.init import DatabaseInitialiser
from pdf.coop_pdf_parser import CoopPdfParser
from credit_suisse.credit_suisse_api import CreditSuisseApi

app = Flask(__name__)


@app.route('/api/post_something', methods=['POST'])
def api_post_something():
    try:
        json_data = request.get_json()
        return jsonify(**{"hello": json_data['hello']})
    except Exception as e:
        return jsonify(**{"error": e})


@app.route('/api/get_something', methods=['GET'])
def api_get_something():
    return jsonify(**{"hello": "world"})


@app.route('/api/test_pdf', methods=['POST'])
def api_test_pdf():
    try:
        json_data = request.get_json()
        return jsonify(CoopPdfParser.parse(json_data['pdf']))
    except Exception as e:
        return jsonify(**{"error": e})


@app.route('/api/get_etf', methods=['POST'])
def api_get_etf():
    cs = CreditSuisseApi()
    return cs.get_etf().content


@app.route('/')
def index():
    return render_template('index.html', example_data="hello")


@app.route('/overview')
def overview():
    return render_template('overview.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/compensate')
def compensate():
    return render_template('compensate.html')


if __name__ == '__main__':
    load_dotenv()
    if environ.get('VCAP_SERVICES'):
        services_credentials = json.loads(environ.get('VCAP_SERVICES'))
        environ['DATABASE_HOST'] = str(services_credentials['mariadbent'][0]['credentials']['host'])
        environ['DATABASE_PORT'] = str(services_credentials['mariadbent'][0]['credentials']['port'])
        environ['DATABASE_NAME'] = str(services_credentials['mariadbent'][0]['credentials']['name'])
        environ['DATABASE_USER'] = str(services_credentials['mariadbent'][0]['credentials']['username'])
        environ['DATABASE_PASSWORD'] = str(services_credentials['mariadbent'][0]['credentials']['password'])
    print("========================================")
    print("=========         ENV VARS         =====")
    print("========================================")
    print(f"database host: {environ.get('DATABASE_HOST')}")
    print(f"database port: {environ.get('DATABASE_PORT')}")
    print(f"database user: {environ.get('DATABASE_USER')}")
    print(f"database pw: {environ.get('DATABASE_PASSWORD')}")
    print(f"database name: {environ.get('DATABASE_NAME')}")
    print("========================================")
    DatabaseInitialiser.init()
    app.run(host='0.0.0.0', port=3000, debug=True)
