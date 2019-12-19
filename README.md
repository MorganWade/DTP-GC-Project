# # Exploring GC-biased mutation across the metazoa

Code & documentation for the Dark Gene Brigade's DTP Michaelmas 2019 Bioninformatics Hackathon project: Exploring GC-biased mutation across the metazoa. Project members: Jack Gordon, Jacques Bouvier, Joe Morford, Morgan Wade, Ryan Carter, Sam Caygill.

Aim: Build a tool which is able to 1) Identify GC rich genes in a reference genome, 2) Search for these genes in a species of interest.

Approach: 1) Python programme to identify GC rich genes, 2) BLAST analysis to search for genes in genome of interest


## Getting Started

Download cDNA genome as a FASTA file of reference species from Ensembl - download the 'cdna.all' version. 
Download latest genome assembly of species of interest.
E.g., for our proof of concept we compared high GC content genes from the Rat (Rattus norvegicus) and Blasted those output genes against the Fat Sand Rat (Psammomys obesus) genome assembly. We used a P. obesus genome assembly given to us by Adam Hargreaves (adam.hargreaves@zoo.ox.ac.uk, https://www.zoo.ox.ac.uk/people/dr-adam-hargreaves).

### Prerequisites

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


## Example Outputs

Add additional notes about how to deploy this on a live system


## Authors

Jack Gordon, Jacques Bouvier, Joe Morford, Morgan Wade, Ryan Carter, Sam Caygill. All from the University of Oxford's BBSRC Doctoral Training Program (http://www.biodtp.ox.ac.uk/).


## Acknowledgments

* Thanks to Adam Hargreaves, our Bioinformatics course lecturer and coordinator, whose work inspired this project and who's P. obesus genome assembly plays a large role in it
* Thanks to PurpleBooth for the README.md template - https://gist.github.com/PurpleBooth/109311bb0361f32d87a2

