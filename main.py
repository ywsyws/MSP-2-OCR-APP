import helper
import requests
from flask import Flask, request, Response, render_template, redirect 
import json
import time
from requests import get, post
import urllib
import os

subscription_key = "73ce4df610864335bd26c971426cb6f6"
vision_base_url = "https://uksouth.api.cognitive.microsoft.com/vision/v2.0/"
text_recognition_url = vision_base_url + "recognizeText"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/comment/new', methods=['POST'])
def add_comment():
    # Get comment from the POST body
    if request.method == "POST":
        
        req     = request.form.to_dict()
        comment = req["comment"] 
        text    = get_text_from_url(comment)
        return Response("<p>" + text + "</p>") 
        # return render_template("/index.html")

    
    req_data = request.get_json()
    comment  = req_data['comment'] 

    # Add comment to the list
    res_data = helper.add_to_list(comment) ### comment = url

    # Return error if comment not added
    if res_data is None:
        response = Response("{'error': 'comment not added - " + comment + "'}", status=400 , mimetype='application/json')
        return response

    # Return response
    # response = Response(json.dumps(res_data), mimetype='application/json')

    # return render_template("index.html")

def get_text_from_url(url_image):

    headers  = {'Ocp-Apim-Subscription-Key': subscription_key}
    params   = {'mode' : 'Handwritten'}
    data     = {'url': url_image}
    response = requests.post(text_recognition_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    
    analysis = {}

    while not "recognitionResult" in analysis:
        response_final = requests.get(response.headers["Operation-Location"], headers=headers)
        analysis       = response_final.json()
        time.sleep(1)
    
    texts = [line["text"] for line in analysis["recognitionResult"]["lines"]]
    
    text_ocr=[]
    for text in texts:
        text_ocr.append(text)
    
    string=' '.join(text_ocr)

    return string
    
