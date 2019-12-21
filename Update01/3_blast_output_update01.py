#code to BLAST sequences of certain GC threshold in a genome and blast against query genome "Xxxxxxx_xxxxxx_output.fasta"

#make a BLASTable database and save it as a separate subdirectory, then BLAST against genome of interest/query genome
 

#import os to access operating system functions

import os

#code to make a BLASTable database

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
		queryinput = 'blastn -query ' + query_input + str(i) +".txt"
		os.system(queryinput + ' -db ' + directory_name + '/genome -out ' + directory_name + '/output_blast' + str(i) + ".txt")
	
	
	return


blast_funct("../Rodent/rat_blast", "/usr/local/bioinformatics/1_Genomics_practical_files/Pobesus_genome_assembly.fasta", "../Rodent/Rattus_norvegicus_queries/Rattus_norvegicus_query", "../Rodent/Rattus_norvegicus_query_counter.txt")
