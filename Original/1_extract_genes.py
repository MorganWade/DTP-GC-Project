#code to extract coding sequences of certain GC threshold in a genome and save to "Xxxxxxx_xxxxxx_output.fasta"


def extractGenes(input_fasta, output_fasta):
	with open(input_fasta, "r") as f, open (output_fasta, "w") as newfile:
		gc_content = 0
		save = 0
		printer = 0
		for line in f:
			if '>' in line:
				if gc_content > .750:
					print(save, gc_content)
					print("".join(nuc))
					print("\n")
					newfile.write(save)
					newfile.write(str(gc_content) + "\n")
					newfile.write("".join(nuc) + "\n")
				nuc = []
				c=0
				a=0
				g=0
				t=0
				save = line
				continue
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
	return


extractGenes("../Rodent/Rattus_norvegicus.fa", "../Rodent/Rattus_norvegicus_output.fasta")





