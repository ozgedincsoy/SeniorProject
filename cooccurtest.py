import pickle

"""
    Detects most weighted 100 autism related genes and most weighted 100 epilepsy related genes.
"""
with open('pickles/weighted.pickle', 'rb') as handle:
    two_dim = pickle.load(handle)

with open('pickles/geneInformation.pickle', 'rb') as handle:
    allGenes = pickle.load(handle)

sorted_x = sorted(two_dim.items(), key=lambda kv: kv[1][0], reverse=True)
sorted_y = sorted(two_dim.items(), key=lambda kv: kv[1][1], reverse=True)

myf= open("mostfound.txt", "a")

"""
print("FOSB ", allGenes["FOSB"])
print("MECP2 ",allGenes["MECP2"])
print("FOXP2 ", allGenes["FOXP2"])
print("FOXP1 ",allGenes["FOXP1"])
print("RAI1 ", allGenes["RAI1"])
print("SLC12A6 ", allGenes["SLC12A6"])
print("FOLH1 ", allGenes["FOLH1"])
"""
#print(sorted_x[:40])
myf.write("=======================AutismMostFound==================================\n")
autism_most = []
epilepsy_most = []
common_genes= set()
for key,value in sorted_x[:100]:
    autism_most.append(key)
    myf.write(key + " " + str(value[0]) + " " + str(value[1]) + "\n")

myf.write("=========================EpilepsyMostFound================================\n")

for key,value in sorted_y[:100]:
    epilepsy_most.append(key)
    myf.write(key + " " + str(value[0]) + " " + str(value[1]) + "\n")

commons = list(set(autism_most).intersection(epilepsy_most))
print(commons)
gene_dic = {}
for common_gene in commons:
    gene_dic[common_gene] = common_gene
    for gene_var in allGenes[common_gene]["matchedTerms"]:
        gene_dic[gene_var] = common_gene

with open('top100genevars.pickle', 'wb') as handle:
    pickle.dump(gene_dic, handle, protocol=pickle.HIGHEST_PROTOCOL)

myf.write("=======================ENDHERE==================================\n")

for g in common_genes:
    print(g)
    print(two_dim[g])
