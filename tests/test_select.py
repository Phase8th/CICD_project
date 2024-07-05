from playwright.sync_api import expect


def test_dropdown_selector(page) -> None:
    page.goto("https://avtodom.ru/actions/?city=msk")
    page.get_by_role("button", name="Все дилеры").click()
    page.get_by_role("button", name="BMW Зорге").click()
    expect(page.locator("[id=\"__nuxt\"]")).to_contain_text("BMW Зорге")