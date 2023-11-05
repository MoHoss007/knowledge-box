from knowledge_box.models import db
from knowledge_box.app_factory import create_app
import nltk

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('stopwords')

    app = create_app()
    db.create_all()
