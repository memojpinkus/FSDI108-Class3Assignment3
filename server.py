from math import prod
from flask import Flask, abort
import json
from mock_data import catalog

app = Flask("Server")

@app.route("/")
def home():
    return "Hello from flask"

@app.route("/me")
def about_me():
    return "Guillermo Jimenez"


#######################################################
###############     API ENDPOINTS     #################
###############      RETURN JSONS     #################
#######################################################

@app.route("/api/catalog", methods=["get"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog", methods=["post"])
def save_product():
    pass

# GET /api/catalog/count -> how many products exist in the catalog
@app.route("/api/catalog/count")
def product_count():
    count = len(catalog)
    return json.dumps(count)

#get /api/catalog/total -> the sum o all the product's prices
@app.route("/api/catalog/total")
def total_of_catalog():
    total = 0
    for prod in catalog:
        total += prod["price"]

    return json.dumps(total)

@app.route("/api/product/<id>")
def get_by_id(id):
    #find the product with _id is equal to id
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)
    
    #not found, return an error 404
    return abort(404, "No product with such id")

app.run(debug=True)