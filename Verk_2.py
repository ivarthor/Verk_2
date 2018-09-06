from sys import argv
import bottle
from bottle import *

@route("/")
def index():
    return"""
    <h2> Verkefni 2 </h2>
    <p><a href=" /A"> Lidur A </a></p>
    <p><a href=" /B"> Lidur B</a></p>
    """

@route("/A")
def a():
    return """
    <h2>Verkefni 2 - lidur A</h2>
    <a href ="/sida/1">Sida 1.</a>
    <a href ="/sida/2">Sida 2.</a>
    <a href ="/sida/3">Sida 3.</a>
    <a href ="/">Forsíða</a>
    """

@route("/B")
def b():
    return """
    <h2>Verkefni 2 - lidur B</h2>
    <p>Þetta eru myndir</p>
    <a href ='/sida2?bokstafur=a'><img src = "myndir/a.png"></a>
    <a href ='/sida2?bokstafur=b'><img src = "myndir/b.png"></a>
    <a href ='/sida2?bokstafur=c'><img src = "myndir/c.png"></a>
    <a href ="/">Forsíða</a>
    """

@route("/sida/<id>")
def page(id):
    if id == "1":
        return 'Sida 1<br><a href ="/A">Til baka</a>'
    elif id == "2":
        return 'Sida 2<br><a href ="/A">Til baka</a>'
    elif id == "3":
        return 'Sida 3<br><a href ="/A">Til baka</a>'
    else:
        abort(404, "<h2> Þessi síða finnst ekki</h2>")


@route("/sida2")
def page2():
    l = request.query.bokstafur
    if l == "a":
        return 'Mynd eitt<br><a href ="/B">Til baka</a>'
    elif l == "b":
        return 'Mynd tvö<br><a href ="/B">Til baka</a>'
    elif l == "c":
        return 'Mynd þrjú<br><a href ="/B">Til baka</a>'


@route("/myndir/<pics>")
def static_skra(pics):
    return static_file(pics,root="myndir")

@error(404)
def error404(error):
    return "ERROR"

#bottle.run(host="localhost", port=8080, debug=True)
bottle.run(host='0.0.0.0', port=argv[1])