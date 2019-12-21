##Running file to create output data needed to run a general linear model to determine whether sequence length is a better predictor of missing genes than GC content



###
from Functions_glm import extractGenes, makeQuery, sequenceCounter, blast_funct, outputResults

NumberGenes = 2000

explans = extractGenes("../Rodent/Rattus_norvegicus.fa", "../Rodent/Rattus_norvegicus_output.fasta", NumberGenes)


N = makeQuery("../Rodent/Rattus_norvegicus_output.fasta", "../Rodent/Rattus_norvegicus", "Rattus_norvegicus")

sequenceCounter(species = "../Rodent/Rattus_norvegicus", counterseq = N)

blast_funct("../Rodent/rat_blast", "/usr/local/bioinformatics/1_Genomics_practical_files/Pobesus_genome_assembly.fasta", "../Rodent/Rattus_norvegicus_queries/Rattus_norvegicus_query", "../Rodent/Rattus_norvegicus_query_counter.txt")

output = outputResults("../Rodent/rat_blast/output_blast", "../Rodent/Rattus_norvegicus_query_counter.txt")


lengths = explans[0]
gcs = explans[1]

print(lengths)
print(gcs)
print(output)

with open("stats.txt", "w") as newfile:
	newfile.write("lengths:")
	newfile.write(str(lengths))
	newfile.write("\nGC proportion:")
	newfile.write(str(gcs))
	newfile.write("\nResult:")
	newfile.write(str(output))
