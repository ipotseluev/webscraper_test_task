from bs4 import BeautifulSoup
import functools
import re


def error_fallback(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return "N/A"
    return wrapper


class CoursePageScraper:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.course_provider_regex = re.compile('Partner__title')

    @error_fallback
    def get_course_name(self):
        if not (text := self.soup.find(attrs={'data-e2e': "xdp-banner-title"})):
            text = self.soup.find(attrs={'id': "programMiniModalName"})
        return text.string

    @error_fallback
    def get_students_count(self):
        return int(self.soup.find('div', class_="_1fpiay2").text.split('already enrolled')[0].replace(',',''))

    @error_fallback
    def get_ratings_count(self):
        return int(self.soup.find(attrs={'data-test': 'ratings-count-without-asterisks'}).text.split(' ratings')[0].replace(',', ''))

    @error_fallback
    def get_description(self):
        if not (text := self.soup.find('div', class_='description')):
            text = self.soup.find('div', class_="css-6ohxmr")
        return text.text.strip()

    @error_fallback
    def get_provider(self):
        return self.soup.find('h3', class_=self.course_provider_regex).string

    @error_fallback
    def get_first_instructor(self):
        return self.soup.find('div', class_="_y1d9czk").text.split('\xa0')[0].strip().split('+')[0].strip()
