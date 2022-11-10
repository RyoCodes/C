from Bio.Seq import Seq
from Bio.SeqUtils import GC #A dedicated library to find the GC content in a given DNA sequence
my_seq = Seq("GGAGGATACCAAACCCCCCCCCGGGGTTCCCCGGGGG") #Input DNA sequence
print(GC(my_seq)) #GC content in the form of percentage
print(my_seq[4:12]) #Sequences in biopython act as strings, so this command to find a particular subset of the sequence
print(my_seq)
print(my_seq.complement) #To print the complement of the sequence
print(my_seq.reverse_complement()) #To print the reverse complement of the sequence
print(my_seq[::-1]) #easiest way to reverse a string
fasta_format_string = ">Name\n%s\n" % my_seq #To print the FASTA format of a string
print(fasta_format_string)
protein_seq = Seq("EVVRRRRNAK")
dna_seq = Seq("ACGT")
print(protein_seq + dna_seq) #Although this is unlikely in real life, it is to show that concatenation is possible.

#Concatenation of multiple sequences
list_of_seqs = [Seq("ACGT"), Seq("AACCTTCGG"), Seq("ATTGGCACT")]
concatenated = Seq("")
for s in list_of_seqs:
    concatenated +=s
    print('The concatenated form:', concatenated)

#To print the lowercase format of the sequence
print(dna_seq.lower())

#Transcription
coding_dna = Seq("ATTCGGCTACCGATCCACGCCCTACGCTTTCAACGTACCACAACTCGG")
print(coding_dna)
template_dna = coding_dna.reverse_complement()
print('The Template DNA sequence: ', template_dna)
messenger_rna = coding_dna.transcribe()
print('The messenger RNA sequence: ', messenger_rna)
print(template_dna.reverse_complement().transcribe()) #Direct way to obtain the mRNA from the template strand
print(messenger_rna.back_transcribe()) #To obtain the template strand from mRNA 

#Translation
print('The protein sequence:', messenger_rna.translate()) #Protein sequence from mRNA
print('The protein sequnece: ', coding_dna.translate()) #Protein sequence directly from coding DNA strand

gene = Seq("ATTGACGATACCAGTACCGATCACAGTACCAGATCACCGATTCCACGACATTACGCGATACGAGACGATCGACAGTAGACGATACTACTATTTCAGACGATAUGA")
print(gene.translate(table = "Bacterial"))
print(gene.translate(table="Bacterial", to_stop = True))

#Translation tables
from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print(standard_table)
print(mito_table)
print(mito_table.stop_codons)
print(mito_table.start_codons)
print(mito_table.forward_table["ACG"])

#Mutable sequence objects
from Bio.Seq import MutableSeq
mutable_seq = MutableSeq(my_seq)
print(mutable_seq)
print(mutable_seq.remove("T"))
print(mutable_seq.reverse())

#Alternatives to sequence onjects

from Bio.Seq import reverse_complement, back_transcribe, translate
my_string = "GGTACCACATCCAGACCCCCATACGGCCACAGCCTCAGCATCCCGAATTTA"
reverse_complement(my_string)
back_transcribe(my_string)
translate(my_string)

