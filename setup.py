import json
import nltk
import mysql.connector

#run only for the first time
if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('stopwords')

    with open("config.json") as config_file:
        config = json.load(config_file)
        db_config = config["DATABASE"]

    db = mysql.connector.connect(host=db_config["HOST"], user=db_config["USERNAME"], password=db_config["PASSWORD"])
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['NAME']}")



