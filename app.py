from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crawl', methods=['POST'])
def crawl():
    query = request.json.get('query')
    if not query:
        return jsonify({'error': '검색어를 입력해주세요.'}), 400

    try:
        result = subprocess.check_output(['python3', 'crawler.py', query], text=True)
        return jsonify({'result': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

