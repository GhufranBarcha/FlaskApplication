
### Jinja 2 template engine

'''
{% ..... %} statements 
{{....}} expression
{#  .....   #} this is for comment

'''



from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# Set the path to the template folder
app.template_folder = 'D:/Flask/FlaskApplication/templatess'

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/succes/<int:score>")
def succes(score):
    return render_template("result.html" , result = ["pass" ,score])

@app.route("/failed/<int:score>")
def failed(score):
    return render_template("result.html" , result = ["failed" ,score])    

@app.route("/result/<int:marks>")
def result(marks):
    
    if marks >= 50:
        
        return redirect(url_for("succes", score=marks))
    else:
        return redirect(url_for("failed", score=marks))

@app.route('/submit', methods=["POST", "GET"])
def submit():
    totalScore = 0
    if request.method == 'POST':
        science = float(request.form["science"])
        math = float(request.form["math"])
        english = float(request.form["english"])
        CVT = float(request.form["CVT"])
        totalScore = (science + math + english + CVT) / 4
    res = "result"
    return redirect(url_for(res, marks=totalScore))

if __name__ == "__main__":
    app.run(debug=True)