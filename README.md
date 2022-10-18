# Coursera.org web scraper

The application gathers info about coursera.org courses matching particular category and results in CSV file containing info about courses.

## Install requirements

```sh
pip install -r ./requirements/requirements
```

## Usage

To get help or usage, run:
```sh
python src/run.py -h|--help | -u|--usage
```

## Unit tests

To perform tests, run:

```sh
pytest -vv ./tests
```

To install tests requirements:
```sh
pip install -r ./requirements/requirements.tests
```

## Category examples

- data-science
- business
- computer-science
- information-technology
- health
- language-learning

and other

## Known bugs

1. For some courses downloaded html doesn't contain some info such as number of students or course name. Looks like it depends on previously requested links. Here are these courses:

```
https://www.coursera.org/professional-certificates/google-project-management
https://www.coursera.org/professional-certificates/ibm-data-analyst
https://www.coursera.org/professional-certificates/google-it-support
```
