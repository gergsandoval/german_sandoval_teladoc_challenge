from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

class SeleniumService:

    def __init__(self, context):
        self.context = context
    
    def type_on(self, by, text):
        self.context.driver.find_element(by[0], by[1]).send_keys(text)
        time.sleep(1)

    def click_on(self, by):
        self.context.driver.find_element(by[0], by[1]).click()
        time.sleep(1)

    def get_text_of(self, by):
        return self.context.driver.find_element(by[0], by[1]).text
        
    def select_by_visible_text(self, by, text):
        select = Select(self.context.driver.find_element(by[0], by[1]))
        select.select_by_visible_text(text)

    def visit_page(self, page):
        self.context.driver.get(page)

    def get_table_rows(self, by):
        table = self.context.driver.find_element(by[0], by[1])
        return table.find_elements(By.CSS_SELECTOR, "tbody > tr")
    
    def is_checked(self, tr, index):
        return self.get_td_element(tr, index).find_element(By.TAG_NAME, "input").is_selected()
    
    def get_text_inside_row(self, row, index):
        return self.get_td_element(row, index).text

    def get_td_element(self, tr, index):
        return tr.find_elements(By.TAG_NAME, "td")[index]