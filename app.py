# from flask import Flask
# app  = Flask(__name__) # __name__ tells the program that all the dependencies you need are available here


# @app.route("/")   # Decorator

# def hello_world():
#     return "Hello ck "

# @app.route("/welcome")
# def welcome():   #Use the different function name for 2nd function 
#     return "Welcome my youtube channels"

# if __name__ == '__main__':
#      app.run(debug = True)

# # msg = "ello worlf"

# # print(msg)
# # print("Pleade subbcdsna dmfsmdnfmsa,dm")




### 3rd Video
## Building Url Dynamically
## Variable Rules and URL Building

from flask import Flask ,redirect,url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome Route class"

@app.route("/failed/<int:score>")
def failed(score):
    return f"Your failed marks are {score}"    


@app.route("/result/<int:marks>")
def result(marks):
    if marks >= 50:
        return f"The person is passed with : {marks}"
    else:

        return redirect(url_for("failed" ,score = marks))
   


app.run(debug = True)    