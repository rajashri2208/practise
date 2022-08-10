from flask import Flask

app=Flask(__name__)
@app.route('/')
def one():
    return "API Success"

if __name__='__main__':
    app.run()
