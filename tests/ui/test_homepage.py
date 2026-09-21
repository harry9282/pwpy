from playwright.sync_api import expect


def test_title_of_homepage(homepage):
    expect(homepage.page).to_have_title(homepage.get_page_title())


def test_validate_user_lands_on_udemy(homepage):
    udemy_page=homepage.go_to_udemy_dealpage()
    expect(udemy_page.page).to_have_url(udemy_page.get_current_url())
    
   



