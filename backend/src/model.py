import pickle
import nltk
from nltk.tokenize.regexp import WordPunctTokenizer
nltk.download("punkt")

class TrollAnalyzer:
  def __init__(self, model):
    self.model = model
    self.tokenizer = WordPunctTokenizer()
    self.scale_score = lambda k: k * 2 - 1

  def analyze(self, sentence):
    words = self.tokenizer.tokenize(sentence)
    predictions = {word: self.scale_score(self.model.predict_proba([word])[0][1]) for word in words}
    total = self.scale_score(self.model.predict_proba([sentence])[0][1])
    return {
        "master": total,
        "tokenized": predictions
    }

def load_analyzer(model_path = "./models/troll_model.pkl"):
    with open(model_path, "rb") as infile:
        model = pickle.load(infile)
        return TrollAnalyzer(model)
    
