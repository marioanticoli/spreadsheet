from flask import render_template
from app.main import bp

@bp.route('/')
def base():
    return render_template('index.html')
