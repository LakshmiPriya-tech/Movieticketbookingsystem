from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('/list', methods=('GET', 'POST'))
def register():
    db = get_db()
    if request.method == 'GET':
        # Fetch movies from db and render movies_list.html template
        error = None
        movies_from_db = db.execute(
            'SELECT * FROM movies'
        ).fetchall()
        return render_template("movies/movies_list.html", movies=movies_from_db)
    elif request.method == 'POST':
        selected_movie_id = request.form['selected_movie']
        m = db.execute(
            'SELECT * from movies WHERE ID = ?', (selected_movie_id,)
            ).fetchone()
        return "That's great! You have booked your ticket for the movie: " + str(m['movie_name']) + " in the theatre " + m['theatre_name']
