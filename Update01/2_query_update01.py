#code to make query sequence ready for blast

import os

def makeQuery(fasta_input, species, sp1):
	counterseq = 0
	make_dir = "mkdir -p " + species + "_queries"
	os.system(make_dir)
	with open(fasta_input, "r") as f:
		for each in f:
			if '>' in each:
				counterseq += 1
			elif "0" in each:
				continue
			else:
				print(each)
				sp2 = species + "_queries/" + sp1
				with open(sp2 + "_query" + str(counterseq) + ".txt", "w") as newfile:
					newfile.write(each)
	return counterseq


N = makeQuery("../Rodent/Rattus_norvegicus_output.fasta", "../Rodent/Rattus_norvegicus", "Rattus_norvegicus")


#code to make separate file with number of query sequences & output as query_counter.txt

def sequenceCounter(species, counterseq):
	with open(species + "_query_counter.txt", "w") as h:
		print(counterseq)
		h.write(str(counterseq))
	return

sequenceCounter(species = "../Rodent/Rattus_norvegicus", counterseq = N)
