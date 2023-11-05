import nltk
import random
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords


class GenerateQuestions:
    def generate(self, document: str) -> list:
        sentences = sent_tokenize(document.lower())

        # Create MCQs
        mcqs = []
        for sentence in sentences:
            mcqs.extend(self.__generate_mcq(sentence))

        mcqs_dicts = []
        for mcq in mcqs:
            question, options = mcq
            options_dicts = [{op: (i == 0)} for i, op in enumerate(options)]
            random.shuffle(options_dicts)
            mcq_dict = {"question_text": question,
                        "options": options_dicts}

            mcqs_dicts.append(mcq_dict)

        return mcqs_dicts

    def __get_distractors(self, word):
        distractors = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.name().lower() != word.lower():
                    distractors.append(lemma.name().replace('_', ' '))
        return list(set(distractors))[:3]  # Limit to 3 distractors

    def __generate_mcq(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        questions = []

        for (word, tag) in tagged:
            if tag in ['NN', 'NNP'] and wordnet.synsets(word):  # Nouns with WordNet entry
                distractors = self.__get_distractors(word)
                if distractors:
                    question = sentence.replace(word, '_______')
                    options = [word.capitalize()] + distractors
                    questions.append((question, options))

        return questions
