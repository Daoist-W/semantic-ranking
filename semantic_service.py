from davinci_service import davinci_query as query_v3
from chat_service import chat_query as query_v4
from embedding_service import get_embedding, get_embeddings_from_list
from gensim_service import most_similar, update_model, update_model_from_list
from text_service import refresh_text_sources_from_local_dir, refresh_text_sources_from_rest_api
from pinecone_service import pinecone_query as query_v2, upsert_embeddings, clean_database


def gensim_query(query, limit):
    return None


def pinecone_query(query, limit):
    return None


def davinci_query(query, limit):
    return None


def chatGPT_query(query, limit):
    return None