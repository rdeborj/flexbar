#!/usr/bin/env python3

import argparse

# from flexbar import trim_adapters

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--read1_fastq',
                        help='FASTQ file for read 1')
    parser.add_argument('--read2_fastq',
                        help='FASTQ file for read 2')
    parser.add_argument('--program',
                        default='flexbar',
                        help='adapter trimming program (default: flexbar)')
    parser.add_argument('-t',
                        '--threads',
                        default=6,
                        help="number of threads")
    parser.add_argument('-q',
                        '--qual_format',
                        default='sanger',
                        help="quality string format")
    parser.add_argument('--adapter_seq',
                        default='AGATCGGAAGAGC',
                        help='adapter sequence')
    parser.add_argument('--adapter_removal',
                        default='RIGHT',
                        help='type of adapter sequence removal')
    parser.add_argument('--min_adapter_overlap',
                        default=7,
                        help='minimum adapter bases overlapping')
    args = parser.parse_args()
    print(args)

################################################################################

if __name__ == "__main__":
    main()
