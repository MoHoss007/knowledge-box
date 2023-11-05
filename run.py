from knowledge_box.app_factory import create_app
import nltk

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('stopwords')
    app = create_app()
    app.run(debug=True)
