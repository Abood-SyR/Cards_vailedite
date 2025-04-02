from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:aabbdd20@cluster0.kzpipyw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.Cobonts
list_cards = db["cards"]