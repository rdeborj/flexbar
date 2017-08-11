"""
Module Description
"""

def trim_adapters(read1_fastq,
                  read2_fastq,
                  flexbar="flexbar",
                  threads=6,
                  qual_format='sanger',
                  adapter_seq='AGATCGGAAGAGC',
                  adapter_removal='RIGHT',
                  min_adapter_overlap=7,
                  pretrim_phred=20,
                  min_read_length=25,
                  max_uncalled_bases=300,
                  output_path='./trimmed_fastq',
                  zip_output="GZ"):
    """
    A wrapper function for the "flexbar" adapter trimming utility.

    USAGE:
        object.trim_adapters(
            arg1
            )

    INPUT:
        * arg1: description of arg1

    OUTPUT:
        list of return values
    """
    options = ' '.join([
        '-n', str(threads),
        '-f', qual_format,
        '-as', adapter_seq,
        '-ae', adapter_removal,
        '-ao', str(min_adapter_overlap),
        '-q', str(pretrim_phred),
        '-m', str(min_read_length),
        '-u', str(max_uncalled_bases),
        '-t', output_path,
        '-r', read1_fastq,
        '-p', read2_fastq,
        '--zip-output', zip_output
        ])
    cmd = ' '.join([flexbar, options])

    return {"command":cmd}
