import requests
import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

ES_CID = os.getenv('ES_CID')
ES_USER = os.getenv('ES_USER')
ES_PWD = os.getenv('ES_PWD')

es = Elasticsearch(
    cloud_id=ES_CID,
    basic_auth=(ES_USER, ES_PWD)
)

es.info()

response=es.index(
 index='movies',
 document={
    'releaseyear': '1908',
    'title': 'It is not this day.',
    'origin': 'American',
    'director': 'D.W. Griffith',
    'cast': 'Harry Solter, Linda Arvidson',
    'genre': 'comedy',
    'wikipage':'https://en.wikipedia.org/wiki/A_Calamitous_Elopement',
    'plot': 'A young couple decides to elope after being caught in the midst of a romantic moment by the woman .'
 })

 print(response)


