"""
	LABASCRAPER PACKAGE
"""

from .models.author 		import Author 
from .models.comment 		import Comment
from .models.cryptocurrency import Cryptocurrency

from .scraper.link_grabber 	import LinkGrabber
from .scraper.page_scraper	import PageScraper

__version__ = '2.0.0'
__all__ = ['Author', 'Comment', 'Cryptocurrency', 'LinkGrabber', 'PageScraper']
