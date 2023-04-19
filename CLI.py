import argparse

def parser_arguments():
    parser = argparse.ArgumentParser(
        description="check if site is online",
        prog='sitechecker'
    )
    parser.add_argument(
        '-u',
        '--urls',
        type=str,
        metavar="URLs",
        nargs='+',
        default=[],
        help="Insert one or more URLs"
    )

    return parser.parse_args()

def results(results,url,errors = ""):
    if results:
        print(f"The website {url} is online and ready for use")
    else:
        print(f"Error, site {url} unreachable. Error:{errors}")
    return 
    