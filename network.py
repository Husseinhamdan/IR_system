from flask import Flask, request
from flask import jsonify

from model.Collection import Collection
from model.query import Query
from model.query_collection import Query_Collection
from services.matcher import Matcher

app =Flask(__name__)

query_file="dataset/cacm/query.text"
query_rel="dataset/cacm/qrels.text"
query_collection=Query_Collection(query_file,query_rel)
collection_cacm="dataset/cacm/cacm.all"
stopWord_cacm="dataset/cacm/common_words"
collection=Collection(collection_cacm,stopWord_cacm)
stopwords=collection._get_stop_word()
@app.route('/')
def hello_flask():
    return "hello hussein"


@app.route('/query_search', methods=['POST'])
def json_example():
    request_data = request.get_json()
    q = request_data['query']
    count = request_data['count']
    query = Query()
    query.read_query(q)
    q_process = query.processing_query(stopwords)
    matcher = Matcher(collection, q_process)
    results=matcher.get_result(count)
    return results

if __name__=='__main__':
    app.run()


