import requests
import shutil
from bs4 import BeautifulSoup as bs
import os

class SubsceneDownload(object):
    baseURL = 'https://www.subscene.com'

    def downloadFileWithURL(self, dictURL):
        for url in dictURL:
            r = requests.get(url['DirectLink'], stream=True, verify=False)
            if r.status_code == 200:
                with open(url['Title'] + ".rar", "wb") as f:
                    shutil.copyfileobj(r.raw, f)
            else:
                raise Exception("Download Failure")

    def makingtheSoup(self, url):
        page_data = requests.get(url, verify=False)
        if page_data.status_code == 200:
            soup = bs(page_data.content, 'lxml')
            return soup
        
    def fetchUrlSubs(self, mainUrl):
        urlsSubs  = []
        soup = self.makingtheSoup(mainUrl)
        tableSubs = soup.select("table > tbody > tr > td.a1 > a")
        for result in tableSubs:
            results = {}
            if "indonesian" in result.get("href"):
                results['Title'] = result.select("span")[1].text.encode("ascii", "ignore").translate(None, '\r\n\t ')
                results['Url']   = self.baseURL + result.get('href')
                urlsSubs.append(results)
        self.getUrlDownloads(urlsSubs)
    
    def getUrlDownloads(self, dicturlsSubs):
        directUrl = []
        for result in dicturlsSubs:
            results = {}
            soup = self.makingtheSoup(result['Url'])
            results['Title'] = result['Title']
            results['DirectLink'] = self.baseURL + soup.select("div.download > a#downloadButton")[0].get('href')
            directUrl.append(results)
        self.downloadFileWithURL(directUrl)