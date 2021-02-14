import os
import json

from dotenv import load_dotenv
from flask import Flask, request, abort, Response

from fcm import FcmIntegration

# Load environment variables
load_dotenv('.env')

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

# Initialize Firebase app
default_app = FcmIntegration().initalize_firebase_app()


@app.route('/single_push', methods=['POST'])
def send_single_push():
    if (
        not 'X-API-KEY' in request.headers or
        request.headers['X-API-KEY'] != app.config['CLIENT_API_KEY']
    ):
        abort(400)
    
    title = request.form['title']
    body = request.form['body']
    token = request.form['token']
    
    data = None
    if request.form.get('data'):
        data = json.loads(request.form.get('data'))
    
    FcmIntegration().send_to_token(
        token=token,
        title=title,
        body=body,
        data=data
    )
    return Response(status=204)


@app.route('/multicast_push', methods=['POST'])
def send_multicast_push():
    
    if (
        not 'X-API-KEY' in request.headers or
        request.headers['X-API-KEY'] != app.config['CLIENT_API_KEY']
    ):
        abort(400)

    title = request.form['title']
    body = request.form['body']
    tokens = request.form.getlist('tokens')

    data = None
    if request.form.get('data'):
        data = json.loads(request.form.get('data'))
    
    FcmIntegration().send_multicast(
        registration_tokens=tokens,
        title=title,
        body=body,
        data=data,
    )
    return Response(status=204)


@app.route('/topic_push', methods=['POST'])
def send_topic_push():
    if not 'X-API-KEY' in request.headers or request.headers['X-API-KEY'] != app.config['CLIENT_API_KEY']:
        abort(400)

    title = request.form['title']
    body = request.form['body']
    topic = request.form['topic']
    FcmIntegration().send_to_topic(topic=topic, title=title, body=body)
    return Response(status=204)
