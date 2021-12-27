from typing import _SpecialForm
from bs4 import BeautifulSoup
import requests
import pandas as pd

class Scraping():
    count =0
    remove_url = ["facebook","twitter","instagram","youtube"]

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    def __init__(self,URL):
        self.URL = URL
        self.BASEURL = URL

    def CreateSoup(self,Url):
        r = requests.get(Url,headers=self.headers)
        htmlContent = r.content
    # print(htmlContent)

        soup = BeautifulSoup(htmlContent,'html.parser')
        return(soup.body)

    def extract_url(self,urls):
        href_list = []
        l=[]
        for url in urls:
            soup = self.CreateSoup(url)
            try:
                for a in soup.find_all('a', href=True,recursive=True):
                    if len(a['href'])<2 or a['href'][0] =='#' or a['href'] in Scraping.remove_url:
                        continue
                    else:
                        if "https" in a['href']:
                            link = a['href']
                            if link not in href_list :
                                href_list.append(link)
                        else:
                            # print(a['href'])
                            # print(self.BASEURL)
                            link = self.BASEURL+a['href'] 
                            if link not in href_list:

                                href_list.append(self.BASEURL+a['href'])
            except:
                pass

                # print(len(href_list))
                # rmove_list= self.remove_duplicates(urls,href_list)
                # l=l+rmove_list
                # l = list(set(l))
            # print(len(l))

        return(href_list)

    def get_data_from_url(self,list_of_url):
        count = 0
        image_list =[]
        for urls in list_of_url:
            # print(list_of_url)
            list_of_images = []
            soup = self.CreateSoup(urls)
            try:
                for item in soup.find_all('img'):
                    if item['src'][0] == '/':
                        # print(item['src'])
                        image_url=self.BASEURL+item['src']
                        print(image_url)

                # for a in soup.find_all('a'):
                #     print(a)
                #     if a.img and a.img['src'][0] == '/':
                #         image_url=self.BASEURL+a.img['src']
                #         if image_url not in list_of_images: 
                #         # [list_of_images.append(image_url) for image_url in a if item not in b]
                        list_of_images.append(image_url)
                image_list.append(list_of_images)
            except:
                pass
        # return(image_list)

    def remove_duplicates(self,test_url,list_of_url):
        # print("test",test_url)
        # print("list",list_of_url)
        # list_of_url = list_of_url+test_url
        # break
        return(list(set(list_of_url)))
        pass



                
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
# uRL =  ['https://www.lincolntownshipmotors.ca/']


# URL = "https://www.steelechryslerhalifax.com/"
# uRL = ["https://www.steelechryslerhalifax.com/"]




# URL = "https://www.cardekho.com/cars/#brands"

# pageScrape = Scraping(URL)
# s = pageScrape.extract_url(uRL)
# print("s>>>",s)
# print(s[0])

# x= "https://www.steelechryslerhalifax.com//new-inventory/index.htm?year=2021&make=Jeep&model=Grand Cherokee&gvBodyStyle=VUS"
# url = pageScrape.extract_url(s)
# print(type(url))
# print(len(url))
# print(url)
# print(len(list(set(url+s))))

# url_info = pageScrape.extract_url(url)
# print(url_info)



# s= [s.append(item) for item in url if item not in s]
# s = s+url
# print(len(list(set(s))))
# removed_url=pageScrape.remove_duplicates(s,url)
# print(len(removed_url))
# print("url>>>",len(url))

# remove_url = ["facebook","twitter","instagram","youtube,Contact,Contact-Us,Contact+Us"]
# u = ['https://ta-in.facebook.com/sharer.php?u=https%3A%2F%2Fwww.steelechryslerhalifax.com%2Fcontact.htm&t=Contact+Us',
# 'https://www.youtube.com/howyoutubeworks?utm_campaign=ytgen&utm_source=ythp&utm_medium=LeftNav&utm_content=txt&u=https%3A%2F%2Fwww.youtube.com%2Fhowyoutubeworks%3Futm_source%3Dythp%26utm_medium%3DLeftNav%26utm_campaign%3Dytgen']
# # x = "youtube"
# l=[]
# for ur in remove_url:
#     for urr in url_info:
#         if (ur in urr):
#             # print(urr)
#             pass
#         else:
#             l.append(urr)
# print(l)
# print(len(l))
# print(x in u)
# v = [v for v in url if v not in remove_url]
# print(len(s))
# d={}
# l= []0
# print('s',s)
# pageScrape.get_data_from_url(s[9])
# for link in s:
# sl=pageScrape.extract_url(s[0])

#     print("s1",sl)