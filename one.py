##########################
# SYNTAX OF FLASK 
##########################

# from flask import Flask

# app = Flask(__name__)  ### WSGI app

# @app.route('/') # API # Default API
# def one():
#     return "API SUCCESS"


# if __name__ == '__main__':
#     app.run()



# @app.route(url,options) 
# e.g. url == '/' or '/predict' or '/app/result'
# options == rules to handle the request 

###################################
# url for routing 
###################################
# from flask import Flask

# app = Flask(__name__)  ### WSGI app

# @app.route('/') # API # Default API
# def one():
#     return "API SUCCESS"

# @app.route('/predict') 
# def predict():
#     return "Predict API"

# @app.route('/result') 
# def result():
#     return "Result API"

# @app.route('/app/data') 
# def data():
#     return "app & data API"

# if __name__ == '__main__':
#     app.run()

##############################

# app.run(host,port,debug,options)

#     host = deafult >> 127.0.0.1 (localhost) . set to '0.0.0.0' for deployment
#     port = 5000, e.g aws >> 8080
#     debug = Default False, if set True the provide debug information on consle 


#######################
# app.run arguments 
#######################

# from flask import Flask

# app = Flask(__name__)  ### WSGI app

# @app.route('/') # API # Default API
# def one():
#     return "API SUCCESS"


# if __name__ == '__main__':
#     app.run(host = '127.0.0.1' , port = 5000 , debug=False)

###########################################

# from flask import Flask

# app = Flask(__name__)  ### WSGI app

# @app.route('/') # API # Default API
# def one():
#     return "API SUCCESS"


# if __name__ == '__main__':
#     app.run(host = 'localhost' , port = 5000 , debug=False)

############################################

# from flask import Flask

# app = Flask(__name__)  ### WSGI app

# @app.route('/') # API # Default API
# def one():
#     return "API SUCCESS"


# if __name__ == '__main__':
#     app.run(host = '127.67.123.1' , port = 8080 , debug=False)

########################################

from flask import Flask

app = Flask(__name__)  ### WSGI app
@app.route('/') # API # Default API
def index():
    return "API SUCCESS"


if __name__ == '__main__':
    app.run(host = '127.0.0.1' , port = 8080 , debug=True)
