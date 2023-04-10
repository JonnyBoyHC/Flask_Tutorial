from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# 1)
# @app.route('/')
# def hello():
#   # return '<html›<body›<h1>HELLO WORLD</h1></body></html>'
#   return render_template('hello.html')

# @app.route('/hello/<name>')
# def hello_name(name):
#   return render_template('hello.html', name=name)

# 2)
# @app.route('/scoring/<int:score>')
# def hello_score(score):
#   return render_template('hello.html', marks=score)

'''Codes from HTML
    <!-- 1) <h1>Hello {{name}}!</h1> -->
    <!-- 2)
    {%if marks > 50%}
    <h1>You have Passed Successfully</h1>
    {% else %}
    <h1>Better Luck next Time</h1>
    {% endif %} -->
    '''

# 3)
@app.route('/result')
def result():
  dict= {'chem' :60, 'bio': 90, 'phy':75, 'eng': 99}
  return render_template('hello.html', result=dict)

if __name__ == '__main__':
  app.run(debug=True)