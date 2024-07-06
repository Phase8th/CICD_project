def test_mainpage_search(page) -> None:
    page.goto("https://avtodom.ru")
    page.get_by_placeholder("от 1 594 900 ₽").click()
    page.get_by_placeholder("от 1 594 900 ₽").fill("10000000")
    page.get_by_role("button", name="Показать").click()

