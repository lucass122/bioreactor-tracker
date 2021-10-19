import os

import pandas as pd
import plotly.express as px

# path of directory containing a collection of fastq files
INPUT_DIR = '/Users/timolucas/Documents/spirito/kraken/'
# number of entities per bar
ENTITIES_PER_BAR = 15
# filter by abbreviation of taxonomic rank (S, G, etc.)
TAX_RANK = 'S'


def count(input_dir: str, entities_per_bar: int, tax_rank: str, title: str) -> None:
    '''
    Read all fastq.gz_report files made by kraken2 from an input
    directory. Then filter by a specified rank and number of entities.
    Finally show and write resulting stacked barchart.

    A bar represent the number of occurrences per entity in a sample.
    '''

    # iterate over all tab-separated fastq.gz_report files in the input directory
    dfs = []
    for tsv_file in [f for f in os.listdir(input_dir) if f.endswith('_report')]:
        # read the files and add a header to the table
        df = pd.read_csv(
            os.path.join(input_dir, tsv_file),
            sep='\t',
            header=None,
            usecols=[1, 3, 5],
            names=['Count', 'Rank', 'Name'])

        # filter for the specified taxonomic rank,
        # sort by value, and pop specified amount of entries
        df = df[df['Rank'] == tax_rank]
        df = df.sort_values('Count', ascending=False)
        df = df.head(entities_per_bar)

        # format name col, drop rank col and add sample name col
        df['Name'] = df['Name'].apply(lambda s: s.strip())
        df = df.drop(columns='Rank')
        df['Sample'] = tsv_file.split('.')[0]

        # append and finally concatenate all dataframes
        dfs.append(df)
    df = pd.concat(dfs)

    # format, show, and write output
    fig = px.bar(df, x='Sample', y='Count', color='Name', title=title)
    fig.show()
    fig.write_html("kraken2_stacked_barchart_count.html")


def percent(input_dir: str, entities_per_bar: int, tax_rank: str, title: str) -> None:
    '''
    Read all fastq.gz_report files made by kraken2 from an input
    directory. Then filter by a specified rank and number of entities.
    Finally show and write resulting stacked barchart.

    A bar represent the percentage occurrences per entity in a sample.
    '''

    # iterate over all tab-separated fastq.gz_report files in the input directory
    dfs = []
    for tsv_file in [f for f in os.listdir(input_dir) if f.endswith('report')]:
        # read the files and add a header to the table
        df = pd.read_csv(
            os.path.join(input_dir, tsv_file),
            sep='\t',
            header=None,
            usecols=[0, 3, 5],
            names=['Percent', 'Rank', 'Name'])

        # filter for the specified taxonomic rank,
        # sort by value, and pop specified amount of entries
        df = df[df['Rank'] == tax_rank]
        df = df.sort_values('Percent', ascending=False)
        df = df.head(entities_per_bar)

        # format name col, drop rank col and add sample name col
        df['Name'] = df['Name'].apply(lambda s: s.strip())
        df = df.drop(columns='Rank')
        df['Sample'] = tsv_file.split('.')[0]

        # append and finally concatenate all dataframes
        dfs.append(df)
    df = pd.concat(dfs)

    # format, show, and write output
    fig = px.bar(df, x='Sample', y='Percent', color='Name', title=title)
    fig.show()
    fig.write_html("kraken2_stacked_barchart_percent.html")


def projected_percent(input_dir: str, entities_per_bar: int, tax_rank: str, title: str) -> None:
    '''
    Read all fastq.gz_report files made by kraken2 from an input
    directory. Then filter by a specified rank and number of entities.
    Finally show and write resulting stacked barchart.

    A bar represents the percentage distribution according to total
    occurrences per entity in a sample.
    '''

    # iterate over all tab-separated fastq.gz_report files in the input directory
    dfs = []
    for tsv_file in [f for f in os.listdir(input_dir) if f.endswith('report')]:
        # read the files and add a header to the table
        df = pd.read_csv(
            os.path.join(input_dir, tsv_file),
            sep='\t',
            header=None,
            usecols=[1, 3, 5],
            names=['Count', 'Rank', 'Name'])

        # filter for the specified taxonomic rank,
        # sort by value, and pop specified amount of entries
        df = df[df['Rank'] == tax_rank]
        df = df.sort_values('Count', ascending=False)
        df = df.head(entities_per_bar)

        # format name col, drop rank col and add sample name col
        df['Name'] = df['Name'].apply(lambda s: s.strip())
        df = df.drop(columns='Rank')
        df['Sample'] = tsv_file.split('.')[0]

        # replace counts by percentage distribution in relation to total counts
        count_sum = sum(df['Count'])
        df['Count'] = df['Count'].apply(lambda c: c / count_sum * 100)
        df['Percent'] = df['Count'].rename('Percent')

        # append and finally concatenate all dataframes
        dfs.append(df)
    df = pd.concat(dfs)

    # format, show, and write output
    fig = px.bar(df, x='Sample', y='Percent', color='Name', title=title)
    fig.show()
    fig.write_html("kraken2_stacked_barchart_projected_percent.html")


if __name__ == '__main__':
    count(INPUT_DIR, ENTITIES_PER_BAR, TAX_RANK, 'Total occurrences per sample')
    percent(INPUT_DIR, ENTITIES_PER_BAR, TAX_RANK, 'Percentage occurrences per sample')
    projected_percent(INPUT_DIR, ENTITIES_PER_BAR, TAX_RANK,
                      'Projected percentage distribution of occurrences per sample')
