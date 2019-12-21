##Python script to get data in a format suitable for plotting as a histogram of frequency of high GC content genes on each chromosome.
#calculates the number of hits on each chromosome for the given GC threshold (in our case >0.75), then it calculates the total nucleotide length of the coding sequence of each chromosome 


def chromosomePosition(fasta, species):
	reader = 0
	counter = 0	
	with open(fasta, "r") as f, open(species + "_chromosome_position_old.txt", "w") as g:
		for line in f:
			if '>' in line:
				for letter in line:
					if ':' in letter:
						counter += 1
					if counter == 2:
						reader = 1
						if reader == 1:
							g.write(letter)
						if counter == 3:
							reader = 0
				reader = 0
				counter = 0
	return 
			

chromosomePosition("../Rodent/Rattus_norvegicus_output.fasta", "../Rodent/Rattus_norvegicus")


def chromosome_edit(species):
	with open(species + "_chromosome_position_old.txt", "r") as h, open(species + "_chromosome_position_new.csv", "w") as i:
		for line in h:
			for letter in line:
				if ':' in letter:
					i.write(",")
				else:	
					i.write(letter)
				
	return 
			

chromosome_edit("../Rodent/Rattus_norvegicus")




########################################

def chromosome_counter(species):
	with open(species + "_complete.fasta", "r") as f, open(species + "_chromosome_length.txt", "w") as g:
		reader = 0
		counter = 0	
		for line in f:
			if '>' in line:
				for letter in line:
					if ':' in letter:
						counter += 1
					if counter == 2:
						reader = 1
						if reader == 1:
							g.write(letter)
						if counter == 3:
							reader = 0

				reader = 0
				counter = 0
	return 
			
chromosome_counter("../Rodent/Rattus_norvegicus")


def chromosome_counter2(species):
	with open(species + "_chromosome_length.txt", "r") as h, open(species + "_chromosome_lengths1.csv", "w") as i:
		for line in h:
			for letter in line:
				if ':' in letter:
					i.write(",")
				else:	
					i.write(letter)
		i.write("\n")
				
	return 
			

chromosome_counter2("../Rodent/Rattus_norvegicus")



def chromosome_counter3(species):
	with open(species + "_complete.fasta", "r") as f, open(species + "_chromosome_lengths2.csv", "w") as g:
		g.write(",")
		for line in f:
			if '>' in line:
				continue
			if '0' in line:
				continue
			else: 
				length = len(line)
				g.write(str(length))
				g.write(",")
				length = 0
	return 
			
chromosome_counter3("../Rodent/Rattus_norvegicus")







