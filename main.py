from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)



@app.route("/main.css")
def index():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip_address = request.environ['REMOTE_ADDR']
    else:
        ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    print("****************")
    print("IP Address:", ip_address)
    print("User Agent:", request.headers.get('User-Agent'))
    print("Accept:", request.headers.get('Accept'))
    print("Accept-Language:", request.headers.get('Accept-Language'))
    return render_template("main.css")



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=443)
