# Singer Search Server
This is the web server backend. Developed using flask. 
## Setup Server
1. Install [Python3](https://www.python.org/downloads/).
2. Create virtual environment.
    > python3 -m venv venv
3. Activate virtual environment.
    > . venv/bin/activate
4. Install requirements.
    > pip install -r requirements.txt

## Setup Elasticsearch
1. Install [Elasticsearch](https://www.elastic.co/elasticsearch/).
2. Install [ICU Analysis Plugin](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html).
3. Start Elasticsearch.
4. Add singer data to Elasticsearch.
    > python3 create_index.py

## Run Server
1. Activate virtual environment.
    > . venv/bin/activate
2. Run server.
    > flask run
3. Navigate to [http://localhost:5000/](http://localhost:5000/)
