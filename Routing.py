from flask import Flask

@app.route('/')
def success():
  return 'Welcome !!!'

if __name__ == "__main__":
  app.run(debug=True)