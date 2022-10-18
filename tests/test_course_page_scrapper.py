import pytest

from src.course_page_scraper import CoursePageScraper
import tests.resources as resources

# region Negative tests

def test_get_course_name_negative():
    obj = CoursePageScraper(html='')
    assert obj.get_course_name() == 'N/A'


def test_get_students_count_negative():
    obj = CoursePageScraper(html='')
    assert obj.get_students_count() == 'N/A'


def test_get_ratings_count_negative():
    obj = CoursePageScraper(html='')
    assert obj.get_ratings_count() == 'N/A'


def test_get_description_negative():
    obj = CoursePageScraper(html='')
    assert obj.get_description() == 'N/A'


def test_get_provider_negative():
    obj = CoursePageScraper(html='')
    assert obj.get_provider() == 'N/A'


def test_get_first_instructor_negative():
    obj = CoursePageScraper(html='')
    assert obj.get_first_instructor() == 'N/A'

# endregion

# region Positive tests

@pytest.mark.parametrize(
    argnames='html_filename, expected_result',
    argvalues= [
        (resources.FOUNDATION_DATA_HTML_FILENAME, 'Foundations: Data, Data, Everywhere'),
        (resources.IT_KUBERNETES_HTML_FILENAME, 'Managing Deployments Using Kubernetes Engine')
    ]
)
def test_get_course_name_positive(html_filename: str, expected_result: str):
    obj = CoursePageScraper(html=resources.html_content[html_filename])
    assert obj.get_course_name() == expected_result


@pytest.mark.parametrize(
    argnames='html_filename, expected_result',
    argvalues= [
        (resources.FOUNDATION_DATA_HTML_FILENAME, 1259670),
        (resources.BUSINESS_DATA_HTML_FILENAME, 'N/A'),
    ]
)
def test_get_students_count_positive(html_filename: str, expected_result: str):
    obj = CoursePageScraper(html=resources.html_content[html_filename])
    assert obj.get_students_count() == expected_result


@pytest.mark.parametrize(
    argnames='html_filename, expected_result',
    argvalues= [
        (resources.FOUNDATION_DATA_HTML_FILENAME, 57850),
    ]
)
def test_get_ratings_count_positive(html_filename: str, expected_result: str):
    obj = CoursePageScraper(html=resources.html_content[html_filename])
    assert obj.get_ratings_count() == expected_result


@pytest.mark.parametrize(
    argnames='html_filename, expected_result',
    argvalues= [
        (resources.FOUNDATION_DATA_HTML_FILENAME, 'This is the first course in the blahblah.'),
        (resources.IT_KUBERNETES_HTML_FILENAME, 'This is a self-paced lab blahblah')
    ]
)
def test_get_description_positive(html_filename: str, expected_result: str):
    obj = CoursePageScraper(html=resources.html_content[html_filename])
    assert obj.get_description() == expected_result


@pytest.mark.parametrize(
    argnames='html_filename, expected_result',
    argvalues= [
        (resources.FOUNDATION_DATA_HTML_FILENAME, 'Google'),
    ]
)
def test_get_provider_positive(html_filename: str, expected_result: str):
    obj = CoursePageScraper(html=resources.html_content[html_filename])
    assert obj.get_provider() == expected_result

# endregion
