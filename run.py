import asyncio
import csv
import typing

import src.cmd_line_parser as cmd_line_parser


class CourseInfo(typing.NamedTuple):
    name: str
    provider: str
    description: str
    number_of_students: int
    number_of_ratings: int


async def gather_courses_data(category_name: str, workers_count: int) -> list[CourseInfo]:
    return [
        CourseInfo(name='Course1', provider='Provider1', description='Description1', number_of_students=1, number_of_ratings=1),
        CourseInfo(name='Course2', provider='Provider2', description='Description2', number_of_students=2, number_of_ratings=2)
    ]


async def main():
    parser = cmd_line_parser.Parser()

    courses_list = await gather_courses_data(
        category_name=parser.get_category_name(),
        workers_count=parser.get_workers_count()
    )

    # Write to csv
    with open(parser.get_output_file_path(), 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(courses_list[0]._fields)
        csv_writer.writerows(courses_list)


if __name__ == '__main__':
    asyncio.run(main())
