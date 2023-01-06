import time
import pandas as pd
from src.scraping.scripts import scripts
from selenium import webdriver

class Section():
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path = driver_path)
        self.delay = {
            "scroll_down": 3,
            "start": 3,
            "end": 3
        }
        self.scroll_down_times = 45
        
                
    def open(self,color):
        base_url = 'https://artsandculture.google.com/color'
        target_page = f'{base_url}?col={color}'
        self.driver.get(target_page)
        print('Open page section {}'.format(color))
        
    def scroll_down(self,scrolls:int):
        for j in range(0, scrolls):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.delay['scroll_down']) 
        print('Finish scrolling down')    
        
    def scrape(self)->list[dict]:        
        time.sleep(self.delay['start'])
        self.scroll_down(self.SCROLL_DOWN)
        time.sleep(self.delay['end'])
        
        picture_images = self.driver.execute_script(scripts.get_pictures_images)
        picture_pages= self.driver.execute_script(scripts.get_pictures_links)
        
        df_pictures = pd.DataFrame({'image_url': picture_images,'page': picture_pages})    
        
        return df_pictures
        