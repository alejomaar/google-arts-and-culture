import time
import pandas as pd
from src.scraping.scripts import scripts
from selenium import webdriver


class ScrapingPictures():
    def __init__(self,driver_path,color_param:str) -> None:
        self.driver = webdriver.Chrome(executable_path = driver_path)
        self.delay = {
            "scroll_down": 3,
            "start": 3,
            "end": 3
        }
        self.color_param = color_param
        
                
    def open(self) -> None:
        base_url = 'https://artsandculture.google.com/color'
        target_page = f'{base_url}?col={self.color_param}'
        self.driver.get(target_page)
        print('Open page section {}'.format(self.color_param))
        
    def scroll_down(self,scrolls:int) -> None:
        for j in range(0, scrolls):
            self.driver.execute_script(scripts.scroll_down)
            time.sleep(self.delay['scroll_down']) 
        print('Finish scrolling down')    
        
    def scrape(self) -> pd.DataFrame:                
        try:
            data = self.driver.execute_script(scripts.pictures_info)
            df_pictures = pd.DataFrame(data)
            df_pictures['color'] = self.color_param
            return df_pictures
        except: 
            print('Something went wrong in: ',self.color_param)
            return pd.DataFrame(columns=['image','page','color'])

        