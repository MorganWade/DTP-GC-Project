#code to extract total number of coding sequences in downloaded genome


def numberSequences(Fasta1, mode):
	with open(Fasta1, mode) as f:
		x = 0
		for line in f:
			if '>' in line:
				x += 1
				print(line)
				print(x)


numberSequences("Rattus_norvegicus.fa", "r")
