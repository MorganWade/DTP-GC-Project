#code to blast sequences of certain GC threshold in a genome and blast against query genome "Xxxxxxx_xxxxxx_output.fasta"





#We can use blast to find whether this genome assembly includes a sequence that is homologous to ​ Pdx1 ​. First, we make a BLAST-able database. We save it to a new sub-directory to keep things tidy.

import os

#blast_function(directory_name, genome_input, db_output, query_input

def blast_funct(directory_name, genome_input, query_input):

	makedirectory = 'mkdir -p ' + directory_name
	os.system(makedirectory)

	genome_input = 'makeblastdb -in ' + genome_input
	dboutput = ' -dbtype nucl -out ' + directory_name + '/genome'

	os.system(genome_input + dboutput)

	queryinput = 'blastn -query ' + query_input 

	
	os.system(queryinput + ' -db ' + directory_name + '/genome -out ' + directory_name + '/output_blast.txt')
	#os.system('blastn -query Rattus_norvegicus_query.txt \
	#-db rat_blast/fatsandrat_genome \
	#-out rat_blast/output_blast.txt')
	
	return


blast_funct("../Rodent/rat_blast", "/usr/local/bioinformatics/1_Genomics_practical_files/Pobesus_genome_assembly.fasta", "../Rodent/Rattus_norvegicus_query.txt")
