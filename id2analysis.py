import pickle

"""
    This script forms sentenceDictAllGenes.pickle.
    That is, the whole genes of the sentences
        that have the intersection of the most weighted 100 autism and epilepsy related genes.
"""

with open('pickles/sentenceDict.pickle', 'rb') as handle:
    sentences = pickle.load(handle)

with open('pickles/geneInformation.pickle', 'rb') as handle:
    genes = pickle.load(handle)

allGenesInSentences = {}
for sentence in sentences:
    gene_list = []
    for gene in genes:
        for var in genes[gene]["matchedTerms"]:
            if var in sentence:
                gene_list.append(var)
    allGenesInSentences[sentence] = gene_list


with open('sentenceDictAllGenes.pickle', 'wb') as handle:
    pickle.dump(allGenesInSentences, handle, protocol=pickle.HIGHEST_PROTOCOL)
