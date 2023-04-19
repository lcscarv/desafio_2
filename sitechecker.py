from urllib.parse import urlparse
from http.client import HTTPConnection

def site_is_online(urls):
    parser = urlparse(urls)
    timeout = 2
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80,443):
        connection = HTTPConnection(port= port, host = host,timeout= timeout)
        try:
            
            connection.request("HEAD","/")    
            return True
        
        except Exception as e:
            print(f"Error, site {urls} unreachable. Error:{e}")
        finally:
            connection.close()
    raise e

