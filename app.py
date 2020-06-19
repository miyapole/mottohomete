import sqlite3
#これでSQliteが使えるよ

#flaskからimpotrしてflaskを使えるようにするYO
from flask import Flask,render_template, request, redirect ,session,url_for

#appって名前でflaskアプリを作っていくよ〜
app = Flask(__name__)

#なんかsessionで使うやつ
app.secret_key = "sunabaco"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login' ,methods=["POST"])
def login():
    # user_id = session['user_id']

    comment = request.form.get("comment")
    conn = sqlite3.connect('homete.db')
    c = conn.cursor()

    conn.commit()
    conn.close()
    return redirect('/bbs')

@app.errorhandler(404)
def notfound(code):
    return "404です。月に代わってお仕置きよ！！(CV:三石琴乃)"




if __name__ == "__main__":
    #Flaskが持っている共用サーバを実行します
    app.run(debug=True)
