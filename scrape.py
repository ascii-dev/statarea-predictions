"""
    Program => Scrape data from SoccerWay
    Author => Samuel Afolaranmi
    Date => 01-04-2018
"""
import time
from bs4 import BeautifulSoup
import requests

URL = 'https://www.statarea.com/predictions/date/{}/competition'

def scrape():
    """
        Scrape data from SoccerWay
    """
    url = URL.format(time.strftime("%Y-%m-%d"))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # matches = soup.find_all('div', class_="cmatch")

    # Get all competitions
    all_competitions = []
    competitions = soup.find_all('div', class_="competition")

    # Remove divs holding advertisements
    for item in competitions:
        league_name = item.find('div', {'class':'header'}).find('div', {'class':'name'}).get_text()
        if league_name != 'Advertisement':
            all_competitions.append(item)
    return all_competitions

def get_league():
    """
        Gets soccer data from the function scrape's raw data
    """
    all_scrape = scrape()
    by_league = []
    elements = []
    for item in all_scrape:
        leagues = {}
        predictions = {}
        # Get the league from the header div
        leagues['name'] = item.find('div', {'class':'header'}).find('div', {'class':'name'}).get_text()

        # prediction = item.find('div', {'class':'body'})
        # matches = prediction.find("div", {"class":"match"})
        # for match in matches:
        #     predictions['match_time'] = match.find("div", {"class":"date"}).get_text()
        # leagues['details'] = predictions
        elements.append(leagues)
    return elements

# def get_data():
#     """
#         Gets soccer data from the function scrape's raw data
#     """
#     all_predictions = scrape()
#     prediction_list = []
#     for item in all_predictions:
#         prediction = {}
#         #Get the prediction details in variables
#         prediction['match_time'] = item.find("div", {"class":"time"}).get_text()
#         prediction['home_team'] = item.find("div", {"class":"teams"}).select("a")[0].get_text()
#         prediction['away_team'] = item.find("div", {"class":"teams"}).select("a")[1].get_text()
#         prediction['tip'] = item.find("div", {"class":"value"}).find("div").get_text()
#         # print("{} => {} - {} => {}".format(match_time, home_team, away_team, tip))
#         prediction_list.append(prediction)
#     return prediction_list

def main():
    """
        Prints out the scraped data
    """
    # the_data = get_data()
    return get_league()

if __name__ == '__main__':
    main()
