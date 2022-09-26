import os
import os.path
from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
import imghdr
from flask_mail import Mail, Message
import secrets
from PIL import Image
from app import app, mail
from app.users.forms import ContactForm

users = Blueprint('users', __name__)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img', picture_fn)

    output_size = (1000, 1000)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@users.route('/', methods=['GET', 'POST'])
def contact():

    form = ContactForm()
    if request.method == "POST":

        msg = Message(f'message form {form.name.data}', sender='eorji452@gmail.com',
                      recipients=['worldwidesaah@gmail.com'])
        msg.body = f""" 
        Name : {form.name.data}
        Email : {form.email.data}
        Phone : {form.phone.data}
        Country : {form.country.data}
        City : {form.city.data}
        State : {form.state.data}
        Code : {form.code.data}
        Address : {form.address.data}
        Date ot birth : {form.date.data}
        Employment status : {form.employ.data}
        Education level : {form.education.data}
        Position applying : {form.position.data}
        Currently in UAE : {form.yes.data}
        Who informed you : {form.media.data}
        """

        mail.send(msg)
        flash('Thanks for being part of our community, we ll get back to you as soon as possible.', 'success')
        return redirect(url_for('users.thanks'))
    return render_template("contact.html", title='Register', form=form)


@users.route('/thanks')
def thanks():
    return render_template("thanks.html")








