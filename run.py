import asyncio

import src.cmd_line_parser as cmd_line_parser


async def main():
    parser = cmd_line_parser.Parser()
    print(f"{parser.get_category_name()}")
    print(f"{parser.get_workers_count()}")
    print(f"{parser.get_output_file_path()}")


if __name__ == '__main__':
    asyncio.run(main())
