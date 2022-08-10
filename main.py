from flask import Flask

app=Flask(__name__)
@app.route('/')
def one():
    return "API Success"


print("hello all i am using git")

if __name__='__main__':
    app.run()
