from selenium import webdriver

"""
service = webdriver.ChromeService(executable_path = 'chromedriver.exe')
options = webdriver.ChromeOptions() 
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service)
"""
driver = webdriver.Chrome()
driver.get("https://www.google.com")

input("....")

