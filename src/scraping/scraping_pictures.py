import time
import pandas as pd
from src.scraping.scripts import scripts
from selenium import webdriver
from typing import Union


class ScrapingPictures():
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path = driver_path)
        self.delay = {
            "scroll_down": 3,
            "start": 3,
            "end": 3
        }
        self.scroll_down_times = 45
        
                
    def open(self,color:str):
        base_url = 'https://artsandculture.google.com/color'
        target_page = f'{base_url}?col={color}'
        self.driver.get(target_page)
        print('Open page section {}'.format(color))
        
    def scroll_down(self,scrolls:int):
        for j in range(0, scrolls):
            self.driver.execute_script(scripts.scroll_down)
            time.sleep(self.delay['scroll_down']) 
        print('Finish scrolling down')    
        
    def scrape(self) -> Union[pd.DataFrame,None]:                
        try:
            data = self.driver.execute_script(scripts.pictures_info)
            df_pictures = pd.DataFrame(data)
            return df_pictures
        except: 
            print('Error')
            return None

        