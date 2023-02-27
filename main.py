from flask import Flask, request, render_template, redirect, url_for, session
from models import db, User, Role


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pw.db"
app.config['SECRET_KEY'] = 'secret_key'
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")
  
@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/404")
def error_404():
    return render_template("404.html")
    
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/profile")
def profile():
    if 'user' in session:
        # Get the username from the session
        username = session['user']
        # Query the database to get the user's profile information
        user = User.query.filter_by(username=username).first()

        return render_template('profile.html', user=user)
    else:
        return render_template('login-register.html')

@app.route('/logout')
def logout():
    # Remove the user from the session
    session.pop('user', None)
    return redirect(url_for('profile'))

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/shop-single")
def shop_single():
    return render_template("shop-single.html")
    

@app.route("/login-form", methods=['POST'])
def login_form():
    # Get the username and password from the form
    username = request.form['login-form-username']
    password = request.form['login-form-password']

    # Check if the username and password are correct
    user_form = User.query.filter_by(username=username, password=password).first()
    if user_form:
        # Create a session
            session['user'] = user_form.username
            return redirect(url_for('index'))
    else:
        # Login failed
        return redirect(url_for('error_404'))
    

@app.route("/register-form", methods=['POST'])
def register_form():
    # Get the username and password from the form
    username = request.form['register-form-username']
    password = request.form['register-form-password']
    email = request.form['register-form-email']
    first_name = request.form['register-form-firstname']
    last_name = request.form['register-form-lastname']
    phone = request.form['register-form-phone']
    morada = request.form['register-form-morada']

    
    role = Role(role="Cliente")
    register = User(username=username, password=password, email=email, firstname=first_name,lastname=last_name, phone=phone,morada=morada, role=role)
    

    db.session.add_all([register, role])
    db.session.commit()

    
    if register:
        session['user'] = register.username
        return redirect(url_for('index'))
    else:
        # Login failed
        return redirect(url_for('error_404'))




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)