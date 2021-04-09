from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key= 'password12345678'

@app.route('/')
def ninja_gold():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def submit_form():
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)