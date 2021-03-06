from flask import Flask, request, jsonify, render_template
import poker as p
import series as s
from model import model
from test_controller import test_controller

app = Flask(__name__, static_url_path='/static2', static_folder='./static2')
app.register_blueprint(test_controller, url_prefix='/testNamespace')


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
    outStr = '<h1>Hello {} , you are {} years old.</h1>'.format(name, age)
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

@app.route('/hello_get2')
def hello_get2():
    name = request.args.get('name')
    age = request.args.get('age')
    # render_template return HTML string
    return render_template('hello_get.html',
                            name=name,
                            age=age)

@app.route('/hello_post2')
def hello_post2():
    method = request.method
    username = request.form.get('username') if method == 'POST' else ''
    return render_template('hello_post.html',
                           method=method,
                           username=username)

@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players)
    return render_template('poker.html', request_method=request_method,
                                         cards=cards)

@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)