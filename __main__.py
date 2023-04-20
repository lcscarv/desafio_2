import argparse
import csv
from http.client import HTTPConnection
from urllib.parse import urlparse
import sys
class SiteChecker:
    def __init__(self,url):
        
        self.url = url
        
        
    def site_is_online(self,url):
        timeout = 10
        error = Exception("Houston, we got a problem!")       
        parser = urlparse(url)
        host = parser.netloc or parser.path.split("/")[0]
        for port in (80,443):
            conn = HTTPConnection(port=port,timeout=timeout,host=host)
            try:
                conn.request("HEAD","/")
                return True,None
            except Exception as e:
                error = e
            finally:
                conn.close()
        return False, str(error)
    
class CLI:
    def __init__(self):
        self.Parser = argparse.ArgumentParser(
            description="Check if site is online", prog = 'desafio_2'
        )
        
        self.define_arguments()
        
    def define_arguments(self):
        
        self.Parser.add_argument(
            '-u','--urls',
            type = str, metavar='URLs',
            nargs='+',default=[],
            help='Insert URLs for analysis'
        )
        self.Parser.add_argument(
            '-f', '--file',
            type=str, metavar='CSV File',
            help='Read URLs from a CSV file for analysis'
        )
        
    def parse_arguments(self):
           
        return self.Parser.parse_args() 
    
  
    def run(self):
        args = self.parse_arguments()
        urls = args.urls
        file = args.file
        
        if not urls and not file:
            print("Error. No URLs. Try Again",file = sys.stderr)
            sys.exit(1)
        if file:
            try:
                with open(file, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        url = row[0]
                        site_checker = SiteChecker(url)
                        results, errors = site_checker.site_is_online(url)
                        self.display_results(results, url, errors)
            except Exception as e:
                print(f"Error reading CSV file: {e}", file=sys.stderr)
                sys.exit(1)
                
        for url in urls:
            errors = ""
            
            try:
                site_checker = SiteChecker(url)
                results,errors = site_checker.site_is_online(url)
                
            except Exception as e:
                results = False
                errors = str(e)
            self.display_results(results,url,errors)
            
            
    def display_results(self,results,url,errors = ""):
        
        if results:
            print(f"The website {url} is online and ready for use")
        else:
            print(f"Error, site {url} unreachable. Error:{errors}")
        return     
        
if __name__ == "__main__":
    cli = CLI()
    cli.run()