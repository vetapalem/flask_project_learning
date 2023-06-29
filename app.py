from flask import Flask,request,render_template,jsonify,redirect,url_for,session
import requests as rq, os as oo


app=Flask(__name__)
app.secret_key='jinja'

@app.route('/')
def mom():
    return f'<h1>{"nothing"}</h1>'

@app.route('/dady')
def dady():
    if 'input' in session:
        return f'<h1>{session["input"]}</h1>'
    else:
        return "<p>noti</p>"

@app.route('/<value>')
def home(value):
    da={
        'q':value,
        "apikey":oo.environ['ne_key'],
        "language":"en",
        # 'country':'in', #country is not working

    }
    with rq.get(url=r'https://newsapi.org/v2/everything', params=da) as mk:
        
        return render_template('main1.html',
                               code=mk.json(),
                               title=value
                               )



@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == 'POST':

        print(request.form)
        session['input']=request.form['typ']

        return redirect(url_for('dady'))
        
        # return redirect(url_for('home',value=request.form['typ']))
    elif request.method == 'GET':
        return render_template('main.html')

@app.route('/logout')
def logout():
    if 'input' in session:
        session.pop('input')
        return '<p>nill</p>'
    else:
        return "<h1>logout...</h1>"
    


with app.test_request_context() :
    print(url_for('dady',next='/'))
    print(url_for('mom'))
    print(url_for('home',value="single",next='/'))
    print(url_for('login',next='/'))
    print(url_for('logout',next='/'))
        




if __name__ == "__main__":
    app.run(debug=True)