from dna_analysis import (
    parse_fasta,
    validate_sequence,
    analyze_sequence,
    find_mutations,
    calculate_mutation_rate,
)

def main():
    # FASTA files
    ref_file = "data/reference.fasta"
    sample_file = "data/sample.fasta"

    # Parse sequences
    ref_seq, ref_invalid_parser = parse_fasta(ref_file)
    sample_seq, sample_invalid_parser = parse_fasta(sample_file)

    # Validate
    ref_valid, ref_invalid = validate_sequence(ref_seq)
    sample_valid, sample_invalid = validate_sequence(sample_seq)

    if not ref_valid:
        print(f"Reference sequence invalid bases: {ref_invalid}")
        return
    if not sample_valid:
        print(f"Sample sequence invalid bases: {sample_invalid}")
        return
    
    if len(ref_seq) != len(sample_seq):
        print("Error: Reference and sample sequences have different lengths!")
        return

    # Analyze
    ref_analysis = analyze_sequence(ref_seq)
    sample_analysis = analyze_sequence(sample_seq)

    print("Reference Analysis:", ref_analysis)
    print("Sample Analysis:", sample_analysis)

    # Mutations
    mutations = find_mutations(ref_seq, sample_seq)
    mutation_rate = calculate_mutation_rate(mutations, len(ref_seq))

    print(f"Total mutations: {len(mutations)}")
    print(f"Mutation rate: {mutation_rate}%")
    for pos, ref_base, sample_base in mutations:
        print(f"Position {pos}: {ref_base} -> {sample_base}")


if __name__ == "__main__":
    main()
