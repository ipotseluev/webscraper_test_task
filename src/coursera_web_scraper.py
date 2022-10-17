import typing
import csv


class CourseInfo(typing.NamedTuple):
    name: str
    provider: str
    description: str
    number_of_students: int
    number_of_ratings: int


class CourseraWebScraper:
    def __init__(self):
        self.baseurl = 'https://www.coursera.org/browse/'
        self.http_reader_client = None

    async def _gather_courses_links(self, courses_category: str) -> list[str]:
        return ['link1', 'link2']

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
