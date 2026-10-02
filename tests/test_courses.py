import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

CREATE_COURSE_URL = (
    'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
)


@pytest.mark.courses
@pytest.mark.regression
def test_successful_create_course(create_courses_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_courses_page.visit(CREATE_COURSE_URL)
    create_courses_page.check_visible_create_course_title()
    create_courses_page.check_disabled_create_course_button()
    create_courses_page.check_visible_image_preview_empty_view()
    create_courses_page.check_visible_image_upload_view()
    create_courses_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    create_courses_page.check_visible_exercises_title()
    create_courses_page.check_visible_create_exercise_button()
    create_courses_page.check_visible_exercises_empty_view()
    create_courses_page.upload_preview_image('./testdata/files/image.jpeg')
    create_courses_page.check_visible_preview_image()
    create_courses_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_courses_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_courses_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )
