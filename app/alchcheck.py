from flask import Flask, render_template, request

app = Flask(__name__)


def performcalc(v1,v2,p1,p2):
    p1 = float(p1)/100
    p2 = float(p2)/100
    v1 = float(v1)
    v2 = float(v2)
    print(p1,p2)
    result = (v1*p1+v2*p2) / (v1+v2)
    print(result)
    return result*100



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calcresponse():
    v1 = request.form['v1']
    v2 = request.form['v2']
    p1 = request.form['p1']
    p2 = request.form['p2']
    result = performcalc(v1,v2,p1,p2)
    return render_template('index.html',result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
