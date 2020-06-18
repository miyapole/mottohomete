import sqlite3
#これでSQliteが使えるよ

#flaskからimpotrしてflaskを使えるようにするYO
from flask import Flask,render_template, request, redirect ,session,url_for

#appって名前でflaskアプリを作っていくよ〜
app = Flask(__name__)

#なんかsessionで使うやつ
app.secret_key = "sunabaco"

@app.route("/")
def helloworld():
    return "Hello World."


@app.errorhandler(404)
def notfound(code):
    return "404です。月に代わってお仕置きよ！！(CV:三石琴乃)"




if __name__ == "__main__":
    #Flaskが持っている共用サーバを実行します
    app.run(debug=True)
