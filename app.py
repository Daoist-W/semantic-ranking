
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import semantic_service as ss


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type, Authorization, Access-Control-Allow-Credentials'


@cross_origin(
    origins=["localhost"],
    allow_headers="*",
    supports_credentials=True
)
@app.route('/api/v1/semantic/search', methods=['POST'])
def search_handler_v1():
    query = request.json['query']
    limit = request.json['limit']
    response = jsonify(ss.gensim_query(query, limit))
    return response


@cross_origin(
    origins=["localhost"],
    allow_headers="*",
    supports_credentials=True
)
@app.route('/api/v2/semantic/search', methods=['POST'])
def search_handler_v2():
    query = request.json['query']
    limit = request.json['limit']
    response = [[match['id'], match['score']] for match in ss.pinecone_query(query, limit)['matches']]
    return response


@cross_origin(
    origins=["localhost"],
    allow_headers="*",
    supports_credentials=True
)
@app.route('/api/v3/semantic/search', methods=['POST'])
def search_handler_v3():
    query = request.json['query']
    limit = request.json['limit']
    response = ss.davinci_query(query, limit)
    return response


@cross_origin(
    origins=["localhost"],
    allow_headers="*",
    supports_credentials=True
)
@app.route('/api/v4/semantic/search', methods=['POST'])
def search_handler_v4():
    query = request.json['query']
    limit = request.json['limit']
    response = ss.chatGPT_query(query, limit)
    return response


if __name__ == '__main__':
    app.run()

