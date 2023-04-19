import sys
from CLI import parser_arguments,results
from sitechecker import site_is_online


def check_urls(urls):
    for url in urls:
        errors = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            errors = str(e)
        results(result,url,errors)
def main():
    args = parser_arguments()
    urls = args.urls
    if not urls:
        print("No URLs for analysis,",file = sys.stderr)
        sys.exit(1)
    check_urls(urls)