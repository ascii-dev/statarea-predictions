"""
    Program => Scrape data from StatArea
    Author => Samuel Afolaranmi
    Date => 01-04-2018
"""
import time
from bs4 import BeautifulSoup
import requests

URL = 'https://www.statarea.com/predictions/date/{}/competition'


def scrape():
    """
    Scrape data from StatArea
    """
    url = URL.format(time.strftime("%Y-%m-%d"))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Get all competitions
    all_competitions = []
    competitions = soup.find_all('div', class_="competition")

    # Remove divs holding advertisements
    for item in competitions:
        league_name = item.find(
            'div',
            {'class': 'header'}
        ).find(
            'div',
            {'class': 'name'}
        ).get_text()
        if league_name != 'Advertisement':
            all_competitions.append(item)
    return all_competitions


def get_league():
    """
    Gets soccer data from the function scrape's raw data
    """
    all_scrape = scrape()
    elements = []
    for item in all_scrape:
        leagues = {}
        league_predictions = []

        # Get the league from the header div
        leagues['name'] = item.find(
            'div',
            {'class': 'header'}
        ).find(
            'div',
            {'class': 'name'}
        ).get_text()

        prediction = item.find('div', {'class': 'body'})
        matches = prediction.find_all("div", {"class": "match"})

        for match in matches:
            predictions = {}
            matchrow = match.find("div", {"class": "matchrow"})
            predictions['match_time'] = match.find("div", {"class": "date"}).get_text()
            predictions['tip'] = matchrow.find(
                "div",
                {"class": "tip"}
            ).find(
                "div",
                {"class": "value"}
            ).find("div").get_text()
            predictions['home_team'] = matchrow.find(
                "div",
                {"class": "teams"}
            ).find(
                "div",
                {"class": "hostteam"}
            ).find(
                "div",
                {"class": "name"}
            ).find("a").get_text()
            predictions['away_team'] = matchrow.find(
                "div",
                {"class": "teams"}
            ).find(
                "div",
                {"class": "guestteam"}
            ).find(
                "div",
                {"class": "name"}
            ).find("a").get_text()
            league_predictions.append(predictions)

            # Get statistics details             
            stats = []
            statsrow = match.find("div", {"class": "inforow"}).find("div", {"class": "coefrow"})
            all_stats = statsrow.find_all("div", {"class": "coefbox"})
            for stat in range(0, len(all_stats)):
                stats.append(all_stats[stat].get_text())
            predictions['stats'] = stats[11:]
        
        leagues['details'] = league_predictions
        elements.append(leagues)
    return elements


def main():
    """
    Prints out the scraped data
    """
    return get_league()


if __name__ == '__main__':
    main()
