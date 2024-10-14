import pandas as pd                                                              
import sys
# Should only contain possible plasmids
# clusterfile = "/home/bxc755/rasmussen/scratch/ptracker/plasmid_graph/data/vae_clusters_within_radius_with_looners_complete_unsplit_candidate_plasmids.tsv" 
clusterfile = sys.argv[0]
df = pd.read_table(clusterfile, sep="\t")                                             
# len(df.contigname)
df = df.assign(contigname = ">" + df.contigname)

from readfasta import readfasta                                   
# All contigs
# fnafile = "data/contigs_darwin_sub.fna"                           
fnafile = sys.argv[1]
header2dna = {header: dna for dna, header in readfasta(fnafile)}

# Filter for only containing plasmids
contigset = set(df.contigname)
header2dna_filtered = {header: dna for header, dna in header2dna.items() if header in contigset}
assert len(header2dna_filtered) == 12350

# print to file
with open(sys.argv[2], "w") as f:
    for header, dna in header2dna_filtered.items():
        print(header, file=f)
        print(dna, file=f)