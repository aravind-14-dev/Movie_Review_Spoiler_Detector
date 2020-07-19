import string
import nltk
nltk.download('stopwords', download_dir='/tmp')
nltk.download('punkt', download_dir='/tmp')
nltk.download('averaged_perceptron_tagger', download_dir='/tmp')
nltk.download('wordnet', download_dir='/tmp')
nltk.data.path.append('/tmp')
from nltk.corpus import stopwords
def text_process(text):
    punc_remove = [char for char in text if char not in string.punctuation]
    punc_remove =''.join(punc_remove)
    return [word for word in punc_remove.split() if word.lower() not in stopwords.words('english')]