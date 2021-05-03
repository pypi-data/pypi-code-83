import pickle
from pathlib import Path

from PIL import Image
from selenium import webdriver
from time import sleep


class Screenshotter(object):
    def __init__(
        self,
        base_url,
        cookies_file_path,
    ):
        self.cookies_file_path = cookies_file_path
        self.base_url = base_url
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--user-data-dir=chrome-data")
        self.driver = webdriver.Chrome(options=chrome_options)

        # if Path(self.cookies_file_path).exists():
        #     cookies = pickle.load(open(self.cookies_file_path, "rb"))

        #     self.driver.get(self.base_url)

        #     print(f"Loading cookies (current url is {self.driver.current_url})")

        #     from selenium.common import exceptions

        #     for cookie in cookies:
        #         try:
        #             self.driver.add_cookie(cookie)
        #             print("loaded cookie.")
        #         except exceptions.InvalidCookieDomainException as e:
        #             print(f"not loading cookie {str(e)}")

        #     print("Finished cookie load.")
        #     self.driver.refresh()
        # else:
        #     print("No cookies file present - no cookies loaded.")

    def save_cookies(self):
        return
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open(self.cookies_file_path, "wb"))

    def close_all(self):
        # close all open tabs
        if len(self.driver.window_handles) < 1:
            return
        for window_handle in self.driver.window_handles[:]:
            self.driver.switch_to.window(window_handle)
            self.driver.close()

    def do_shot(self, filename):
        d = Path("screenshots")
        d.mkdir(exist_ok=True)
        self.driver.save_screenshot(filename)

    def quit(self):
        self.save_cookies()
        # sleep(5)
        # self.close_all()
        self.driver.quit()


def crop(in_name, out_name, top, bottom, left, right):
    img = Image.open(in_name)
    width, height = img.size

    # crop
    # 10 pixels from the left
    # 20 pixels from the top
    # 30 pixels from the right
    # 40 pixels from the bottom

    cropped = img.crop((left, top, width - right, height - bottom))
    cropped.save(out_name)


# if __name__ == '__main__':
#     selenium_object = SeleniumDriver()
#     driver = selenium_object.driver

#     if is_logged_in(driver):
#         print("Already logged in")
#     else:
#         print("Not logged in. Please log in.")

#     sleep(120)

#     selenium_object.quit()
