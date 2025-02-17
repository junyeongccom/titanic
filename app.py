from flask import Flask, render_template
from com.junyeongc.models.titanic.titanic_controller import TitanicController
from com.junyeongc.models.matjib.matjib_controller import Matjibcontroller

app = Flask(__name__)

@app.route('/')
def index():
    controller = TitanicController()
    controller.modelling('train.csv','test.csv')
    mcontroller = Matjibcontroller()
    mcontroller.modelling('matjib.csv')
    return render_template("/index.html")


if __name__ == '__main__':
    app.run(debug=True)
