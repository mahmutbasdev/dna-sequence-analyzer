def analyze_sequence(sequence):
    """
    Return a dictionary with length, base_count and GC content percentage
    """
    base_count = {base: sequence.count(base) for base in "ACGT"}
    total = len(sequence)
    gc_content = ((base_count["G"] + base_count["C"]) / total * 100) if total else 0

    return {
        "length": total,
        "base_count": base_count,
        "gc_content": round(gc_content, 2),
    }
