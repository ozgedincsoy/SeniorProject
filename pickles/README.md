# Pickle Files

The following pickle files holds dictionaries.

{ x : y }

* docToGenes.pickle : 

x (Integer) : Documents' PMID (Pubmed Document ID)

y (List) : List of genes that belongs to x.

* geneGraph.pickle : 

x (String) : Gene Name

y (List of pairs (a, b) ) : a is a gene name that occurs in the same document, b is the number of documents that have x and a in it.

* geneInformation.pickle :

x (String) : Gene Name

y (JSON) : HUDO ID of the gene, actual name, number of occurence, number of documents that gene occurs, matched terms, document ids as a list

* genePairs.pickle :

x (String) : Gene1-Gene2

y (Integer) : The number of documents that have gene1 and gene2. 

* weighted.pickle :

x (String) : Gene Names

y (Pair) : First element of the pair holds the number of occurence of the gene  per document in autism related papers, second element of the pair holds the number of occurence of the gene per document in epilepsy related papers.

* top100genevars.pickle : Intersection of the most weighted 100 autism related genes and the most weighted 100 epilepsy related genes are found as ['MECP2', 'SLC12A6', 'RAI1', 'FOSB', 'FOXP1', 'FOLH1', 'FOXP2']. A map is built for the genes variances (matched terms).

x (String) : Gene Variance

y (String) : Actual name of the gene

* sentenceDict.pickle : The dictionary is formed for ['MECP2', 'SLC12A6', 'RAI1', 'FOSB', 'FOXP1', 'FOLH1', 'FOXP2'].

x (String) : Sentence

y (List) : Gene Names 

* sentenceDictAllGenes.pickle : The dictionary is formed for the sentences that have one of the genes ,['MECP2', 'SLC12A6', 'RAI1', 'FOSB', 'FOXP1', 'FOLH1', 'FOXP2'], in it. The sentences are analyzed later and other genes are also detected.

x (String) : Sentence (Same as sentenceDict.pickle)

y (List) : Gene Names
