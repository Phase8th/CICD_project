def test_dropdown_selector(page) -> None:
    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto("https://avtodom.ru")
    page.get_by_role("banner").get_by_role("link", name="Новости").click()
