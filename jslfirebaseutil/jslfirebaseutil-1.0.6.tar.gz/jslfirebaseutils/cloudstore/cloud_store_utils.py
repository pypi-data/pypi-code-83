import logging
import os

from firebase_admin import firestore
from google.cloud import firestore

FORMAT = "%(levelname)s %(asctime)s %(funcName)s() %(lineno)i %(message)s"
formatter = logging.Formatter(FORMAT)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


class JslFirebaseUtil:
	db = None

	def __init__(self, credentials_path):
		self.initialize_firebase_client(credentials_path)

	def initialize_firebase_client(self, credentials_path=None):
		if credentials_path:
			os.environ[
				"GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
			self.db = firestore.Client()
			logger.info("Firebase client is initialized")
		else:
			logger.error(f"Credentials Path can not be empty {credentials_path}")

	def clear_all_collection(self, collection_name):
		deleted_count = 0
		try:
			if collection_name:
				collection_reference = self.db.collection(collection_name)
				docs = collection_reference.stream()
				for doc in docs:
					logger.info(f'Deleting doc {doc.id} => {doc.to_dict()}')
					doc.reference.delete()
					deleted_count += 1
			else:
				logger.error(f"{collection_name}: collection name can not be blank")
		except Exception as e:
			logger.error(f"Exception while clearing all docs inf{collection_name} WIth exception message: {e.args}")
		logger.info(f"Total deleted records: {deleted_count}")

	def delete_document_collection_with_contains(self, collection_name, limit=10, string_contains=None):
		deleted_count = 0
		try:
			if collection_name and string_contains:
				collection_reference = self.db.collection(collection_name)
				docs = collection_reference.limit(limit).stream()
				for doc in docs:
					if string_contains in str(doc.to_dict()):
						logger.info(f'Deleting doc {doc.id} => {doc.to_dict()}')
						doc.reference.delete()
						deleted_count += 1
			else:
				logger.error(f"{collection_name}:{string_contains} can not be blank")
		except Exception as e:
			logger.error(f"Exception while clearing all docs inf{collection_name} WIth exception message: {e.args}")

		logger.info(f"Total deleted records: {deleted_count}")
