def readfasta(filename):
    '''Reading in several fasta files
       yield each pair of header and dna seperate
    '''
    # Try to open the file, error if file does not exsist
    try: file = open(filename, "r")
    except FileNotFoundError as errormessage:
        sys.exit(f"The file '{filename}' could not be found, error: {errormessage}")

    # Extract the dna, and the headers.
    oldheader = "FIRST HEADER"
    for line in file:
        line = line.strip()
        #if line is header yield dna and header except FIRST HEADER
        if line.startswith(">"):    
            newheader = line
            if oldheader != "FIRST HEADER":
                yield dna, oldheader
            dna = ""
            oldheader = newheader
        else:
            dna += line
    # Yield the last header and dna
    yield dna, oldheader
    file.close()
