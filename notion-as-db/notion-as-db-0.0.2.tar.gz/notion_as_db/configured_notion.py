import pandas as pd
from config2.config import config
from notion.client import NotionClient


class Notion(NotionClient):
    def __init__(self):
        super().__init__(config.notion.v2token)
        tmp_dict = self.get_block_name_url_dict()
        self.__block_dict__ = dict((x, self.get_block(tmp_dict[x])) for x in tmp_dict.keys())

    def get_block_name_url_dict(self) -> dict:
        tmp_block = self.get_block(config.notion.block_info_url)
        tmp_list = tmp_block.collection.get_rows()
        return dict((row.block_name, row.link_url) for row in tmp_list)

    def get_collections_as_dict(self, input_block):
        tmp_dict = dict()
        if "collection" in dir(input_block):
            return input_block.collection
        if "children" not in dir(input_block):
            return input_block
        else:
            for x in input_block.children:
                if "title" in dir(x):
                    tmp_dict[x.title] = self.get_collections_as_dict(x)
        if not tmp_dict:
            return input_block
        else:
            return tmp_dict

    def get_df_from_collection_block(self, input_collection):
        col_list = list(x["name"] for x in input_collection.get_schema_properties())
        tmp_result_list = list()
        tmp_list = input_collection.get_rows()
        for x in tmp_list:
            tmp_dict = dict((key, x.get_property(key)) for key in col_list)
            tmp_result_list.append(tmp_dict)
        return pd.DataFrame(tmp_result_list)

    @property
    def block_dict(self):
        return self.__block_dict__
