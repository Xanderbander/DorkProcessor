from flask import Flask, jsonify
from data_retrieval import retrieve_data

app = Flask(__name__)

@app.route('/api/extract-data', methods=['GET'])
def extract_data_api():
    try:
        url = "https://example.com"
        css_selector = "div.result"
        date_selector = "div.date"
        date_format = "%Y-%m-%d"
        data_pattern = r"^[0-9]{16}$"
        output_filename = "cards.csv"

        data = retrieve_data(url, css_selector, date_selector, date_format, data_pattern, output_filename)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
