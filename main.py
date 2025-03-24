from flask import Flask, render_template, request
import random
import time

app = Flask(__name__)
lista=["🍒", "🍋", "🔔", "🍉", "⭐", "7️⃣", "🎰"]

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():

    a=random.choice(lista)

    b=random.choice(lista)

    c=random.choice(lista)
    
    time.sleep(2)    
    
    if a==b and b==c:
        win= True
    else:
        win= False
    return render_template('vastaus.html', bet=int(request.args['money']), a=a, b=b, c=c, win=win)













if __name__=='__main__':
    app.run(debug=True)
    
    
    
    
    
#<h2>Your account balance is {{balance}} dollars.</h2>