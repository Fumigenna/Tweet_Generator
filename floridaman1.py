
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class wait_for_more_than_n_elements_to_be_present(object):
    def __init__(self, locator, count):
        self.locator = locator
        self.count = count

    def __call__(self, driver):
        try:
            elements = EC._find_elements(driver, self.locator)
            return len(elements) > self.count
        except StaleElementReferenceException:
            return False


url = "https://twitter.com/_floridaman"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# initial wait for the tweets to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li[data-item-id]")))

# scroll down to the last tweet until there is no more tweets loaded
while True:
    tweets = driver.find_elements_by_css_selector("li[data-item-id]")
    number_of_tweets = len(tweets)

    driver.execute_script("arguments[0].scrollIntoView();", tweets[-1])

    try:
        wait.until(wait_for_more_than_n_elements_to_be_present((By.CSS_SELECTOR, "li[data-item-id]"), number_of_tweets))
    except TimeoutException:
        break

tweet_element = driver.find_elements_by_class_name('tweet-text')
tweets =[]
for tweet in tweet_element:
    tweets.append((tweet.text).encode('ascii','ignore'))
florida_man_tweets = []
file = open('floridamantweets.txt','w')
for tweet in tweets:
    if tweet.startswith('Florida Man'):
        florida_man_tweets.append(tweet)
        file.write(tweet + '\n')
file.close()
