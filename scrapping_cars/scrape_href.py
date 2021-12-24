from typing import _SpecialForm
from bs4 import BeautifulSoup
import requests
import pandas as pd

class Scraping():
    count =0
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    def __init__(self,URL):
        self.URL = URL
        self.BASEURL = URL

    def CreateSoup(self,Url):
        r = requests.get(URL,headers=self.headers)
        htmlContent = r.content
    # print(htmlContent)

        soup = BeautifulSoup(htmlContent,'html.parser')
        return(soup)

    def extract_url(self,URL):
        href_list = []
        soup = self.CreateSoup(URL)
        for a in soup.find_all('a', href=True,recursive=True):
            if len(a['href'])<2 or a['href'][0] =='#':
                pass
            else:
                if "https" in a['href']:
                    link = a['href']
                    href_list.append(link)
                else:
                    link = self.BASEURL+a['href']             
                    href_list.append(self.BASEURL+a['href'])

        return(href_list)

    def get_data_from_url(self,list_of_url):
        count = 0
        # for urls in list_of_url:
        print(list_of_url)
        list_of_images = []
        soup = self.CreateSoup(list_of_url)
        
        for a in soup.find_all('a'):
            # print(a)
            if a.img and a.img['src'][0] == '/':
                image_url=self.BASEURL+a.img['src']
                list_of_images.append(image_url)
        print(list_of_images)



                
        # print(list_of_images)
            # images = soup.findAll('img')
            # for image in images:
            #     print(image['src'])
                # try:
                #     if (image['src'][0]) =='/':
                #         # print(image['src'][0])
                #         print(self.BASEURL+image['src'])
                #         image_url=self.BASEURL+image['src']
                #         # print(image_url)
                #         list_of_images.append(image_url)
                #     else:
                #         # print(image['src'])
                #         pass

                # except:
                #     pass


        # pass






# URL =  'https://www.lincolntownshipmotors.ca/'

URL = "https://www.steelechryslerhalifax.com/"



# URL = "https://www.cardekho.com/cars/#brands"

pageScrape = Scraping(URL)
s = pageScrape.extract_url(URL)
# print(s)
# d={}
# l= []0
# print('s',s)
pageScrape.get_data_from_url(s[9])
# for link in s:
# sl=pageScrape.extract_url(s[0])

#     print("s1",sl)