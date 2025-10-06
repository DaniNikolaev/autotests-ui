from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.empty_view.empty_view_component import EmptyViewComponent
from config import settings
from elements.icon import Icon
from elements.text import Text
from elements.button import Button
from elements.file_input import FileInput
from elements.image import Image


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, "create-course-preview")

        self.image_upload_info_icon = Icon(page, f'{identifier}-image-upload-widget-info-icon', "Icon")
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text', "Title")
        self.image_upload_info_description = Text(page,
                                                  f'{identifier}-image-upload-widget-info-description-text',
                                                  "Description")
        self.image_upload_button = Button(page, f'{identifier}-image-upload-widget-upload-button', "Upload button")

        self.image_upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', "File input")

        self.image_preview = Image(page, f'{identifier}-image-upload-widget-preview-image', "Image")
        self.image_remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button', "Remove button")

    def check_image_form_empty_view_(self):
        self.preview_empty_view.check_visible(
            title="No image selected",
            description="Preview of selected image will be displayed here"
        )

    def check_image_form_fully_view(self):
        self.image_preview.check_visible()

    def check_upload_image_form(self, is_uploaded: bool = False):
        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file')

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')

        self.image_upload_button.check_visible()
        if is_uploaded:
            self.image_remove_button.check_visible()

    def click_image_upload_button(self):
        self.image_upload_button.click()

    def upload_image(self):
        self.image_upload_input.set_input_files(settings.test_data.image_file)

    def click_image_remove_button(self):
        self.image_remove_button.click()
