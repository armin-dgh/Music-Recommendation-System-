from flask import Flask, request, render_template
import numpy as np 
import pickle
import pandas as pd



#loading model 

df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))



def recommendation(song_df):
    matches = df[df['song'] == song_df]
    if matches.empty:
        return []
    idx = matches.index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

    songs = [df.iloc[m_id[0]].song  for m_id in distances[1:21]]
    return songs



# flask app
app = Flask(__name__)

# path 
@app.route('/')
def index():
    names = list(df['song'].values)
    return render_template('index.html',name = names)

@app.route('/recom', methods=["POST"])
def mysong():
    user_song = request.form['names']
    songs = recommendation(user_song)

    return render_template('index.html',songs=songs)



# python
if __name__ == "__main__":
    app.run(debug=True)