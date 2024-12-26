import os
from idlelib.rpc import response_queue

from playwright.sync_api import Playwright, sync_playwright, expect, Page


def test_add_todo(page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")


def test_loc(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()



def test_locator_and(page):
    page.goto("https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()

def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()


def test_checkbox_1(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()


def test_select_multiple(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#skills', value=["playwright", "python"])

def test_drag_and_drop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")


def test_download(page):

    page.goto("https://demoqa.com/upload-download")

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, file_name))

def test_text(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_inner_texts())


def test_first(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page).to_have_url('https://demo.playwright.dev/todomvc/#/')
    expect(page.get_by_placeholder("What needs to be done?")).to_be_empty()
    page.get_by_placeholder("What needs to be done?").fill("1")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("2")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.get_by_test_id("todo-item")).to_have_count(2)
    page.get_by_test_id('todo-item').get_by_role('checkbox').nth(1).click()
    expect(page.get_by_test_id('todo-item').nth(1)).to_have_class('completed')
    page.pause()

def test_listen_network(page: Page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://osinit.ru/')

def test_api(page: Page):
    data = [
              {
                "id": 9743,
                "username": "fsd",
                "firstName": "fff",
                "lastName": "ggg",
                "email": "bbb",
                "password": "tt",
                "phone": "333",
                "userStatus": 0
              }
            ]
    headers = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray', data=data, headers=headers)
    print(response.status)
    print(response.json())