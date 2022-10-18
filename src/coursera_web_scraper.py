from bs4 import BeautifulSoup
import csv
import typing

from course_page_scraper import CoursePageScraper
from interfaces.async_http_reader import AsyncHttpReader


class CourseInfo(typing.NamedTuple):
    name: str
    provider: str
    description: str
    students_count: int
    ratings_count: int


class CourseraWebScraper:
    def __init__(self, async_http_reader: AsyncHttpReader):
        self.BASE_URL = 'https://www.coursera.org'
        self.async_http_reader = async_http_reader

    async def _get_courses_links(self, courses_category: str) -> list[str]:
        category_browse_url = f"{self.BASE_URL}/browse/{courses_category}"
        html_text = await self.async_http_reader.get_text(url=category_browse_url)
        soup = BeautifulSoup(html_text, "html.parser")
        product_cards = soup.findAll('div', class_='rc-ProductCard')
        courses_links = [card.find('a', class_='CardText-link').get('href') for card in product_cards]
        return courses_links

    async def _get_course_data(self, course_link: str, course_category: str) -> CourseInfo:
        link = f'{self.BASE_URL}{course_link}'
        page_text = await self.async_http_reader.get_text(url=link)
        course_scrapper = CoursePageScraper(html=page_text)

        name = course_scrapper.get_course_name()
        students_count = course_scrapper.get_students_count()
        ratings_count = course_scrapper.get_ratings_count()
        description = course_scrapper.get_description()
        provider = course_scrapper.get_provider()

        assert isinstance(name, str)
        assert isinstance(provider, str)
        return CourseInfo(
            name=name,
            provider=provider,
            description=description,
            students_count=students_count,
            ratings_count=ratings_count
        )
    async def _collect_courses_data(
            self,
            courses_links: list[str],
            courses_category: str,
            workers_count: int
        ) -> list[CourseInfo]:
        result = []
        for i in range(len(courses_links)):
            print(f"[{i + 1}/{len(courses_links)}] Processing {courses_links[i]}")
            result.append(await self._get_course_data(course_link=courses_links[i], course_category=courses_category))
        return result

    async def scrap_courses_info(self, courses_category: str, workers_count: int, output_file_path: str):
        # 1. Collect links to courses from the given category
        courses_links = await self._get_courses_links(courses_category)

        # 2. Collect courses info using max(workers_count, len(links_list) task pool
        courses_data = await self._collect_courses_data(
            courses_category=courses_category,
            courses_links=courses_links,
            workers_count=workers_count
        )

        # 3. Write to csv
        with open(output_file_path, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(courses_data[0]._fields)
            csv_writer.writerows(courses_data)
