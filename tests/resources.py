from os import path


_CURRENT_DIR = path.dirname(__file__)
_RESOURCE_PATH = path.join(_CURRENT_DIR, 'resources')
_COURSE_PAGE_SCRAPER_RESOURCE_PATH = f'{_RESOURCE_PATH}/course_page_scraper'

def _read_course_scraper_html(filename):
    return open(f'{_COURSE_PAGE_SCRAPER_RESOURCE_PATH}/{filename}').read()

FOUNDATION_DATA_HTML_FILENAME = 'data_science.foundation_data.html'
FOUNDATION_DATA_HTML_CONTENT = _read_course_scraper_html(FOUNDATION_DATA_HTML_FILENAME)

# https://www.coursera.org//specializations/business-data-management-communication
# The course isn't started yet, so no students have enrolled
BUSINESS_DATA_HTML_FILENAME = 'data_science.business_data.html'
BUSINESS_DATA_HTML_CONTENT = _read_course_scraper_html(BUSINESS_DATA_HTML_FILENAME)

# https://www.coursera.org/projects/googlecloud-managing-deployments-using-kubernetes-engine-lfjkj
# Has unusual location for course name and description
IT_KUBERNETES_HTML_FILENAME = 'it.kubernetes.html'
IT_KUBERNETES_HTML_CONTENT = _read_course_scraper_html(IT_KUBERNETES_HTML_FILENAME)


# Helps avoid printing html content on test execution
html_content = {
    FOUNDATION_DATA_HTML_FILENAME: FOUNDATION_DATA_HTML_CONTENT,
    BUSINESS_DATA_HTML_FILENAME: BUSINESS_DATA_HTML_CONTENT,
    IT_KUBERNETES_HTML_FILENAME: IT_KUBERNETES_HTML_CONTENT
}
