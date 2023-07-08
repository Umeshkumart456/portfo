from flask import Flask, render_template,url_for, request, redirect
import csv
app = Flask(__name__)



@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a')as database:
        name=data["name"]
        number=data["number"]
        email=data["email"]
        message=data["message"]
        file=database.write(f'\n{name},{number},{email},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a',newline='')as database2:
        name=data["name"]
        number=data["number"]
        email=data["email"]
        message=data["message"]
        csv_writer=csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,number,email,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again.!'

'''
@app.route('/projects.html')
def my_projects():
    return render_template('projects.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')
'''