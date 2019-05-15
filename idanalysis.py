from pymongo import MongoClient
import nltk
import pickle
client = MongoClient("mongodb://localhost:27017/")
db = client.pubmed
collection = db.abstracts_copy14m

tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

with open('top100genevars.pickle', 'rb') as handle:
    allGenes = pickle.load(handle)

sentence_dict = {}
counter= 0
for article in collection.find({"MedlineCitation.Article.Abstract.AbstractText":{'$exists':True}}):
    abstract_paragraphs = article["MedlineCitation"]["Article"]["Abstract"]["AbstractText"]
    for paragraph in abstract_paragraphs:
        sentences = tokenizer.tokenize(paragraph)
        for sentence in sentences:
            for var in allGenes:
                #print("var ", var)
                #print("sentence ", sentence)
                if var in sentence:
                    gene_list = sentence_dict.get(sentence, [])
                    gene_list.append(var)
                    sentence_dict[sentence] = gene_list

with open('sentenceDict.pickle', 'wb') as handle:
    pickle.dump(sentence_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
