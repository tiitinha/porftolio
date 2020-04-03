from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)

def write_to_file(data):
    with open('database.csv', 'a') as db:
        email = data["email"]
        message = data["text"]
        file = db.write(f'\n{email}, {message}')

def write_to_csv(data):
    with open('database.csv', 'a') as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db2, delimiter = ',', quotechar = '', quoting = csv.QUOTE_MINIMAL, newline='')
        csv_writer.writerow(email, subject, message)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return "something went wrong"