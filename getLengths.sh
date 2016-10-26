#!/usr/bin/python
# This script uses biopython to find the length of each sequence while also saving the genetic sequence itself. If needed it can be adjusted to leave out any of those parts by editing the second to last line

# Run it using `./getLength.sh SEQ.fasta > output.txt`

#!/usr/bin/python
from Bio import SeqIO
import sys
cmdargs = str(sys.argv)
for seq_record in SeqIO.parse(str(sys.argv[1]), "fasta"):
 output_line = '%i' % \
 (len(seq_record))
 print(output_line)

