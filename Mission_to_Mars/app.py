#Importations
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#It's Flask Time
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")
