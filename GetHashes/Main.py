import click
from GetHashes import getHashes

@click.command()
@click.argument('file_name', type=click.Path(exists=True, readable=True), nargs=1)
@click.option('--output', required=True, type=str)
def main(output, file_name):
    getHashes(file_name, output)
    print('Hash dumped in ' + output)
    
if __name__ == '__main__':
    main()