from pymongo import MongoClient
import pprint

printer = pprint.PrettyPrinter()

'''
must get the connection from compass and paste it in between "   " 
'''
conn = "mongodb://localhost:27017/"
client = MongoClient(conn)

# specifies which database in the client we want (we name the var db)
db = client.shopifystore
#in the db we are currently working with a collection called products, assign an appropriate var name as such:
products_collection = db.products


def find_all():
    '''
    collection_name.find() returns all documents in the collection
    collection_name.find().limit(x) returns x amount of documents in the collection
    collection_name.find().count() DONT USE THIS RATHER USE
    collection_name.count_documents(filter={})
    collection_name.find({"Price" : 500}) returns all documents which match the price
    '''
    products = products_collection.find().limit(3)

    for product in products:
        printer.pprint(product)

#find_all()

'''
bottom code is to find one document matching the contents of the filter ({whats inside these curly braces}) in a collection:

printer.pprint(products_collection.find_one({"Name" : "Je Mappelle"}))

so in this code, a document with the name "Je Mappelle" will be returned and all the other fields in the same document as well.
if however you only want the price associated with this product returned and nothing else you can do so by:

--> printer.pprint(products_collection.find_one({"Name" : "Je Mappelle"}, {"Price" : 1})

The 1 stands for show.

**NOTE** ---> the _id field will be returned everytime along with the filter 
'''




def get_product_by_id(product_id):
    #import Objectid from bson to work with id's
    from bson.objectid import ObjectId
    #change the string product_id to an actual Objectid
    _id = ObjectId(product_id)
    #search for the _id through the collection using a filter
    product = products_collection.find_one({"_id" : _id})

    printer.pprint(product)

#get_product_by_id("63d638a73896787b4940aad1")


'''
================================================
MORE ADVANCED QUERIES
================================================
'''

'''def get_price_range(min_price, max_price):
    query = {"$and": [
        {"Price In ZAR" : {"$gte" : min_price}},
        {"Price In ZAR": {"$lte" : max_price}}
    ]}
   

    products = products_collection.find(query).sort("Price In ZAR")
    for product in products:
        printer.pprint(product)


get_price_range(200, 400)'''

def get_price_range(min_price, max_price):
    query = {"$and": [
        {"Price in ZAR" : {"$gte" : min_price}},
        {"Price in ZAR": {"$lte" : max_price}}
    ]}
   

    products = list(products_collection.find(query).sort("Price in ZAR"))
    print("Number of products:", len(products))
    for product in products:
        printer.pprint(product)


def project_columns():
    # curly braces because its just a filter
    columns = {"_id" : 0, "Name" : 1, "Price in ZAR" : 1}
    # finds all documents and only shows the fields with a 1
    products = products_collection.find({}, columns)

    for prod in products:
        printer.pprint(prod)

get_price_range(200, 400)
project_columns()

