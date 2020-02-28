import os
import pickle
from flask import current_app, request, jsonify, render_template
from app import create_app
from app.views import views_bp
from app.forms import ReivewTextForm

ML_DIR = 'ML_DIR'
SENTIMENT_MAP = {'Negative':0, 'Positive':1, 'Compliant':2}

@views_bp.route("/")
def index():
    form = ReivewTextForm()
    return render_template('review.html', form=form)

@views_bp.route("/postReview", methods=['POST'])
def post_review():
    # data = request.form['review_text']
    review_text = request.form['review_text']
    model_file = os.path.join(current_app.config[ML_DIR], 'mnb_classifier.pickle')
    tfidf_file = os.path.join(current_app.config[ML_DIR], 'tfidf.pickle')

    with open(model_file, 'rb') as data:
        model = pickle.load(data)
    with open(tfidf_file, 'rb') as data:
        tfidf = pickle.load(data)
    
    sentiment_id = model.predict(tfidf.transform([review_text]))
    return jsonify(sentiment=get_sentiment(sentiment_id))

def get_sentiment(sentiment_id):
    for sentiment, id in SENTIMENT_MAP.items():
        if id == sentiment_id:
            return sentiment