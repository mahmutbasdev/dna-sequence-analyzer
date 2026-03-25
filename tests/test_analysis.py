import unittest
import sys
import os

from dna_analysis import (
    parse_fasta,
    validate_sequence,
    analyze_sequence,
    find_mutations,
    calculate_mutation_rate,
)


class TestDNAAnalysis(unittest.TestCase):

    def setUp(self):
        # Example sequences for testing
        self.ref_seq = "ACGTACGT"
        self.sample_seq = "ACGTTCGT"  # 1 mutation: A->T at position 5

    def test_validate_sequence_valid(self):
        # Check that a valid sequence passes validation
        valid, invalid = validate_sequence(self.ref_seq)
        self.assertTrue(valid)
        self.assertEqual(invalid, [])

    def test_validate_sequence_invalid(self):
        # Check that an invalid sequence is detected correctly
        invalid_seq = "ACGTXCGT"
        valid, invalid = validate_sequence(invalid_seq)
        self.assertFalse(valid)
        self.assertEqual(invalid, ["X"])

    def test_find_mutations(self):
        # Check that mutations are correctly identified
        mutations = find_mutations(self.ref_seq, self.sample_seq)
        self.assertEqual(len(mutations), 1)
        self.assertEqual(mutations[0], (5, "A", "T"))

    def test_calculate_mutation_rate(self):
        # Check that mutation rate is calculated correctly
        mutations = find_mutations(self.ref_seq, self.sample_seq)
        rate = calculate_mutation_rate(mutations, len(self.ref_seq))
        self.assertEqual(rate, 12.5)  # 1/8 = 12.5%

    def test_analyze_sequence(self):
        # Check analysis results
        result = analyze_sequence(self.ref_seq)
        self.assertEqual(result["length"], 8)
        self.assertEqual(result["base_count"]["A"], 2)
        self.assertEqual(result["gc_content"], 50.0)


if __name__ == "__main__":
    unittest.main()