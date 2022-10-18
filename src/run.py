import asyncio

from aio_http_reader import AiohttpReader
from coursera_web_scraper import CourseraWebScraper
import cmd_line_parser as cmd_line_parser


async def run(parser: cmd_line_parser.Parser):
    async_http_reader = AiohttpReader()
    exit_code = 0
    try:
        application = CourseraWebScraper(async_http_reader=async_http_reader)
        await application.scrap_courses_info(
            courses_category=parser.get_category_name(),
            workers_count=parser.get_workers_count(),
            output_file_path=parser.get_output_file_path()
        )
    finally:
        await async_http_reader.close()
    return exit_code


if __name__ == '__main__':
    parser = cmd_line_parser.Parser()
    exit_code = asyncio.run(run(parser=parser))
    quit(code=exit_code)
