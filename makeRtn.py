from flask import *
from loaddata import *

def isGet(request):
    if request.method =='GET':
        return True
    
    return False

def isPost(request):
    if request.method =='POST':
        return True
    
    return False

def makeRtnTemplate(request):
    if isGet(request):
        return render_template("call.html", Kaito="お電話ありがとうございます。ヤマトシステム開発でございます")
    
    if isPost(request):
        TO = request.form['to']
        FROMC = request.form['fromCompany']
        FROMH = request.form['fromHuman']
        FROM = FROMC and FROMH
        REQUIREMENT = request.form['requirement']
        
        if TO and FROM and REQUIREMENT:
            return render_template("call.html", 
                                   Kaito=rtnTFR(TO, FROMC, FROMH, REQUIREMENT), to=TO,
                                   fromCompany=FROMC,
                                   fromHuman=FROMH,
                                   requirement=REQUIREMENT,
                                   showButton=True
                                   )
        
        if TO and FROM:
            return render_template("call.html", 
                                   Kaito=rtnTF(),
                                   to=TO,
                                   fromCompany=FROMC,
                                   fromHuman=FROMH,
                                   )
            
        if TO:
            return render_template("call.html", 
                                   Kaito=rtnT(),
                                   to=TO
                                   )
        if FROM:
            return render_template("call.html", 
                                   Kaito=rtnF(),
                                   fromCompany=FROMC,
                                   fromHuman=FROMH,
                                   )
    
    return "error"
    
