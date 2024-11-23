import connexion
from flask import Flask, render_template
from db import db, ma  
import api  
from data_loader import load_data  

connexion_app = connexion.App(__name__, specification_dir='./')
app = connexion_app.app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()
    load_data(app)  

@app.route('/')
def home():
    return render_template('home.html')

connexion_app.add_api('swagger.yml')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

