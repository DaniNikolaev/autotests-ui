from enum import Enum


class AllureStory(str, Enum):
    DASHBOARD = "Dashboard"
    AUTHORIZATION = "Authorization"
    REGISTRATION = "Registration"
    CREATE_COURSE = "Create_course"
    COURSES_LIST = "Courses_list"
