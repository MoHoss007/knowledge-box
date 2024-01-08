from knowledge_box import create_app

if __name__ == "__main__":
    app = create_app("config.json")
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])
