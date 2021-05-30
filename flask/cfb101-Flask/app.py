from flask import Flask, request, jsonify
import poker as p
import series as s

app = Flask(__name__, static_url_path='/static2', static_folder='./static2')

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/hello/Allen')
def geetAtAllen():
    return 'Hello Allen!'

@app.route('/hello/Ted')
def geetAtTed():
    return 'Hello Ted!'

@app.route('/hello/<name>')
def greet(name):
    greetStr = 'Hello {}!'
    return greetStr.format(name)

@app.route('/hello_get')
def hello_get():
    name = request.args.get('name')
    age = request.args.get('age')
    outStr = '<h1>Hello {} , you are {} years old.<h1>'.format(name, age)
    return outStr # HTML string

@app.route('/add/<x>/<y>')
def add(x, y):
    return str(int(x) + int(y))

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    method = request.method
    outStr = """
    <form action="/hello_post" method="POST">
        <div>
            What's your name?
        </div>
        <div>
            <input name="username">
        </div>
        <div>
            <button type="submit">SUBMIT</button>
        </div>
    </form>
    """
    if method == 'POST':
        username = request.form.get('username')
        outStr += """
        <h3>Hello {} !</h3>
        """.format(username)
    return outStr

@app.route('/pokerGame/<playerAmount>')
def pokerGame(playerAmount):
    playerAmountInt = int(playerAmount)
    resultJson = p.poker(playerAmountInt) # JSON
    return jsonify(resultJson) # JSON string

@app.route('/seriesNumber')
def seriesNumber():
    n = int(request.args.get('n'))
    result = str(s.Func(n))
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)