from flask import Flask, redirect, url_for, request

app = Flask(__name__, template_folder='templates')

@app.route('/success/<name>')
def success(name):
  return f'Welcome {name}'

@app.route('/login', methods=['POST','GET'])
def login():
  if request.method == 'POST':
    username = request.form.get('nam')
    return redirect(url_for('success', name=username or ''))
  else:
    username = request.args.get('nam')
    return redirect(url_for('success', name=username or ''))


if __name__ == "__main__":
  app.run(debug=True)