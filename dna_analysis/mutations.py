def find_mutations(reference_sequence, sample_sequence):
    """
    Compare two DNA sequences and return a list of mutations.
    Each mutation is represented as a tuple: (position, ref_base, sample_base)
    """

    # Ensure sequences are the same length
    if len(reference_sequence) != len(sample_sequence):
        raise ValueError("Sequences must have equal length")

    mutations = []

    # Compare sequences position by position
    for i, (ref, sample) in enumerate(zip(reference_sequence, sample_sequence)):
        if ref != sample:
            mutations.append((i + 1, ref, sample))

    return mutations


def calculate_mutation_rate(mutations, sequence_length):
    """
    Calculate mutation percentage based on total sequence length.
    Returns 0 if sequence length is 0.
    """

    if sequence_length == 0:
        return 0

    # Mutation rate as a percentage, rounded to 2 decimals
    return round((len(mutations) / sequence_length) * 100, 2)
