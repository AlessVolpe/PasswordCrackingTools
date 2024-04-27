import click
from Hasher import HasherLogic


@click.command()
@click.argument("file_name", type=click.Path(exists=True, readable=True), nargs=1)
@click.option("--output", required=True, type=str)
def main(path_to_hash, path_to_dump):
    """
    Main method of the script
    
    Args:
        :param str path_to_hash: /path_to/hash_file
        :param str path_to_dump: /path_to/hash_file
    """
    hasher = HasherLogic(dump_file=path_to_dump, hash_file=path_to_hash)
    hasher.hash_lister()
    print("Hash dumped in " + path_to_hash)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
