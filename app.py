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

    name = request.form.get("name")
    homete1 = request.form.get("homete1")
    homete2 = request.form.get("homete2")
    homete3 = request.form.get("homete3")
    conn = sqlite3.connect('homete.db')
    c = conn.cursor()
    c.execute("insert into user_id values(null,?,?,?,?)", (name,homete1,homete2,homete3))

    conn.commit()
    conn.close()
    print(name,homete1,homete2,homete3)
    return redirect('/result')

@app.route('/result' ,methods=['GET'])
def result():
    
    conn = sqlite3.connect('homete.db')
    c = conn.cursor()
    # p1 = request.form.get("level")
    # p2 = request.form.get("level")
    # p3 = request.form.get("level")

    c.execute("SELECT small_word FROM small ORDER BY RANDOM()")
    p1 = c.fetchone()
    c.execute("SELECT medium_word FROM medium ORDER BY RANDOM()")
    p2 = c.fetchone()
    c.execute("SELECT large_word FROM large ORDER BY RANDOM()")
    p3 = c.fetchone()

    print (p1)
    print (p2)
    print (p3)

    conn.commit()
    conn.close()
    
    return "結果ページにいくよ"




@app.errorhandler(404)
def notfound(code):
    return "404です。月に代わってお仕置きよ！！(CV:三石琴乃)"




if __name__ == "__main__":
    #Flaskが持っている共用サーバを実行します
    app.run(debug=True)
