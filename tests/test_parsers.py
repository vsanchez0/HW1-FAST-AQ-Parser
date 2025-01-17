# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest
import os


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    good = os.path.join('data','test.fa')
    blank = os.path.join('tests','blank.fa')
    bad = os.path.join('tests','bad.fa')

    parser = FastaParser(good)
    sequences = list(parser)
    assert len(sequences) > 0, "Expected at least one sequence in test.fa"
    assert isinstance(sequences[0], tuple) and len(sequences[0]) == 2, \
        "Each sequence should be a tuple with (header, sequence)"
    
    parser = FastaParser(blank)
    assert getattr(parser, '_sequences')==None, "Expected no sequences in blank.fa"

    parser = FastaParser(bad)
    assert getattr(parser, '_sequences')==None, "Expected malformed fasta file"


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    good = os.path.join("data", "test.fa")
    fastq = os.path.join("data", "test.fq")

    parser = FastaParser(good)
    sequences = list(parser)
    assert len(sequences) > 0, "Expected valid sequences from a well-formed FASTA file"

    parser = FastaParser(fastq)
    sequences = list(parser)
    assert sequences[0][0] is None, "Expected None when reading a FASTQ file with FastaParser"


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq = os.path.join("data", "test.fq")

    parser = FastqParser(fastq)
    reads = list(parser)
    assert len(reads) > 0, "Expected valid reads from a well-formed FASTQ file"

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq = os.path.join("data", "test.fq")
    fasta = os.path.join("data", "test.fa")
    
    parser = FastqParser(fastq)
    first_read = list(parser)[0]
    assert first_read[0] is not None, "Expected valid first read from a FASTQ file"

    try:
        parser = FastqParser(fasta)
        first_read = list(parser)[0]
        assert first_read[0] is None, "Expected None when reading a FASTA file with FastqParser"
    except Exception as e:
        assert isinstance(e, ValueError), f"Expected ValueError for FASTA file, got {type(e)}"