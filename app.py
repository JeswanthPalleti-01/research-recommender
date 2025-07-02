from flask import Flask, request, jsonify, render_template
from utils.fetch_and_filter import fetch_and_filter_relevant_papers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')
    category = data.get('category', 'cs.AI')
    max_results = int(data.get('max_results', 20))

    if not query:
        return jsonify({"error": "Query is required"}), 400

    results = fetch_and_filter_relevant_papers(query, category, max_results)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

