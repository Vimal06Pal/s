from scrape_href import Scraping


# URL =  'https://www.lincolntownshipmotors.ca/'
# uRL =  ['https://www.lincolntownshipmotors.ca/']

URL = "https://www.steelechryslerhalifax.com/"
uRL = ["https://www.steelechryslerhalifax.com/"]
pageScrape = Scraping(URL)
# s = pageScrape.extract_url(uRL)
# # print("s>>>",s)

# url = pageScrape.extract_url(s)
# print(url)

x=['https://www.steelechryslerhalifax.com/new/Jeep/2021-Jeep-Gladiator-1d5d460f0a0e09af69981ba12b40257f.htm']
image = pageScrape.get_data_from_url(x)
print(image)

# url_info = pageScrape.extract_url(url)
# print(url_info)
