
rule filter_fasta:
    input: 
        "data/vae_clusters_within_radius_with_looners_complete_unsplit_candidate_plasmids.tsv",
        "data/contigs_darwin_sub.fna"
    output:
        "filtered.fasta"
    shell:
        """
        python scripts/create_filtered_fasta.py {input[0]} {input[1]} {output}
        """
    
rule blast:
    input: 
        "filtered.fasta"
    output:
        "filtered_fasta_blastout.txx"
    shell:
        """
        ./bin/ncbi-blast-2.16.0+/bin/blastn -query {input} -db data/PLSDB/plsdb.fna -out {output}  -outfmt 6
        """

