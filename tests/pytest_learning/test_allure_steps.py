import allure


@allure.step("Step #3")
def check_sidesteps():
    with allure.step("Sidestep #3.1"):
        pass
    with allure.step("Sidestep #3.2"):
        pass


@allure.step("Step #4 with title: {title}")
def check_format_step(title: str):
    pass


def test_feature():
    with allure.step("Step #1"):
        pass
    with allure.step("Step #2"):
        pass
    check_sidesteps()
    check_format_step(title="Hello!")
    with allure.step("Step #5"):
        pass
