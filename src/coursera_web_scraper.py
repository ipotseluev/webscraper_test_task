from bs4 import BeautifulSoup
import typing
import csv

from interfaces.async_http_reader import AsyncHttpReader


class CourseInfo(typing.NamedTuple):
    name: str
    provider: str
    description: str
    number_of_students: int
    number_of_ratings: int


class CourseraWebScraper:
    def __init__(self, async_http_reader: AsyncHttpReader):
        self.baseurl = 'https://www.coursera.org/'
        self.async_http_reader = async_http_reader

    async def _gather_courses_links(self, courses_category: str) -> list[str]:
        category_browse_url = f"{self.baseurl}/browse/{courses_category}"
        html_text = await self.async_http_reader.get_text(url=category_browse_url)
        soup = BeautifulSoup(html_text, "html.parser")
        product_cards = soup.findAll('div', class_='rc-ProductCard')
        courses = [card for card in product_cards if card.find('label', class_='rc-CardText css-1feobmm').string == 'Course']
        courses_links = [course.find('a', class_="CardText-link").attrs['href'] for course in courses]
        return courses_links

    async def _gather_courses_data(self, courses_links: list[str], workers_count: int) -> list[CourseInfo]:
        return [
            CourseInfo(name='Course1', provider='Provider1', description='Description1', number_of_students=1, number_of_ratings=1),
            CourseInfo(name='Course2', provider='Provider2', description='Description2', number_of_students=2, number_of_ratings=2)
        ]

    async def scrap_courses_info(self, courses_category: str, workers_count: int, output_file_path: str):
        # 1. Collect links to courses from the given category
        courses_links = await self._gather_courses_links(courses_category)

        # 2. Collect courses info using max(workers_count, len(links_list) task pool
        courses_data = await self._gather_courses_data(
            courses_links=courses_links,
            workers_count=workers_count
        )

        # 3. Write to csv
        with open(output_file_path, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(courses_data[0]._fields)
            csv_writer.writerows(courses_data)
