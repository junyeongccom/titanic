from flask import Flask, render_template
from com.junyeongc.models.titanic.titanic_controller import Controller
from com.junyeongc.models.matjib.matjib_controller import Matjibcontroller

app = Flask(__name__)

@app.route('/')
def index():
    controller = Controller()
    controller.modelling('train.csv','test.csv')
    controller = Matjibcontroller()
    controller.modelling('matjib.csv')
    return render_template("/index.html")


if __name__ == '__main__':
    app.run(debug=True)
