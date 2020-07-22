import helper
import requests
from flask import Flask, request, Response, render_template, redirect 
import json
import time
from requests import get, post
import urllib
import os

subscription_key = os.environ['COGNITIVE_SERVICE_KEY']
endpoint= os.environ['COMPUTER_VISION_ENDPOINT']
text_recognition_url = endpoint + "/vision/v3.0/read/analyze"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/comment/new', methods=['POST'])
def add_comment():
    # Get comment from the POST body
    if request.method == "POST":
        
        req = request.form.to_dict()
        comment = req["comment"]
        text = get_text_from_url(comment)
        return Response("<p>" + text + "</p>") 
        # return render_template("/index.html")

    
    req_data = request.get_json()
    comment = req_data['comment']

    # Add comment to the list
    res_data = helper.add_to_list(comment)

    # Return error if comment not added
    if res_data is None:
        response = Response("{'error': 'comment not added - " + comment + "'}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return render_template("index.html")

def get_text_from_url(url_image):
    
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    data = {'url': url_image}
    send_response = requests.post(text_recognition_url, headers=headers, json=data)
    send_response.raise_for_status()

    # The recognized text isn't immediately available, so poll to wait for completion.
    analysis = {}
    poll = True
    while (poll):
        response_final = requests.get(send_response.headers["Operation-Location"], headers=headers)
        analysis = response_final.json()
        
        time.sleep(1)
        if ("analyzeResult" in analysis):
            poll = False
        if ("status" in analysis and analysis['status'] == 'failed'):
            poll = False

    text_ocr=[]
    for index, line in enumerate(analysis['analyzeResult']['readResults'][0]['lines']):
        text_ocr.append(line['text'])

    string=' '.join(text_ocr)

    return string
    
