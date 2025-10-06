import allure

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("FILE_INPUT")


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "File Input"

    def set_input_files(self, path: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth=nth, **kwargs)
        step = f'Set file "{path}" to the {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            locator.set_input_files(path)
