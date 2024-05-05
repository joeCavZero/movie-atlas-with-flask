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
        return redirect( '/search/{}'.format( db.getRandomId() ) )
    
    @app.route('/search/<movie>' , methods=['GET'])
    def find_movie(movie):
        
        return jsonify( db.getMovieById(movie) )
    
    app.run( port = PORT , debug = True )
    




if __name__ == '__main__':
    main()