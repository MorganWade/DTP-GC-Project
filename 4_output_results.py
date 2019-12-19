#code to output results of BLAST and calculate percent query alignments:

#function to output BLAST results

def outputResults(Fasta1):
	with open(Fasta1, "r") as f:
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
	print(counter)
	return counter
			

counter = outputResults("../Rodent/rat_blast/output_blast.txt")



#function to calculate percent query alignments:

def blastStatistics(species, counter):
	with open(species + "_query_counter.txt", "r") as f, open(species + "_%_genes_found.txt", "w") as g:
		for line in f:
			total = int(line)
		percent_alignments = (counter/total)*100
		print("percent alignments:", percent_alignments, "%")
		g.write(str(percent_alignments))
	
	return


blastStatistics("../Rodent/Rattus_norvegicus", counter)
