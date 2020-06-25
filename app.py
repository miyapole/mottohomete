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

# @app.route('/form_post', methods=['POST'])
# def form_post():
#     print(request.form.get('level', None))
#     return redirect(url_for('login'))

@app.route('/login' ,methods=["GET", "POST"])
def login():
    # user_id = session['user_id']

    name = request.form.get("name")
    homete1 = request.form.get("homete1")
    homete2 = request.form.get("homete2")
    homete3 = request.form.get("homete3")
    conn = sqlite3.connect('homete.db')
    c = conn.cursor()
    c.execute("insert into user_id values(null,?,?,?,?)", (name,homete1,homete2,homete3))
    level = request.form.get("level")
    
    # if level == "普通の褒め":
    #     c.execute("select small_word from smaill where id = RANDOM()")
    #     p = c.fetchone()
    # elif level == "まあまあの褒め":
    #     c.execute("select midium_word from midium where id = RANDOM()")
    #     p = c.fetchone()
    # else: 
    #     c.execute("select large_word from large where id = RANDOM()")
    #     p = c.fetchone()


    c.execute("SELECT small_word FROM small ORDER BY  RANDOM()")
    p1 = c.fetchone()
    c.execute("SELECT medium_word FROM medium ORDER BY RANDOM()")
    p2 = c.fetchone()
    c.execute("SELECT large_word FROM large ORDER BY RANDOM()")
    p3 = c.fetchone()

    conn.commit()
    conn.close()

    if level =="普通の褒め":
        p=p1
    elif level =="まあまあの褒め":
        p=p2
    else:
        p=p3

    p = str(p).replace('name', name)
    p = str(p).replace('homete1', homete1)
    p = str(p).replace('homete2', homete2)
    p = str(p).replace('homete3', homete3)

    return render_template("result.html",p=p)


@app.errorhandler(404)
def notfound(code):
    return "404です。月に代わってお仕置きよ！！(CV:三石琴乃)"




if __name__ == "__main__":
    #Flaskが持っている共用サーバを実行します
    app.run(debug=True)
