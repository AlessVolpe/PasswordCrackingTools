import click
from AnalyzerFunctions import topX

@click.command()
@click.argument('file_name', type=click.Path(exists=True, readable=True), nargs=1)
@click.option('--top', required=True, type=int)
def main(top, file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
        
    print(topX(lines, top))
    
if __name__ == '__main__':
    main()