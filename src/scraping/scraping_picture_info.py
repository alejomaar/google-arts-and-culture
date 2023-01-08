import time
import pandas as pd
from src.scraping.scripts import scripts
from selenium import webdriver


class ScrapingPictureInfo():
    def __init__(self,driver_path,picture_page:str) -> None:
        self.driver = webdriver.Chrome(executable_path = driver_path)
        self.picture_page = picture_page
        self.delay = 3        
                
    def open(self) -> None:
        target_page = self.picture_page
        self.driver.get(target_page)
          
    def scrape(self) -> dict:                
        try:
            data = self.driver.execute_script(scripts.get_picture_info)
            info = {"page":self.picture_page,"data":data}
            return info
        except: 
            print('Something went wrong in: ',self.picture_page)
            return {"page":"","data":""}

        