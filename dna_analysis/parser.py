def parse_fasta(file_path):
    """
    Reads a FASTA file and returns the DNA sequence as a string.
    Skips header lines starting with '>'.
    """
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    # Combine lines, skip headers and empty lines, make uppercase
    sequence = "".join(
        line.strip().upper()
        for line in lines
        if not line.startswith(">") and line.strip()
    )

    # Detect invalid bases
    valid_bases = {"A", "C", "G", "T"}
    invalid_bases = [b for b in sequence if b not in valid_bases]

    return sequence, invalid_bases
