import helper
import requests
from flask import Flask, request, Response, render_template, redirect 
import json
import time
from requests import get, post
import urllib

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
    res_data = helper.add_to_list(comment) ### comment = url

    # Return error if comment not added
    if res_data is None:
        response = Response("{'error': 'comment not added - " + comment + "'}", status=400 , mimetype='application/json')
        return response

    # Return response
    # response = Response(json.dumps(res_data), mimetype='application/json')

    # return render_template("index.html")

def get_text_from_url(url_image):
            
    return "Fichier sauvegardé"
    
