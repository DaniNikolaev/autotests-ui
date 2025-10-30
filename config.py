from enum import Enum
from typing_extensions import Self

from pydantic import FilePath, HttpUrl, DirectoryPath, BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    CHROMIUM = "chromium",
    FIREFOX = "firefox",
    WEBKIT = "webkit"


class TestUser(BaseModel):
    email: str
    username: str
    password: str


class TestData(BaseModel):
    image_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    allure_results_dir: DirectoryPath | None = None
    videos_dir: DirectoryPath | None = None
    tracing_dir: DirectoryPath | None = None
    browser_state_file: FilePath | None = None

    @classmethod
    def initialize(cls) -> Self:
        allure_results_dir = DirectoryPath("./allure-results")
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        browser_state_file = FilePath("browse-state.json")

        allure_results_dir.mkdir(exist_ok=True)
        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
                        allure_results_dir=allure_results_dir,
                        videos_dir=videos_dir,
                        tracing_dir=tracing_dir,
                        browser_state_file=browser_state_file
                        )

    def get_base_url(self):
        return f'{self.app_url}/'


settings = Settings().initialize()
