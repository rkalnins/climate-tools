import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse

def get_name(url):
    parsed = urlparse(url)
    return parsed.path.replace("/", "_")[1:]
    

def get_files(filename, pattern, destination_root):

    with open(f, "r") as html:
        contents = html.read()

        soup = BeautifulSoup(contents, "html.parser")
        pattern = "tx"
        all_txs = soup.find_all("a", text=pattern)

        for t in all_txs:
            url = t['href']
            destination_name = get_name(url)
            print(url)
    
if __name__ == "__main__":
    f = str(sys.argv[1])
    pattern = str(sys.argv[2])

    if len(sys.argv) == 4:
        destination_root = str(sys.argv[3])
    else:
        destination_root = ""

    get_files(f, pattern, destination_root)
