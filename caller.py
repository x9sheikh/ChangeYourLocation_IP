from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from browsermobproxy import Server
import time
from selenium.webdriver.common.proxy import Proxy, ProxyType
from pyvirtualdisplay import Display
import urllib


class SastaKhanaTesting():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", "51.38.80.159")
        profile.set_preference("network.proxy.http_port", 80)
        profile.update_preferences()

        #self.display = Display(visible=0, size=(800, 600))
        #self.display.start()
        #self.driver = webdriver.Firefox(firefox_profile=profile)

    def closeBrowser(self):
        driver = self.driver
        try:
            driver.close()
            print("LOGOUT *Successful* ")
        except:
            print("LOGOUT *Failed* ")

    def myIP(self):
        driver = self.driver
        driver.get("https://whatismyipaddress.com/")
        time.sleep(5)

    def trueCaller(self):
        urllib

    def google(self):
        #display = Display(visible=0, size=(800, 600))
        #display.start()

        # now Firefox will run in a virtual display.
        # you will not see the browser.
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 2)
        profile.set_preference("network.proxy.http", "51.38.80.159")
        profile.set_preference("network.proxy.http_port", 8080)
        profile.update_preferences()
        browser = webdriver.Firefox(firefox_profile=print())
        browser.get('https://whatismyipaddress.com/')
        time.sleep(5)
        print(browser.title)
        browser.quit()

        #display.stop()

sasta = SastaKhanaTesting(username='x9sheikh', password='@X9sheikh.usama')
# sasta.myIP()
# sasta.closeBrowser()
#sasta.trueCaller()
sasta.google()
#sasta.closeBrowser()













options = Options()
options.add_argument('--proxy-server=46.102.106.37:13228')
browser = webdriver.Chrome(executable_path='ChromeDriverPath', chrome_options=options)