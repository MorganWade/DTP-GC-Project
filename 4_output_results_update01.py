#code to output results of BLAST into an array and calculate BLAST statistics:

#function to output BLAST results into an array (for later use)

import numy as np

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
	print(results1)
	return results1
			

array = outputResults("../Rodent/rat_blast/output_blast", "../Rodent/Rattus_norvegicus_query_counter.txt")


#function to calculate BLAST statistics:

def blastStatistics(species, array):
	with open(species + "_query_counter.txt", "r") as f, open(species + "_stats_genes_found.txt", "w") as g:
		Total = np.sum(array)
		percent_alignments = 100*Total/len(array)
		print("percent alignments:", percent_alignments, "%")
		g.write("Number of genes with hits: ")
		g.write(str(Total))
		g.write("\nTotal Number of genes: ")
		g.write(str(len(array)))
		g.write("\nPercent alignments: ")
		g.write(str(percent_alignments))
	
	return


blastStatistics("../Rodent/Rattus_norvegicus", array)


#function to calculate 

def genehits(species, array):
	filename = species + "_output.fasta"
	list1 = []
	with open(filename, "r") as f:
		for line in f:
			if ">" in line:
				list1.append(line)
	with open(species + "_stats_genes_found.txt", "a") as g:
		g.write("\n\nMATCHED:\n")
		for (i, j) in zip(array, list1):
			if (i == 1):
				print(j)
				g.write(j)
		g.write("\nUNMATCHED:\n")
		for (i, j) in zip(array, list1):
			if (i == 0):
				print(j)
				g.write(j)
	return

				



genehits("../Rodent/Rattus_norvegicus", array)






