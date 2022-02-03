from flask import Flask, render_template, request
from resources.feedback import FeedBack
from send_email import send_email

#'sqlite:///lexus.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/lexus'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


@app.before_first_request   
def create_db():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer  = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or dealer =='':
            return render_template('index.html', message='Please enter required fields')
        
        if db.session.query(FeedBack).filter(FeedBack.customer == customer).count() == 0:
            data = FeedBack(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_email(customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have alredy submitted feedback')


if __name__ == '__main__':
    from database import db
    db.init_app(app)
    app.run(debug=True)