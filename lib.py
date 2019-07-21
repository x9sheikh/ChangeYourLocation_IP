from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy

proxy_use= "176.58.118.148:8080"
desired_capability = webdriver.DesiredCapabilities.FIREFOX
desired_capability['proxy'] = {
    'proxyType': "manual",
    'httpProxy': proxy_use,
    'ftpProxy': proxy_use,
    'sslProxy': proxy_use,
        }
queryURL = "https://www.truecaller.com/"
browser = webdriver.Firefox(capabilities=desired_capability)
browser.get(queryURL)