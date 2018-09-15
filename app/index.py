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
    DatabaseInitialiser.init()
    app.run(host='0.0.0.0', port=3000, debug=True)
