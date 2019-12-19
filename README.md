# # Exploring GC-biased mutation across the metazoa

Code & documentation for the Dark Gene Brigade's DTP Michaelmas 2019 Bioinformatics Hackathon project: Exploring GC-biased mutation across the metazoa. Project members: Jack Gordon, Jacques Bouvier, Joe Morford, Morgan Wade, Ryan Carter, Sam Caygill.

Aim: Build a tool which is able to:
1) Identify GC rich genes in a reference genome, 
2) Search for these genes in a species of interest.

Approach: 
1) Python programme to identify GC rich genes, 
2) BLAST analysis to search for genes in genome of interest

Background:

GC rich genes are more likely to be missing from genome assemblies. This is a well-known phenomena in many bird and honey bee species where only recently have scientists been able to produce assemblies containing these GC-rich genes. However, the same is true in gerbils - specifically the Fat Sand Rat, Psammomys obesus, which is known to have unusually high GC content around the ParaHox Gene cluster (Hargreaves et al, 2017).

About the project:

This is a set of code which searches a reference species' cDNA genome for genes which have a high GC content (defined as GC content > 0.750) then uses these sequencces as queries against the species of interest genome assembly to see if these high GC content regions have been conserved across the species. In our case, we did our project comparing the well-studied and well-sequenced Rat (Rattus norvegicus) against the comparatively poorly-studied Fat Sand Rat (Psammomys obesus).

### Prerequisites

Download cDNA genome as a FASTA file of reference species from Ensembl - download the 'cdna.all' version. 
Download latest genome assembly of species of interest as a FASTA file.

E.g., for our proof of concept we compared high GC content genes from the Rat (Rattus norvegicus) and BLASTed those output genes against the Fat Sand Rat (Psammomys obesus) genome assembly. We used a P. obesus genome assembly given to us by Adam Hargreaves (adam.hargreaves@zoo.ox.ac.uk, https://www.zoo.ox.ac.uk/people/dr-adam-hargreaves).

*we have not uploaded sample genome data here due to file size, but here is the link to the Ensembl page where we downloaded our Rat genome: http://www.ensembl.org/Rattus_norvegicus/Info/Index and here is a link to the latest genome assembly of the Fat Sand Rat from NCBI: ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/215/935/GCA_002215935.1_ASM221593v1/GCA_002215935.1_ASM221593v1_genomic.fna.gz*


## Notes on the Versions

There are three sets of scripts, each saved in it's own branch. This README.md is for all of them. 

*The original approach:*
All the query sequences from one species are in the same file & that query file as a whole gets BLASTed against the genome of interest 

*Update01:*
Each query sequence is in a separate file and each separate query gets BLASTed against the genome of interest. 

--> Why two approaches?

We realized BLAST might find some of the shorter query sequences multiple times in each genome, thereby artificially altering the hit count. So we changed it to BLAST each query separately, that way we can take it as a binary output - were there hits or not - for each query. 

*Stats scripts:*
Scripts to generate: 
- random samples of genes from the reference genome to create a null distribution of % hits to see if GC-rich rat genes are less likely to be found in the gerbil genome than are GC-normal genes
- the data needed to run a general linear model on sequence length and GC content to determine if sequence length is a better predictor of missing genes than GC content

--> The actual statistics were calculated in R using the generated data (no original code, standard R functions)

Branches:

Main Branch = original approach: all query sequences in one file, this file gets BLASTed against species of interest genome, number of hits taken, percentage of hits calculated.

Update01 Branch = Update01 : query sequences in separate files, each file gets BLASTed against sepecies of interest genome, binary statistics calculations - were there hits or not? <-- meant to control for the same query sequence potentially popping up multiple times in the genome

Stats Branch = Stats scripts

mappingGCcontentTOchromosomes : Branch containing an R script and a python3 script for generating histograms of frequency of GC content across chromosomes for the Rat (Rattus norvegicus) genome. This is useful primarily for our project presentation and is unlikely to be useful for anyone else. Still, it is included here for posterity's sake.


## Getting Started

Work off of the code from Update01 Branch - this is the most recent and most up-to-date set of code.

We worked on a Linux Ubuntu system. The code is written for Python 3 and meant to be saved as a script and then run from the command line:
```
python3 1_extract_new_genes.py
```
In order to run the BLAST you will need to include:
```
import os
```
in that script (included in the code uploaded here).


## Running the Code

Create a directory for your project as a whole, e.g., 'GC_Project' and within that directory make a subdirectory called 'Code' and another for each species you will BLAST your species of interest against, e.g., 'Rat'. Save all the code files to the 'Code' directory and save your genomes of your reference species and species of interest into the 'Rat' directory.

As part of the scripts you will generate the additional directories you will need, e.g., making a BLAST-able database and saving it to a new subdirectory.


## Example Outputs - Proof of Concept

Q1: Are there GC rich genes in the Rat genome that are 'missing' in the gerbil genome?

Result: Identified GC rich genes in the rat genome --> BLASTed these genes against the gerbil genome --> 2/13 genes were present in the gerbil genome --> Missing genes included FRAT2, TRNP1, BRI3
  
However, it is unlikely these genes are actually missing - more likely they have not been assembled in the P. obesus genome. We are working off of an older P. obesus genome assembly, so it is possible that the most current assembly may contain these genes or their homologs.


Q2: Are GC genes more likely to be missing?

Approach & Result: We also used our tool to see if GC rich genes were more likely to be missing compared to random samples of genes from the reference genome. To do this, we conducted queries using GC rich genes and compared the hit % to the hit % for a series of random samples of genes from the same rat genome. This confirmed earlier observations mentioned in the introduction that GC rich genes were more likely to be missing from genome assemblies. Statistics run in R.

Q3: Are these results potentially confounded by sequence length?

Approach & Result: Mean sequence length of 13 very GC rich rat genes considerably lower than average length of rat genes - could sequence length be confounding our results about GC content? We used our tool to randomly pull 2000 rat genes & their lengths & GC contents and query them against the gerbil genome. We then performed a general linear model on that data determine whether sequence length was a better predictor of missing genes than GC content and found that, yes, sequence length is a better predictor of missing genes than GC content. 


## Authors

Jack Gordon (jack.gordon@stcatz.ox.ac.uk), Jacques Bouvier (jacques.bouvier@stx.ox.ac.uk), Joe Morford (joe.morford@merton.ox.ac.uk), Morgan Wade (morgan.wade@hertford.ox.ac.uk), Ryan Carter(ryan.carter@stx.ox.ac.uk), Sam Caygill (samuel.caygill@hertford.ox.ac.uk). All from the University of Oxford's BBSRC Doctoral Training Program (http://www.biodtp.ox.ac.uk/).

For questions or comments, please contact Joe Morford joe.morford@merton.ox.ac.uk or Jacques Bouvier jacques.bouvier@stx.ox.ac.uk

## Acknowledgments

* Thanks to Adam Hargreaves, our Bioinformatics course lecturer and coordinator, whose work inspired this project and who's P. obesus genome assembly plays a large role in it
* Thanks to PurpleBooth for the README.md template - https://gist.github.com/PurpleBooth/109311bb0361f32d87a2

## References

* Hargreaves et al (2017) Genome sequence of a diabetes-prone rodent reveals a mutation hotspot around the ParaHox gene cluster. PNAS 114 (29) 7677-7682. https://doi.org/10.1073/pnas.1702930114 

## Extras
* For more information of the larger context of this project, check out: http://theconversation.com/introducing-dark-dna-the-phenomenon-that-could-change-how-we-think-about-evolution-82867
