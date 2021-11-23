#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from elasticsearch import Elasticsearch
import config

app = Flask(__name__)
es = Elasticsearch([config.es_base])

@app.route('/')
def index():
    return render_template('index.html', app_data=[])

@app.route('/search/<term>')
def about(term: str):
    result = es.search(
        index = config.es_index,
        body={
            "query": {
                "multi_match" : {
                    "query":    "කලා සූර",
                    "fields": ["name", "info", "from", "gender", "intro", "description", "type", "birth", "is", "age", "death", "was", "star sign", "instruments:", "profiles", "family", "a.k.a.", "education", "known for", "residence", "genre:", "politics", "stats", "notable works"]
                }
            }
        }
    )
    return result



if __name__ == '__main__':
    app.run()