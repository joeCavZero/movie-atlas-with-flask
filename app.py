from flask import Flask , request , render_template , jsonify , redirect
import pandas as pd

from config import *
from src.database import *

def main():
    app = Flask(__name__)

    db = database()
    
    @app.route('/' , methods=['GET'])
    def index():
        return render_template('index.html')
    
    @app.route('/random' , methods=['GET'])
    def random():
        return redirect( f'/movie/{ db.getRandomId() }' )
    
    @app.route('/movie/<id>' , methods=['GET'])
    def movie(id):
        return render_template('movie.html' , info= db.getMovieById( int(id) )  )#jsonify( db.getMovieById(int(movie) ) )
    

    @app.route('/search/<movie>' , methods=['GET'])
    def find_movie(movie:str):
        aux = db.getIdByTitle( movie )
        return redirect( f'/movie/{aux}')    

    app.run( port = PORT , debug = True )
    




if __name__ == '__main__':
    main()