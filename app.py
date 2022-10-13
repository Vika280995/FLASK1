from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'
db =SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    intro = db.Column(db.String(300),nullable=False)
    text = db.Column(db.Text,nullable=False)
    notes = db.Column(db.String(500))
    data = db.Column(db.DateTime,default=datetime.utcnow)


    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")



@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/newpage')
def newpage():
    return render_template("newpage.html")

@app.route('/create_article',methods=['POST','GET'])
def create_article():
    if request.method=="POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']


        artile = Article(title=title,intro=intro,text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "При добавлении статьи произошла ошибка"
    else:
        return render_template("create_article.html")

#@app.route('/user/<string:name>/<int:id>')
#def user(name,id):
 #   return 'User page'+name+"-"+ str(id)


if __name__ == '__main__':
   app.run(debug=True)


