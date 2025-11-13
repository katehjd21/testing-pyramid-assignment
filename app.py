from flask import Flask,render_template
from controllers.duty import DutyController
app = Flask(__name__)

@app.route('/')
def index():
    duty = DutyController().get_duty()
    return render_template("random_duty.html", duty=duty) 
    