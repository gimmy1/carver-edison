from flask import Blueprint, jsonify
from project.api.models import Tweet

tweets_blueprint = Blueprint('tweets', __name__)

@tweets_blueprint.route('/tweets/tweet', methods=['GET'])
def tweet_tweet():
    return jsonify({
        "tweet": "tweet"
    })

@tweets_blueprint.route('/tweets/<tweet_id>', methods=['GET'])
def get_single_tweet(tweet_id):
    """ Get single user details """
    response_object = {
        'message': 'Does not exist'
    }
    try:
        tweet = Tweet.query.filter_by(id=int(tweet_id)).first()
        if not tweet:
            return jsonify(response_object), 404
        else:
            response_object = {
                'id': tweet.id,
                'title': tweet.title,
                'name': tweet.name
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
    
@tweets_blueprint.route('/tweets/', methods=['GET'])
def get_all_tweets():
    """ Get all tweets """
    response_object = {
        'tweets': [tweet.to_json() for tweet in Tweet.query.all()]
    }
    return jsonify(response_object), 200

