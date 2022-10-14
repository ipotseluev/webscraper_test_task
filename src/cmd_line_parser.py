from typing import Optional
import argparse


def workers_count_type(s: str):
    if int(s) < 1:
        raise ValueError("Workers count must be greater than 0")
    return int(s)


class Parser:
    def __init__(self, args: Optional[list[str]] = None):
        parser = argparse.ArgumentParser(description='Get info about Coursera courses from particular category')
        parser.add_argument(
            'category',
            help='name of a subject which groups courses'
        )
        parser.add_argument(
            '-w',
            '--workers-count',
            type=workers_count_type,
            default=1,
            help='maximum number of parallel workers which poll the web site'
        )
        parser.add_argument(
            '-o',
            '--output-file',
            default='courses.csv',
            help="path to output csv file"
        )
        self.args = parser.parse_args(args)

    def get_category_name(self) -> str:
        return self.args.category

    def get_workers_count(self) -> int:
        return self.args.workers_count

    def get_output_file_path(self) -> str:
        return self.args.output_file
