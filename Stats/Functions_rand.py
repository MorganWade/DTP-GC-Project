##Functions for creating a null distribution for hit % by BLASTing random samples of reference species (e.g. rat) genes to species of interest (e.g. gerbil) genome 

import os
import numpy as np
from random import sample


#Function to extract random genes

def extractGenes(input_fasta, output_fasta, N):
	print("Extracting genes...")
	with open(input_fasta, "r") as f, open (output_fasta, "w") as newfile:
		allgenes = []
		allseq = []
		nuc = []
		lengths = []
		for line in f:
			if '>' in line:
				if len(nuc) > 0:
					nuc = "".join(nuc)
					allseq.append(nuc)
					lengths.append(len(nuc))
					nuc = []
				allgenes.append(line)
			else:
				nuc.append(line.strip("\n"))
		counter = 0
		genes = np.random.choice(allgenes, size = N, replace = False)
		for (each1, each2) in zip(allgenes, allseq):
			if each1 in genes:
				newfile.write(str(each1))
				newfile.write(str(each2))
				newfile.write("\n")
		m = np.mean(lengths)
		sd = np.std(lengths)
	return [m, sd]



#Function to make query

def makeQuery(fasta_input, species, sp1):
	print("Making query...")
	counterseq = 0
	make_dir = "mkdir -p " + species + "_queries"
	os.system(make_dir)
	with open(fasta_input, "r") as f:
		for each in f:
			if '>' in each:
				counterseq += 1
			else:
				sp2 = species + "_queries/" + sp1
				with open(sp2 + "_query" + str(counterseq) + ".txt", "w") as newfile:
					newfile.write(each)
	return counterseq


#Function to make new txt file with query count

def sequenceCounter(species, counterseq):
	with open(species + "_query_counter.txt", "w") as h:
		h.write(str(counterseq))
	return


#Function to BLAST queries against reference species genome & output these results in a new txt file

def blast_funct(directory_name, genome_input, query_input, count):
	print("Blasting...")
	with open(count, "r") as file:
		for line in file:
			N = line

	for i in range(1, int(N)+1):
		queryinput = 'blastn -query ' + query_input + str(i) +".txt"
		os.system(queryinput + ' -db ' + directory_name + '/genome -out ' + directory_name + '/output_blast' + str(i) + ".txt")
	
	return


#Function to output formatted results from blast output

def outputResults(Fasta1, N):
	print("Results...")
	with open(N, "r") as g:
		for line in g:
			M = line
	results = []
	for i in range(1, int(M)+1):
		files = Fasta1 + str(i) +".txt"
		with open(files, "r") as f:
			reader = 0
			counter = -5
			for line in f:
				if 'Sequences producing significant alignments' in line:
					reader = 1
				if reader == 1: 
					counter += 1
				#	print(line)
				if '>' in line:
					reader = 0
			results.append(counter)
	results1 = []
	for i in results:
		if (i <= 0):
			results1.append(0)
		else:
			results1.append(1)
	print(results1)
	return results1
		

#Function to calculate total number of genes with hits

def blastStatistics(species, array):
	Total = np.sum(array)
	print("Number of genes with hits:", Total)
	return Total





