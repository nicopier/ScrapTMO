from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from lxml import etree, html
import re
import copy
import time

class VisorTMO():
    def __init__(self, url):
        self.dict_with_chapters = {}
        self.url = url
        self.driver = webdriver.Edge()
        self.driver.get(self.url)
        time.sleep(5) 

    def click_object(self, xpath):
        element_to_click = self.driver.find_element(By.XPATH, xpath)  # Now uses XPath
        element_to_click.click()
        time.sleep(0.1)

    def execu(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".list-group")
        listo_to_iter = range(1,len(elements)+1)
        for numerito in reversed(listo_to_iter):
            xpath = f'//*[@id="chapters"]/ul/li[{numerito}]'
            try:
                self.click_object(xpath)
            except:
                pass
        data = self.driver.page_source
        #tree = etree.parse(data)
        tree = html.fromstring(data)
        elements_with_onclick = tree.xpath('//*[@onclick]')
        for element in elements_with_onclick:
            onclick_value = element.get('onclick')#extraer el onclick
            match = re.search("collapseChapter\('(.*)'\)", onclick_value)
            if match:
                onclick_value_1 = match.group(1)
                try:
                    inside_xpath = f'//*[@id="{onclick_value_1}"]//a'
                    a = elements_with_onclick[2].xpath(inside_xpath)
                    webpage = a[-1].attrib
                    self.dict_with_chapters[element.text_content()] = webpage['href']
                except:
                    pass    

visorTMO = VisorTMO('https://visortmo.com/library/manga/11338/saitama-chainsaw-shoujo').execu()
