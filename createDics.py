import re
import pymongo
from pymongo import MongoClient
import pickle

"""
    This script creates geneInformation.pickle and docToGenes.pickle files.
"""

def get_two_genes_contained(gene1, gene2):
    res = []
    for doc in docs:
        if gene1 in docs[doc] and gene2 in docs[doc]:
            res.append(doc)
    return res

#print('Mongo version', pymongo.__version__)
client = MongoClient('localhost', 27017)
db = client.pubmed
collection = db.abstracts_copy14m

f = open("analyzedfiles/union.txt", "r")
file = f.read()

f_a = open("analyzedfiles/autism.txt", "r")
file_a = f_a.read()

f_e = open("analyzedfiles/epilepsy.txt", "r")
file_e = f_e.read()

genes = {}
docs = {}

genes_a = {}
docs_a = {}

genes_e = {}
docs_e = {}

gene_l = {}

matches = re.findall("([^\s]+)\s+([0-9]+)\s+(.*?)[\s\n]*([0-9]+)\s+([0-9]+)\s+([a-zA-Z](?:.*?|)*[\s\n]+)((?:[0-9]+,)*[0-9]+),[\s\n]", file, re.MULTILINE | re.DOTALL)

matches_a = re.findall("([^\s]+)\s+([0-9]+)\s+(.*?)[\s\n]*([0-9]+)\s+([0-9]+)\s+([a-zA-Z](?:.*?|)*[\s\n]+)((?:[0-9]+,)*[0-9]+),[\s\n]", file_a, re.MULTILINE | re.DOTALL)

matches_e = re.findall("([^\s]+)\s+([0-9]+)\s+(.*?)[\s\n]*([0-9]+)\s+([0-9]+)\s+([a-zA-Z](?:.*?|)*[\s\n]+)((?:[0-9]+,)*[0-9]+),[\s\n]", file_e, re.MULTILINE | re.DOTALL)


for m in matches:
    doc_ids = m[6].split(',')
    matched_term_list = m[5].split(' | ')
    matched_term_list = matched_term_list[:len(matched_term_list)-1]
    genes[m[0]] = { "hugo" : m[1] , "name" : m[2], "occurrence" : m[3], "paperNum" : m[4], "matchedTerms" : matched_term_list, "docs" : doc_ids}
    gene_l[m[0]] = m[0]
    for g in m[2]:
        gene_l[g] = m[0]


for gene in genes:
    for doc_id in genes[gene]['docs']:
        gene_list = docs.get(doc_id, [])
        gene_list.append(gene)
        docs[doc_id] = gene_list

for m in matches_a:
    doc_ids = m[6].split(',')
    matched_term_list = m[5].split(' | ')
    matched_term_list = matched_term_list[:len(matched_term_list)-1]
    genes_a[m[0]] = { "hugo" : m[1] , "name" : m[2], "occurrence" : m[3], "paperNum" : m[4], "matchedTerms" : matched_term_list, "docs" : doc_ids}

for gene in genes_a:
    for doc_id in genes_a[gene]['docs']:
        gene_list = docs_a.get(doc_id, [])
        gene_list.append(gene)
        docs_a[doc_id] = gene_list

for m in matches_e:
    doc_ids = m[6].split(',')
    matched_term_list = m[5].split(' | ')
    matched_term_list = matched_term_list[:len(matched_term_list)-1]
    genes_e[m[0]] = { "hugo" : m[1] , "name" : m[2], "occurrence" : m[3], "paperNum" : m[4], "matchedTerms" : matched_term_list, "docs" : doc_ids}

for gene in genes_e:
    for doc_id in genes_e[gene]['docs']:
        gene_list = docs_e.get(doc_id, [])
        gene_list.append(gene)
        docs_e[doc_id] = gene_list


two_dim = {}
for gene in genes:
    two_dim[gene] = []
    if gene in genes_a:
        two_dim[gene].append(float(genes_a[gene]["occurrence"])/float(genes_a[gene]["paperNum"]))
    else:
        two_dim[gene].append(0.0)
    if gene in genes_e:
        two_dim[gene].append(float(genes_e[gene]["occurrence"])/float(genes_e[gene]["paperNum"]))
    else:
        two_dim[gene].append(0.0)

sorted_y = sorted(two_dim.items(), key=lambda kv: kv[1][1], reverse=True)
counter= 0
sorted_x = sorted(two_dim.items(), key=lambda kv: kv[1][0], reverse=True)

with open('weighted.pickle', 'wb') as handle:
    pickle.dump(two_dim, handle, protocol=pickle.HIGHEST_PROTOCOL)

for key, value in sorted_x:
    counter+=1
    if (key,value) in sorted_y:
        print(key,value)
print("\n-----\n")
for document in collection.find():
    pmid = document["MedlineCitation"]["PMID"]
    break
    if pmid in docs:
        print(docs[pmid])
    #print(tokenizer.tokenize(document["MedlineCitation"]["Article"]["Abstract"]["AbstractText"][0])) # iterate the cursor
    #print("b")

with open('pickles/geneInformation.pickle', 'wb') as handle:
    pickle.dump(genes, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('pickles/docToGenes.pickle', 'wb') as handle:
    pickle.dump(docs, handle, protocol=pickle.HIGHEST_PROTOCOL)
