#code to make query sequence file ready for blast


def makeQuery(fasta_input, species):
	with open(fasta_input, "r") as f, open(species + "_query.txt", "w") as newfile:
		for each in f:
			if '>' in each:
				continue
			elif "0" in each:
				continue
			else:
				print(each)
				newfile.write(each)
	return


makeQuery("../Rodent/Rattus_norvegicus_output.fasta", "../Rodent/Rattus_norvegicus")


#code to make a separate file with the number of query sequences

def sequenceCounter(species):
	with open(species + "_query.txt", "r") as g, open(species + "_query_counter.txt", "w") as h:
		counter = 0
		for line in g:
			counter +=1
		print(counter)
		h.write(str(counter))
	return

sequenceCounter("../Rodent/Rattus_norvegicus")
