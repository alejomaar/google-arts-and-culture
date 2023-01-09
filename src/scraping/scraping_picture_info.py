from typing import Any
import pandas as pd
from src.scraping.scripts import scripts
from selenium import webdriver
import sqlite3
import pyprojroot
from pathlib  import Path

class ConnPictureinfo():
    def __init__(self) -> None:
        self.conn = self.connection()

    def connection(self) -> sqlite3.Connection:
        root_path =  pyprojroot.here()
        data_processed_folder = (root_path / "data"/'processed')
        conn = sqlite3.connect(data_processed_folder/'picture_info.db')
        return conn 
    
    def create_table(self)->None:
        query="""
        CREATE TABLE IF NOT EXISTS picture_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            picture_url TEXT,
            data TEXT,
            isReady INTEGER
        )
        """
        self.conn.execute(query)

class ScrapingPictureInfo():
    def __init__(self,driver_path,picture_page:str) -> None:
        self.driver = webdriver.Chrome(executable_path = driver_path)
        self.picture_page = picture_page
        self.conn = self.connection()

    def connection(self) -> None:
        root_path =  pyprojroot.here()
        data_processed_folder = (root_path / "data"/'processed')
        conn = sqlite3.connect(data_processed_folder/'picture_info.db')
        return conn 

    
                
                
    def open(self) -> None:
        target_page = self.picture_page
        self.driver.get(target_page)
        
          
    def scrape(self) -> dict:                
        try:
            data = self.driver.execute_script(scripts.get_picture_info)
            #info = {"page":self.picture_page,"data":data}
            
            
            return info
        except: 
            print('Something went wrong in: ',self.picture_page)
            return {"page":"","data":""}

        