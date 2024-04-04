import click
from AnalyzerFunctions import AnalizerFunctions

@click.command()
@click.argument('file_name', type=click.Path(exists=True, readable=True), nargs=1)
@click.option('--top', required=True, type=int)

def main(top, file_name):
    af = AnalizerFunctions()
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
        
    print(af.topX(wordlist=lines, num=top))
    
if __name__ == '__main__':
    main()