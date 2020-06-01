from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return '<h1>This is AboutPage!!!!!!<h1>'


@app.route('/data')
def data():
    dict = {"a": 100, "b": 200}
    return jsonify(dict)


@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({
        'result': 'success',
        'msg': '이 요청은 GET!',
        'title_receive': title_receive,
        'data': [
            request.args.get('b'),
            request.args.get('a')
        ],
    })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
