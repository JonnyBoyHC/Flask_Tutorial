from flask import Flask, redirect, url_for, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def success():
  return 'Welcome !!!'

if __name__ == "__main__":
  app.run(debug=True)