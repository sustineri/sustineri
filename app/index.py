from flask import Flask, render_template, request, jsonify

from pdf.coop_pdf_parser import CoopPdfParser

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


@app.route('/')
def index():
    return render_template('index.html', example_data="hello")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
