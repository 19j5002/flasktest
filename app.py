import sys
sys.path.append("I://開発環境/python/flasktest/Lib/site-packages")

from makeRtn import *
app = Flask(__name__)
# @app.route("/")
# def hello():
#     test = 100
#     return "Hello World"

@app.route("/", methods=['GET', 'POST'])
def main():
    template = makeRtnTemplate(request)
    
    return template

@app.route("/hello/<whom>")
def hello(whom):
    return render_template("hello.html", whom=whom)


if __name__ == "__main__":
    app.run(debug=True, port=8080)