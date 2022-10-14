import asyncio
import csv
from re import L
import typing

import src.cmd_line_parser as cmd_line_parser


class CourseInfo(typing.NamedTuple):
    name: str
    provider: str
    description: str
    number_of_students: int
    number_of_ratings: int


baseurl = 'https://www.coursera.org/browse/'


async def gather_courses_links(http_client, category_name: str) -> list[str]:
    return ['link1', 'link2']


async def gather_courses_data(http_client, courses_links: list[str], workers_count: int):
    return [
        CourseInfo(name='Course1', provider='Provider1', description='Description1', number_of_students=1, number_of_ratings=1),
        CourseInfo(name='Course2', provider='Provider2', description='Description2', number_of_students=2, number_of_ratings=2)
    ]


async def main():
    # 1. Parse command line arguments
    parser = cmd_line_parser.Parser()
    # 2. Create http client
    http_client = None
    # 3. Gather list of links to courses
    courses_links = await gather_courses_links(http_client, category_name=parser.get_category_name())
    # 4. Collect courses info using max(workers_count, len(links_list) task pool
    courses_data = await gather_courses_data(
        http_client,
        courses_links=courses_links,
        workers_count=parser.get_workers_count()
    )
    # 5. Write to csv
    with open(parser.get_output_file_path(), 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(courses_data[0]._fields)
        csv_writer.writerows(courses_data)


if __name__ == '__main__':
    asyncio.run(main())
