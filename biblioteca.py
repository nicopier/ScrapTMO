import requests
from bs4 import BeautifulSoup
import copy

class BibliotecaScrapper():
    def __init__(self):
        self.export_json = {}
        self.all_data_template = {"url":None, "score":None, "type":None, "demograpy":None}
        self.biblioteca_url = "https://visortmo.com/library?_pg=1&page="
        self.page = 1
        self.webpage_searcher = f"{self.biblioteca_url}{self.page}"
        
    def basic_scrape(self):
        response = requests.get(self.webpage_searcher, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"})
        
        soup = BeautifulSoup(response.text, 'html.parser')
        mangas = soup.find_all(class_='element')
        
        for a in mangas:
            manga_url = a.find("a").attrs
            manga_title = a.find(class_ ="thumbnail-title").text
            self.all_data_template["url"] = manga_url["href"]
            self.all_data_template["score"] = a.find(class_ ="score").text
            self.all_data_template["type"] = a.find(class_= "book-type").text
            self.all_data_template["demograpy"] = a.find(class_= "demography").text
            manga_title = manga_title.strip('\n')
            self.export_json[manga_title] = copy.deepcopy(self.all_data_template)
    
    def midd_scrapper(self):
        for page in range(1,1400):
            self.basic_scrape()
            self.page += 1
            
#Scrapper().midd_scrapper()
