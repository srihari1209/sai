from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/computerNetwork')
def computerNetwork():
    return render_template("computerNetwork.html")


@app.route('/unifiedCommunications')
def unifiedCommunications():
    return render_template("unifiedCommunications.html")


@app.route('/videoConference')
def videoConference():
    return render_template("videoConferance.html")


@app.route('/IPTelephony')
def IPTelephony():
    return render_template("IPTelephony.html")


@app.route('/computerHardware')
def computerHardware():
    return render_template("computerHardware.html")


@app.route('/CCTV')
def CCTV():
    return render_template("CCTV.html")


@app.route('/sendMail', methods=['GET', 'POST'])
def sendMail():
    if request.method == "POST":
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
