# DNA Mutation Analysis (Python)

This is a simple Python project that analyzes DNA sequences and detects mutations between a reference sequence and a sample sequence.

## Features

- DNA sequence validation (A, C, G, T)
- Nucleotide composition counting
- GC content calculation
- Mutation detection between two sequences
- Mutation rate calculation

## Project Structure
- data/             FASTA files
- dna_analysis/     core functions: parser, validator, analysis, mutations
- scripts/          run_analysis.py: main script to run analysis
- tests/            unit tests

## Usage
> Requires Python 3.10+ to run

1. Place your FASTA files in the data/ folder or, use the existing example files.
(To detect mutations, you should modify either the sample sequence or the reference sequence.)

2. Run the analysis script from the project root:

### Windows
```bash
$env:PYTHONPATH="src"
python -m scripts.run_analysis
```
### Linux / macOS
```bash
export PYTHONPATH=src
python -m scripts.run_analysis
```

## Run Unittest
In project root:

### Windows
```bash
$env:PYTHONPATH="src"
python -m unittest discover -s tests -p "*.py"
```
### Linux / macOS
```bash
export PYTHONPATH=src
python -m unittest discover -s tests -p "*.py"
```

## Purpose

This project serves as an introduction to DNA sequence analysis, focusing on how biological sequence data can be processed and analyzed programmatically.

## What I Learned

- Handling and cleaning biological sequence data
- Validating DNA sequences programmatically
- Comparing sequences to detect mutations
- Calculating nucleotide statistics and mutation rates
- Structuring a Python project professionally for reuse and clarity
