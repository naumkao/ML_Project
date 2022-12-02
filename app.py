import flask
from flask import render_template
import pickle
#import sklearn
#from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeRegressor
#from sklearn.ensemble import GradientBoostingRegressor
#from sklearn.multioutput import MultiOutputRegressor

app = flask.Flask(__name__, template_folder = 'templates')
@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open ('multiout_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)
        
        X_IW = float(flask.request.form['IW'])
        X_IF = float(flask.request.form['IF'])
        X_VW = float(flask.request.form['VW'])
        X_FP = float(flask.request.form['FP'])
        X = ['X_IW', 'X_IF', 'X_VW', 'X_FP']
        y_pred = loaded_model.predict([[X]])

        return render_template('main.html', result = y_pred)

if __name__ == '__main__':
    app.run(debug=False)
    #    ['IW','IF','VW','FP']