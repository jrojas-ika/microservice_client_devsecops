from flask import Blueprint, request, jsonify
from usecases import use_cases_client
from entities.model import Client
import logging

client_bp=Blueprint("client_bp", __name__)
request_mapping="/client" #http://ip:port/client

@client_bp.route(request_mapping, methods=["POST"]) # type: ignore
def insert():
    json=request.get_json()
    if not json:
        logging.warning("BODY EMPTY INSERT")
        return {"message": "empty body"}, 400
    try:
        if use_cases_client.insert(Client(**json)):
            logging.info("INSERT OK")
            return {"message": "Inserted"}, 201
    except Exception as ex:
        logging.error("ERROR INSERT {%s}", ex)
        return {"message": "server error"}, 500

@client_bp.route(request_mapping, methods=["GET"])
def select():
    try:
        data=use_cases_client.select_all()
        if data:
            dictionary_list=[{"id": t.id, "name": t.name, "address": t.address, "email": t.email} for t in data]
            return jsonify(dictionary_list), 200
        else:
            return [], 200
    except Exception as ex:
        logging.error("ERROR GET {%s}", ex)
        return {"message": "server error"}, 500