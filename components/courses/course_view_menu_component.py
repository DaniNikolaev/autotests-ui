import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', "Menu button")
        self.menu_edit_button = Button(page, 'course-view-edit-menu-item', "Edit button")
        self.menu_delete_button = Button(page, 'course-view-delete-menu-item', "Delete button")

    def check_menu(self, index: int):
        self.menu_button.check_visible(nth=index)

    def click_menu(self, index: int = 0):
        self.menu_button.click(nth=index)

    def check_edit(self, index: int = 0):
        self.click_menu(index)

        self.menu_edit_button.check_visible()
        self.menu_edit_button.check_have_text("Edit")

    @allure.step("Click menu button and click edit button")
    def click_edit(self, index: int = 0):
        self.check_edit(index)
        self.menu_edit_button.click(nth=index)

    def check_delete(self, index: int = 0):
        self.click_menu(index)

        self.menu_delete_button.check_visible()
        self.menu_delete_button.check_have_text("Delete")

    @allure.step("Click menu button and click delete button")
    def click_delete(self, index: int = 0):
        self.check_delete(index)
        self.menu_delete_button.click(nth=index)
