from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app. route('/blog/<int:postID>')
def show_blog(postID):
  return 'Blog Number %d' %postID

@app.route('/rev/<float:revNo>')
def revision_number (revNo):
  return 'Revision Number %f' %revNo

@app.route('/flask/<name>')
def hello_flask(name):
  return name

@app. route('/python/')
def hello_python():
  return 'Hello Python'

if __name__ == "__main__":
  app.run(debug=True)