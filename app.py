from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with strong key

# Email configuration (Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'josephkidenye@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'   # Use App Password
app.config['MAIL_DEFAULT_SENDER'] = 'josephkidenye@gmail.com'

mail = Mail(app)

def send_email(recipient, subject, body):
    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/practice-areas')
def practice_areas():
    return render_template('practice-area.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        date = request.form.get('date')
        time = request.form.get('time')
        message = request.form.get('message')
        body = f"New Consultation Booking:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nTime: {time}\nMessage: {message}"
        try:
            send_email('josephkidenye@gmail.com', f'Booking from {name}', body)
            flash('Your consultation request has been sent. We will confirm within 24 hours.', 'success')
        except Exception as e:
            flash('There was an error. Please try again later.', 'danger')
        return redirect(url_for('booking'))
    return render_template('booking.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        body = f"Contact Message:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        try:
            send_email('josephkidenye@gmail.com', f'Contact from {name}', body)
            flash('Your message has been sent. We will get back to you soon.', 'success')
        except Exception as e:
            flash('Failed to send. Please try again.', 'danger')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)