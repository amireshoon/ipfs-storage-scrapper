from bs4 import BeautifulSoup
import requests

class IpfsStorageScrapper:
    url = ""
    headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
    
    def __init__(self, url, headers = None) -> None:
        self.url = url
        self.headers = headers if headers != None else self.headers

    def getHTML(self) -> str:
        req = requests.get(self.url, self.headers)
        return req.content
    
    def proccess(self) -> list:
        soup = BeautifulSoup(self.getHTML(), 'html.parser')
        table = soup.find_all('table')

        if len(table) < 0:
            return []
        
        items = table[0].find_all('tr')
        ipfsItems = []
        
        for item in items:
            tds = item.find_all('td')
            ipfsItem = {
                'name': tds[1].get_text().strip(),
                'url'   :   tds[1].find('a').get('href')
            }
            ipfsItems.append(ipfsItem)

        return ipfsItems
    
def main():
    iss = IpfsStorageScrapper(url="https://<myuser>.mypinata.cloud/ipfs/<hash>")
    items = iss.proccess()
    print(items)

if __name__ == "__main__":
    main()
