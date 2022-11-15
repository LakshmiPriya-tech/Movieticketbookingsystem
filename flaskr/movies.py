from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,current_app
)
from werkzeug.security import check_password_hash, generate_password_hash
import json
from flaskr.db import get_db


bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('/seats', methods=['GET', 'POST'])
def seats():
    current_app.logger.info("Current aruments: %s", str(request.args))
    db=get_db()
    selectedmovie=request.args.get('selectedmovie')
    if request.method == 'GET':
        s=db.execute('SELECT seats FROM movies WHERE ID = ?',(selectedmovie,)).fetchone()
        l=json.loads(s['seats'])
        def seats_for_html(l):
            l_1= db.execute('SELECT booked_seats FROM movies WHERE ID = ?',(selectedmovie))
            l_booked=json.loads(l_1['booked_seats'])
            l_all=l.extend(l_booked)
            d={}
            for i in l_all:
                if i in l_booked:
                    d[i]= True
                else:
                    d[i]= False
            return d,l_all
        map,l_seats=seats_for_html(l)
        return render_template("movies/seats.html", seat_numbers=l, mapping_dict=map, list_of_seats=l_seats)   

    elif request.method == 'POST':
        current_app.logger.info(str(request.form))
        selected_seats = request.form
        selected_seats_int=[]
        for i in selected_seats:
            i=int(i)
            selected_seats_int.append(i)
        s_db=db.execute('SELECT booked_seats FROM movies WHERE ID = ?',(selectedmovie)).fetchone()
        current_app.logger.info('seats from db: %s',str(s_db))
        if s_db['booked_seats'] == '':
            db.execute('UPDATE movies SET booked_seats = ? WHERE ID = ?',(json.dumps(selected_seats_int),selectedmovie))
        else:
            s_db1=json.loads(s_db['booked_seats'])
        #current_app.logger.info('seats from db: %s',s_db1)
            s_db1.extend(selected_seats_int)
            db.execute('UPDATE movies SET booked_seats = ? WHERE ID = ?',(json.dumps(s_db1),selectedmovie))
        db.commit()

        s1 = db.execute('SELECT seats FROM movies WHERE ID = ?',(selectedmovie,)).fetchone()
        l1 = json.loads(s1['seats'])
        for i in selected_seats_int:
            l1.remove(i)
        db.execute('UPDATE movies SET seats = ? WHERE ID = ?',(json.dumps(l1),selectedmovie,))
        db.commit()
        m=db.execute('SELECT movie_name FROM movies WHERE ID = ?',(selectedmovie)).fetchone()
        ss=json.dumps(selected_seats_int)
        current_app.logger.info('seats=%s',(str(ss)))
        return "You have booked seats "+ str(ss) +" for the movie "+ str(m['movie_name'])

        #current_app.logger.info("the selected seats are:%s",selected_seats)

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
        return redirect(url_for('movies.seats')+'?selectedmovie='+selected_movie_id)


