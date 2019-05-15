import re
import pickle

"""
    This script creates genePairs.pickle and geneGraph.pickle.
    It retrieves the genes that belongs to the same documents.
"""

def get_two_genes_contained(gene1, gene2, docs):
    res = []
    for doc in docs:
        if gene1 in docs[doc] and gene2 in docs[doc]:
            res.append(doc)
    return res

f = open("analyzedfiles/union.txt", "r")
file = f.read()

genes = {}
docs = {}
geneNames =[]
matches = re.findall("([^\s]+)\s+([0-9]+)\s+(.*?)[\s\n]*([0-9]+)\s+([0-9]+)\s+([a-zA-Z](?:.*?|)*[\s\n]+)((?:[0-9]+,)*[0-9]+),[\s\n]", file, re.MULTILINE | re.DOTALL)


for m in matches:
    doc_ids = m[6].split(',')
    matched_term_list = m[5].split(' | ')
    matched_term_list = matched_term_list[:len(matched_term_list)-1]
    genes[m[0]] = { "hugo" : m[1] , "name" : m[2], "occurrence" : m[3], "paperNum" : m[4], "matchedTerms" : matched_term_list, "docs" : doc_ids}
    geneNames.append(m[0])

for gene in geneNames:
    for doc_id in genes[gene]['docs']:
        gene_list = docs.get(doc_id, [])
        gene_list.append(gene)
        docs[doc_id] = gene_list

co_occurrence = {}
cooccur_graph = {}
for gene1 in geneNames:
    for gene2 in geneNames:
        cond= 0
        if gene1 is not gene2:
            gene_list = -1
            if (gene1 + "-" + gene2) not in co_occurrence and (gene2 + "-" + gene1) not in co_occurrence:
                #gene_list = co_occurrence.get((gene1 + "-" + gene2), -1)
                gene_list = len(get_two_genes_contained(gene1, gene2, docs))
                if gene_list is not 0:
                    print(gene_list)
                    cond=1
                    #print(len(get_two_genes_contained(gene1, gene2, docs)))
            if cond is 1:
                #print(gene_list)
                co_occurrence[(gene1 + "-" + gene2)] = gene_list
                pair_list1 = cooccur_graph.get(gene1, [])
                pair_list1.append((gene2, gene_list))
                cooccur_graph[gene1] = pair_list1
                pair_list2 = cooccur_graph.get(gene2, [])
                pair_list2.append((gene1, gene_list))
                cooccur_graph[gene2] = pair_list2

with open('pickles/genePairs.pickle', 'wb') as handle:
    pickle.dump(co_occurrence, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('pickles/geneGraph.pickle', 'wb') as handle:
    pickle.dump(cooccur_graph, handle, protocol=pickle.HIGHEST_PROTOCOL)
#print(co_occurrence)
