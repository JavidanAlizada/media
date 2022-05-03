import requests


class Scrapper:

    def __init__(self, url):
        self.__url = url

    def __get_content(self):
        response_url = requests.get(self.__url)
        return response_url.text.split('mainEntityOfPage')[1:]

    def get_links(self):
        links = self.__get_content()
        formatted_links = [link.split(",")[0][4:-1] for link in links]
        return formatted_links
