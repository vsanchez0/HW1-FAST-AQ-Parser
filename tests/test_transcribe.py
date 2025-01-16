# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    seq = "ATGC"
    expected_output = "UACG"
    assert transcribe(seq) == expected_output, f"Expected {expected_output}, got {transcribe(seq)}"
    
    seq = "ATGC"
    expected_output_reverse = "GCAU"
    assert transcribe(seq, reverse=True) == expected_output_reverse, f"Expected {expected_output_reverse}, got {transcribe(seq, reverse=True)}"
    
    invalid_seq = "ATGZ"
    try:
        transcribe(invalid_seq)
        assert False, "Expected ValueError for invalid nucleotides, but no error was raised."
    except ValueError as e:
        assert str(e) == "Sequence contains invalid nucleotides.", f"Unexpected error message: {e}"
    
    seq = ""
    expected_output_empty = ""
    assert transcribe(seq) == expected_output_empty, f"Expected {expected_output_empty}, got {transcribe(seq)}"


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    seq = "ATGC"
    expected_output = "GCAU"
    assert reverse_transcribe(seq) == expected_output, f"Expected {expected_output}, got {reverse_transcribe(seq)}"
    
    invalid_seq = "ATGZ"
    try:
        reverse_transcribe(invalid_seq)
        assert False, "Expected ValueError for invalid nucleotides, but no error was raised."
    except ValueError as e:
        assert str(e) == "Sequence contains invalid nucleotides.", f"Unexpected error message: {e}"
    
    seq = ""
    expected_output_empty = ""
    assert reverse_transcribe(seq) == expected_output_empty, f"Expected {expected_output_empty}, got {reverse_transcribe(seq)}"