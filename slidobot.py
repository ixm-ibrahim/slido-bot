from selenium import webdriver
import time
import sys
import getopt
import _thread

class SlidoBot:
    def __init__(self, hash=None, xpath=None, driver=None, scrolls=None, question=None):
        if hash == None or xpath == None or driver == None or scrolls == None or question == None:
            raise("Invalid arg")
        self.hash = hash
        self.xpath = xpath
        self.driver = driver
        self.scrolls = scrolls
        self.question = question
        if "chrome" in self.driver:
            self.driver = webdriver.Chrome(self.driver)
        else:
            self.driver = webdriver.Firefox(executable_path=self.driver)
    def closeBrowser(self):
        self.driver.close()

    def vote(self):
        self.driver.get("https://app.sli.do/event/" + self.hash + "/live/questions")
        time.sleep(5)
        for i in range(0,int(self.scrolls)):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        click_elem = self.driver.find_element("xpath", "//body/div[@id='root']/div[3]/div[2]/div[1]/div[2]/div[5]/div[1]//div[contains(div[1]/div[2]/span,'" + self.question + "')]/div[1]//div[1]/div[3]/div[2]/button[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", click_elem)
        time.sleep(1)
        #click_elem.click()
        self.driver.execute_script("arguments[0].click();", click_elem)
        time.sleep(1)

# hash # xpath # times
def main():
    HASH = ""
    #XPATH = ""
    DRIVER = ""
    QUESTION = ""
    SCROLLS = 0
    VOTES = 1
    try:
        options, args = getopt.getopt(
            sys.argv[1:], "h:x:d:v:q:s:",
            ["hash=", "xpath=", "driver=", "votes="])
        for name, value in options:
            if name in ('-h', '--hash'):
                HASH = value
            #if name in ('-x', '--xpath'):
            #    XPATH = value
            if name in ('-d', '--driver'):
                DRIVER = value
            if name in ('-q', '--question'):
                QUESTION = value
            if name in ('-s', '--scrolls'):
                SCROLLS = value
            if name in ('-v', '--votes'):
                VOTES = value

    except getopt.GetoptError as err:
        print(str(err))
        print("Invalid args!")
        sys.exit(1)

    for i in range(1, int(VOTES)+1):
        BOT = SlidoBot(HASH, "", DRIVER, SCROLLS, QUESTION)
        #_thread.start_new_thread( BOT.vote, () )
        BOT.vote()
        BOT.closeBrowser()
        print("Votes: " + str(i))
if __name__ == "__main__":
    print("Have fun.")
    main()
