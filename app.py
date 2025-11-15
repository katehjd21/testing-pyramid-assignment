from flask import Flask,render_template
from controllers.duty_controller import DutyController
from controllers.coin_controller import CoinController

app = Flask(__name__)

@app.route('/')
def landing_page():
    coins = CoinController().fetch_all_coins()
    return render_template("coins.html", coins=coins)

@app.route('/automate')
def automate_page():
    duty = DutyController().fetch_duty()
    return render_template("automate_duties.html", duty=duty) 
    