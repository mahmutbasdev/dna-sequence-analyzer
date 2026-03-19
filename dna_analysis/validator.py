def validate_sequence(sequence):
    """
    Validate DNA sequences.
    Checks that a sequence contains only valid nucleotides (A, C, G, T).
    """

    valid_bases = {"A", "C", "G", "T"}

    # If sequence is a list, convert it to a string
    if isinstance(sequence, list):
        sequence = "".join(sequence)

    # Collect all invalid bases in the sequence
    invalid_bases = [base for base in sequence if base not in valid_bases]

    # Sequence is valid if no invalid bases were found
    is_valid = len(invalid_bases) == 0

    return is_valid, invalid_bases
