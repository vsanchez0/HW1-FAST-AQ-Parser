from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    # Create instance of FastqParser
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console


    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console

    fasta_parser = FastaParser("data/test.fa")
    fastq_parser = FastqParser("data/test.fq")
    
    print("Transcribed sequences from FastaParser:")
    for record in fasta_parser:
        transcribed_seq = transcribe(record[1])
        print(f">{record[0]}\n{transcribed_seq}")
    
    print("\nTranscribed sequences from FastqParser:")
    for record in fastq_parser:
        transcribed_seq = transcribe(record[1])
        print(f"@{record[0]}\n{transcribed_seq}")
    
    print("\nReverse transcribed sequences from FastaParser:")
    for record in fasta_parser:
        rev_transcribed_seq = reverse_transcribe(record[1])
        print(f">{record[0]}\n{rev_transcribed_seq}")
    
    print("\nReverse transcribed sequences from FastqParser:")
    for record in fastq_parser:
        rev_transcribed_seq = reverse_transcribe(record[1])
        print(f"@{record[0]}\n{rev_transcribed_seq}")


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
