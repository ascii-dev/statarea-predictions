"""
    Program => Scrape data from SoccerWay
    Author => Samuel Afolaranmi
    Date => 01-04-2018
"""
import time
from bs4 import BeautifulSoup
import requests
# import urllib

URL = 'https://www.statarea.com/predictions/date/{}/starttime'

def scrape():
    """
        Scrape data from SoccerWay
    """
    # query = urllib.quote(URL)
    url = URL.format(time.strftime("%Y-%m-%d"))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all('div', class_="cmatch")


def get_data():
    """
        Gets soccer data from the function scrape's raw data
    """
    all_predictions = scrape()
    prediction_list = []
    for item in all_predictions:
        prediction = {}
        #Get the prediction details in variables
        prediction['match_time'] = item.find("div", {"class":"time"}).get_text()
        prediction['home_team'] = item.find("div", {"class":"teams"}).select("a")[0].get_text()
        prediction['away_team'] = item.find("div", {"class":"teams"}).select("a")[1].get_text()
        prediction['tip'] = item.find("div", {"class":"value"}).find("div").get_text()
        # print("{} => {} - {} => {}".format(match_time, home_team, away_team, tip))
        prediction_list.append(prediction)
    return prediction_list

def main():
    """
        Prints out the scraped data
    """
    the_data = get_data()
    return the_data

if __name__ == '__main__':
    main()
