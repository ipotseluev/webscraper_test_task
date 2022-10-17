import asyncio

from src.coursera_web_scraper import CourseraWebScraper
import src.cmd_line_parser as cmd_line_parser

if __name__ == '__main__':
    parser = cmd_line_parser.Parser()
    application = CourseraWebScraper()
    exit_code = asyncio.run(
        application.scrap_courses_info(
            courses_category=parser.get_category_name(),
            workers_count=parser.get_workers_count(),
            output_file_path=parser.get_output_file_path()
        )
    )
    quit(code=exit_code)
