##Functions to create output data needed to run a general linear model to determine whether sequence length is a better predictor of missing genes than GC content

import os
import numpy as np


#Function which calculates the GC content of all the genes and randomly extracts a specified number N of them along with their lengths and GC content

def extractGenes(input_fasta, output_fasta, N):
	with open(input_fasta, "r") as f, open (output_fasta, "w") as newfile:
		allgenes = []
		allseq = []
		alllength = []
		allgc = []
		nuc = []
		lengths = []
		allgc = []
		for line in f:
			if '>' in line:
				if len(nuc) > 0:
					nuc = "".join(nuc)
					allseq.append(nuc)
					lengths.append(len(nuc))
					allgc.append(gc_content)
					nuc = []
				c=0
				a=0
				g=0
				t=0
				allgenes.append(line)
			else:
				for i in line:
					if i == "C":
						c += 1    
					if i == "G":
						g += 1
					if i == "A":
						a += 1    
					if i == "T":
						t += 1
				nuc.append(line.strip("\n"))
				gc_content = (g+c)/(a+t+g+c)
		counter = 0
		genes = np.random.choice(allgenes, size = N, replace = False)
		lengthout = []
		gcout = []
		for (each1, each2, each3, each4) in zip(allgenes, allseq, lengths, allgc):
			if each1 in genes:
				newfile.write(str(each1))
				newfile.write(str(each2))
				newfile.write("\n")
				newfile.write(str(each3))
				lengthout.append(each3)
				newfile.write("\n")
				newfile.write(str(each4))
				gcout.append(each4)
				newfile.write("\n")
		print(len(allgenes))
	return [lengthout, gcout]


#Function which makes a BLASTable directory and counts the number of queries

def makeQuery(fasta_input, species, sp1):
	counterseq = 0
	make_dir = "mkdir -p " + species + "_queries"
	os.system(make_dir)
	with open(fasta_input, "r") as f:
		for each in f:
			if '>' in each:
				counterseq += 1
			elif "A" in each or "C" in each or "T" in each or "G" in each:
				sp2 = species + "_queries/" + sp1
				with open(sp2 + "_query" + str(counterseq) + ".txt", "w") as newfile:
					newfile.write(each)
	return counterseq


#Function which writes the total number of queries to a new file

def sequenceCounter(species, counterseq):
	with open(species + "_query_counter.txt", "w") as h:
		h.write(str(counterseq))
	return


#Function which BLASTs the queries against the genome of interest (gerbil)

def blast_funct(directory_name, genome_input, query_input, count):

	makedirectory = 'mkdir -p ' + directory_name
	os.system(makedirectory)

	genome_input = 'makeblastdb -in ' + genome_input
	dboutput = ' -dbtype nucl -out ' + directory_name + '/genome'

	os.system(genome_input + dboutput)

	with open(count, "r") as file:
		for line in file:
			N = line

	for i in range(1, int(N)+1):
		print("Blasting: " + str(i))
		queryinput = 'blastn -query ' + query_input + str(i) +".txt"
		os.system(queryinput + ' -db ' + directory_name + '/genome -out ' + directory_name + '/output_blast' + str(i) + ".txt")
	
	return


#Function to output BLAST results as binary output (hit or no hit)

def outputResults(Fasta1, N):
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
	return results1
		



