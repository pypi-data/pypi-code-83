import asyncio
import logging
from typing import List

from bs4 import BeautifulSoup

from udemy_enroller.http import get
from udemy_enroller.scrapers.base_scraper import BaseScraper

logger = logging.getLogger("udemy_enroller")


class IDownloadCouponScraper(BaseScraper):
    """
    Contains any logic related to scraping of data from idownloadcoupon.com
    """

    DOMAIN = "https://www.idownloadcoupon.com"

    def __init__(self, enabled, max_pages=None):
        super().__init__()
        self.scraper_name = "idownloadcoupon"
        if not enabled:
            self.set_state_disabled()
        self.last_page = None
        self.max_pages = max_pages

    @BaseScraper.time_run
    async def run(self) -> List:
        """
        Runs the steps to scrape links from idownloadcoupon.com

        :return: list of udemy coupon links
        """
        links = await self.get_links()
        self.max_pages_reached()
        return links

    async def get_links(self):
        """
        Scrape udemy links from idownloadcoupon.com

        :return: List of udemy course urls
        """
        self.current_page += 1
        course_links = await self.get_course_links(
            f"{self.DOMAIN}/product-category/udemy/page/{self.current_page}/"
        )

        logger.info(
            f"Page: {self.current_page} of {self.last_page} scraped from idownloadcoupon.com"
        )
        udemy_links = await self.gather_udemy_course_links(course_links)

        for counter, course in enumerate(udemy_links):
            logger.debug(f"Received Link {counter + 1} : {course}")

        return udemy_links

    async def get_course_links(self, url: str) -> List:
        """
        Gets the url of pages which contain the udemy link we want to get

        :param str url: The url to scrape data from
        :return: list of pages on idownloadcoupon.com that contain Udemy coupons
        """
        text = await get(url)
        if text is not None:
            soup = BeautifulSoup(text.decode("utf-8"), "html.parser")

            course_links = [i.find("a")["href"] for i in soup.find("ul", class_="products columns-3").find_all("li")]

            self.last_page = (
                soup.find("ul", class_="page-numbers").find_all("li")[-2].text
            )

            return course_links

    @staticmethod
    async def get_udemy_course_link(url: str) -> str:
        """
        Gets the udemy course link

        :param str url: The url to scrape data from
        :return: Coupon link of the udemy course
        """

        text = await get(url)
        if text is not None:
            soup = BeautifulSoup(text.decode("utf-8"), "html.parser")
            udemy_link = (
                soup.find("span", class_="rh_button_wrapper").find("a").get("href")
            )
            return udemy_link

    async def gather_udemy_course_links(self, courses: List[str]):
        """
        Async fetching of the udemy course links from idownloadcoupon.com

        :param list courses: A list of idownloadcoupon.com course links we want to fetch the udemy links for
        :return: list of udemy links
        """
        return [
            link
            for link in await asyncio.gather(*map(self.get_udemy_course_link, courses))
            if link is not None
        ]
