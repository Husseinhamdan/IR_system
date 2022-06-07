from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import wordnet

porter=PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

# get part of speech tag
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def lower_text(text):
    lower=text.lower().strip()
    return lower

def text_to_wordtoken(text):
    token=word_tokenize(text)
    return token

def text_to_sentenctoken(text):
    sentence=sent_tokenize(text)
    return sentence

def stemText(sentence):
    token_words=word_tokenize(sentence)
    token_words
    stem_text=[]
    for word in token_words:
        stem_text.append(porter.stem(word))
        stem_text.append(" ")
    return stem_text

def stemWord(token_words):
    stem_word = []
    for word in token_words:
        stem_word.append(porter.stem(word))
    return stem_word

def lemmText(sentence):
    token_words=word_tokenize(sentence)
    token_words
    lemm_text=[]
    for word in token_words:
        lemm_text.append(wordnet_lemmatizer.lemmatize(word,get_wordnet_pos(word)))
    return lemm_text


def lemmWord(token_words):
    lemm_word=[]
    for word in token_words:
        lemm_word.append(wordnet_lemmatizer.lemmatize(word,get_wordnet_pos(word)))
    return lemm_word

def filter_stopWord(indexList,stopWord):
    filter_word=[]
    for index in indexList:
        if index not in stopWord:
            filter_word.append(index)
    return filter_word



