import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import argparse

URL = ''
SUFFIX = "'.pdf'"
SAVE_DIR = '' 

def parse_input():

    ap = argparse.ArgumentParser(description = "Download all files with a certain suffix from a website.")
    ap.add_argument("-url", help = "Website url to download your files from", required = True)
    ap.add_argument("-dir", help = "Directory to save files to. Default is current directory", required = False, default="")
    ap.add_argument("-suf", help = "File suffix to download. Default is pdf", required = False, default="pdf")

    opts = ap.parse_args()
    global URL 
    URL = opts.url
    global SAVE_DIR
    SAVE_DIR = opts.dir
    global SUFFIX
    SUFFIX = "." + opts.suf


def main():
    if not os.path.exists(SAVE_DIR):
        print("The directory does not exist", SAVE_DIR)
        return
        #TODO: add option to create directory
        #os.mkdir(SAVE_DIR)

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")    
    print ("Start")

    for file_link in soup.select("a[href$="+SUFFIX+"]"):
        #print("file",file_link)

        #Name the pdf files using the last portion of each link which are unique in this case, if not it's overwritten..
        filename = os.path.join(SAVE_DIR,file_link['href'].split('/')[-1])

        print("Downloading", filename)        

        #TODO: check if file exists before writing.. what do we do then?

        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(URL,file_link['href'])).content)

if __name__ == "__main__":
    #TODO: add progress bar
    #TODO: Might also extend to regex for different file 
    #TODO: deal with tricky file downloads like (.pdf/download) -> could give this as a suffix
    # or https://edu.epfl.ch/coursebook/fr/internet-analytics-COM-308
    #TODO: chekc if url valid -- catch error if not

    parse_input()

    main()