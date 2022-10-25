from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,current_app
)
from werkzeug.security import check_password_hash, generate_password_hash
import json
from flaskr.db import get_db


bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('/seats', methods=['GET', 'POST'])
def seats():
    db=get_db()
    if request.method == 'GET':
        selectedmovie=request.args.get('selectedmovie')
        current_app.logger.info("Selected movie=%s", selectedmovie)
        s=db.execute('SELECT seats FROM movies WHERE ID = ?',(selectedmovie,)).fetchone()
        l1=json.loads(s['seats'])
        current_app.logger.info("Got from db: %s", s['seats'])
        return render_template("movies/seats.html", seat_numbers=l1 )


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
        return redirect(url_for('movies.seats'))


