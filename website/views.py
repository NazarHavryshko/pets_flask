from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def index():
    return render_template('index.html', user=current_user)


@views.route('/404', methods=['GET'])
def page404():
    return render_template('page404.html', user=current_user)


@views.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@views.route('/add', methods=['GET'])
@login_required
def add():
    return render_template('add.html', user=current_user)


@views.route('/sell', methods=['GET', 'POST'])
@login_required
def sell():
    if request.method == 'POST':
        print(request.form)

    return render_template('sell.html', user=current_user)


@views.route('/lost_found', methods=['GET', 'POST'])
@login_required
def lost_found():
    if request.method == 'POST':
        print(request.form)

    return render_template('lost__found.html', user=current_user)


@views.route('/in_good_hands', methods=['GET', 'POST'])
@login_required
def in_good_hands():
    if request.method == 'POST':
        print(request.form)

    return render_template('in_good_hands.html', user=current_user)


@views.route('/your_pet', methods=['GET', 'POST'])
@login_required
def your_pet():
    if request.method == 'POST':
        print(request.form)

    return render_template('your_pet.html', user=current_user)


@views.route('/find_pet', methods=['GET'])
def find_pet():
    return render_template('find_pet.html', user=current_user)



