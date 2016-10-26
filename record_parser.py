#! usr/bin/env python

"""
This code reads a genbank file and extracts the Accession number, organism, taxonomy, and sequence.
It requires biopython
"""

from Bio import SeqIO

#Loads a parser and iterator for our GenBank file
gb_handle = open("file_path/sequences.gb", "r")

#Parsing through GenBank file
#Print the following: Name, taxonomy, Seq, organism
#Print Name, organism and Tax to tax file
#Print Name, organism and seq to fasta file

tax_file = open("tax_file_path_out/taxonomy.tax", 'a')
fasta_file = open("sequences_file_path_out/sequences.fasta", 'a')

for seq_record in SeqIO.parse(gb_handle, "genbank"):
    #Write taxonomy file
    tax_file.write(seq_record.name + "\t" + ";".join((seq_record.annotations['taxonomy'])) + "\n")
    
    #Write fasta file
    fasta_file.write(">" + seq_record.name + "\t" + ";".join((seq_record.annotations['taxonomy'])) + "\n" + str(seq_record.seq) + "\n")
    
#for genome in SeqIO.parse(gb_handle, "genbank"):
	#for gene in genome.features:
		#if (gene.type == "CDS"):
			#if ('gene' in gene.qualifiers):
				#if ([gene_name] in gene.qualifiers['gene'][0].lower():
					#start = gene.location.start.position
					#end = gene.location.end.position
					#tax_file.write(genome.name + "\t" + ";".join((genome.annotations['taxonomy'])) + "\n")
					#fasta_file.write(">" + genome.name + "\t" + ";".join((genome.annotations['taxonomy'])) + "\n" + str(genome.seq[start:end]) + "\n")
print ("All Done")
tax_file.close()
fasta_file.close()
