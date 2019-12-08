from flask import Flask, render_template, request, jsonify
import fonctions

app = Flask(__name__)
app.config['SECRET_KEY']='fdsfsdfesfezfe'

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html')

@app.route('/', methods=['GET','POST'])
#JS appel cette route
def get_user_input():
    if request.method =='POST':
        user_input = request.form['user_input']
        returned_response = fonctions.parserKiller(user_input)
        return render_template('home.html')
    else :
        return render_template('home.html')

if  __name__== '__main__':
    app.run(debug=True)


