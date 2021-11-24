#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify
from elasticsearch import Elasticsearch
import config

app = Flask(__name__)
es = Elasticsearch([config.es_base])

@app.route('/')
def index():
    return render_template('index.html', app_data=[])

@app.get('/search/<term>')
def about(term: str):
    result = es.search(
        index = config.es_index,
        body={
            "query": {
                "multi_match" : {
                    "query": term,
                    "fields": [
                        "name^2", 
                        "info", 
                        "from", 
                        "gender", 
                        "intro", 
                        "description^0.5", 
                        "type", 
                        "birth", 
                        "is", 
                        "age", 
                        "death", 
                        "was", 
                        "star sign", 
                        "instruments:", 
                        "profiles", 
                        "family", 
                        "a.k.a.^2", 
                        "education", 
                        "known for", 
                        "residence", 
                        "genre:", 
                        "politics", 
                        "stats", 
                        "notable works"
                    ]
                }
            }
        }
    )
    sources = [hit["_source"] for hit in result['hits']['hits']]
    return jsonify(sources)



if __name__ == '__main__':
    app.run()