from flask import *
app = Flask(__name__)

# @app.route("/")
# def hello():
#     test = 100
#     return "Hello World"

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template("call.html", Kaito="お電話ありがとうございます。ヤマトシステム開発でございます")
    elif request.method == 'POST':
        TO = request.form['to']
        FROMS = request.form['froms']
        YOKEN = request.form['yoken']
        
        if TO and FROMS and YOKEN:
            return render_template("call.html", Kaito=f"それでは{TO}に取り次ぎますのでお待ちください<br><br>(取次後)<br>お疲れ様です。運用技術部の明石です。(お疲れ様です)ただいま、{FROMS}さまより、{YOKEN}でお電話をいただいておりますがこちらおつなぎしてもよろしいでしょうか<br>承知いたしました。それではおつなぎいたします。", to=TO, froms=FROMS, yoken=YOKEN)
        
        if TO and FROMS:
            return render_template("call.html", Kaito="恐れ入りますがご用件をお伺いしてもよろしいでしょうか", to=TO, froms=FROMS)
        
        if TO:
            return render_template("call.html", Kaito="恐れ入りますが(再度)お名前をお伺いしてもよろしいでしょうか", to=TO)
        
        if FROMS:
            return render_template("call.html", Kaito="", froms=FROMS)
        
    return render_template("call.html", Kaito="error")

@app.route("/hello/<whom>")
def hello(whom):
    return render_template("hello.html", whom=whom)


if __name__ == "__main__":
    app.run(debug=False, port=8080)