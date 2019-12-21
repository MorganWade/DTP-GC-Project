##Running file for creating a null distribution for hit % by BLASTing random samples of reference species (e.g. rat) genes to species of interest (e.g. gerbil) genome. Uses functions from Functions_rand.py 


import os
import numpy as np
from Functions_rand import extractGenes, makeQuery, sequenceCounter, blast_funct, outputResults, blastStatistics


#Our observed values from Blasting high GC content genes from Rat against Gerbil:

OverallN = 13
MatchN = 2



###

#creates an appropriate directory:

if os.path.isdir("../Rodent/rat_blast")==False:
	makedirectory = 'mkdir ' + "../Rodent/rat_blast"
	os.system(makedirectory)
	genome_input = 'makeblastdb -in ' + "/usr/local/bioinformatics/1_Genomics_practical_files/Pobesus_genome_assembly.fasta"
	dboutput = ' -dbtype nucl -out ' + "../Rodent/rat_blast" + '/genome'
	os.system(genome_input + dboutput)
###


#running the functions for a specified number of rounds to create the null distribution

Rounds = 20
i = 0
Number_Hits = []

while i < Rounds:
	print("Round:")
	print(i)
	lengthcheck = extractGenes("../Rodent/Rattus_norvegicus.fa", "../Rodent/Rattus_norvegicus_output.fasta", OverallN)
	N = makeQuery("../Rodent/Rattus_norvegicus_output.fasta", "../Rodent/Rattus_norvegicus", "Rattus_norvegicus")

	sequenceCounter(species = "../Rodent/Rattus_norvegicus", counterseq = N)


	blast_funct("../Rodent/rat_blast", "/usr/local/bioinformatics/1_Genomics_practical_files/Pobesus_genome_assembly.fasta", "../Rodent/Rattus_norvegicus_queries/Rattus_norvegicus_query", "../Rodent/Rattus_norvegicus_query_counter.txt")

	array = outputResults("../Rodent/rat_blast/output_blast", "../Rodent/Rattus_norvegicus_query_counter.txt")

	Out = blastStatistics("../Rodent/Rattus_norvegicus", array)
	Number_Hits.append(Out)
	i += 1
	print("\n")





Less_equal = []
for j in Number_Hits:
	if j <= MatchN:
		Less_equal.append(j)
	

p = len(Less_equal)/Rounds
if p == 0:
	print("p < ", 1/Rounds)
else:
	print("p = ", p)


print("\nMean length of all sequences:")
print(str(lengthcheck[0]))
print("\nStandard deviation of lengths:")
print(str(lengthcheck[1]))





