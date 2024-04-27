import click
from AnalyzerFunctions import AnalizerFunctions


@click.command()
@click.argument("file_name", type=click.Path(exists=True, readable=True), nargs=1)
@click.option("--top", required=True, type=int)
def main(top, file_name):
    """
    Main method of the script
    
    Args:
        :param int top: size of the list
        :param str file_name: /path_to/wordlist
    """
    af = AnalizerFunctions()
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    print(af.top_x(wordlist=lines, num=top))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
