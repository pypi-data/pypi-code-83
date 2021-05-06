# -*- coding: utf-8 -*-

"""
Author     : ZhangYafei
Description: Geo数据下载
"""
import asyncio
import os
from collections.abc import Iterable
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import async_timeout
from lxml import etree
from pandas import DataFrame
from requests import Session
from tqdm import tqdm
from zyf.timer import Timeit


class GeoDataType:
    SeriesMatrix = 1


class AccessionDownloader:
    def __init__(self, accession_save_filepath: str = None, history_dir: str = None):
        self.session = Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76'}
        self.session.headers = headers
        self.history_dir = history_dir if history_dir else 'history'
        self.success_filepath = f'{self.history_dir}/success_accession_page.txt'
        self.accession_list = []
        self.accession_save_filepath = accession_save_filepath if accession_save_filepath else 'accession_list.txt'

        if not os.path.exists(self.history_dir):
            os.mkdir(self.history_dir)

    @Timeit(prefix='成功读取并完成过滤')
    def filter_request(self, display: int, page_nums: int):
        filter_string = f'每页 {display} 个, 共 {page_nums} 页'

        if os.path.exists(self.success_filepath):
            self.success_f = open(self.success_filepath, mode='a+')
            self.success_f.seek(0)
            success_pages = {int(line.strip()) for line in self.success_f}
            page_list = {page for page in range(1, page_nums + 1) if page not in success_pages}
            filter_string += f', 成功下载：{len(success_pages)}页'
        else:
            self.success_f = open(self.success_filepath, mode='a')
            page_list = set(range(1, page_nums + 1))

        if os.path.exists(self.accession_save_filepath):
            self.accession_save_f = open(self.accession_save_filepath, mode='a+')
            self.accession_save_f.seek(0)
            success_count = len({row.strip() for row in self.accession_save_f})
            filter_string += f' -> {success_count} 个'
        else:
            self.accession_save_f = open(self.accession_save_filepath, mode='w')

        if page_list:
            filter_string += f', 本次需下载 {len(page_list)} 页'
        else:
            filter_string += f', 全部下载成功'
        print(filter_string)
        return page_list

    def spider(self, display, page):
        url = f'https://www.ncbi.nlm.nih.gov/geo/browse/?view=series&zsort=date&display={display}&page={page}'
        print(f'make request to {url}')
        return page, self.session.get(url)

    def parse(self, future):
        try:
            page, response = future.result()
            html = etree.HTML(response.content)
            accessions = html.xpath('//table[@id="geo_data"]/tbody/tr/td[1]/a/text()')
            for accession in accessions:
                self.accession_save_f.write(f'{accession}\n')
            self.success_f.write(f'{page}\n')
            self.accession_save_f.flush()
            self.success_f.flush()
            print(page, len(accessions))
        except Exception as e:
            print(e)

    @Timeit(prefix='Accessions 下载完毕')
    def start(self, workers: int = None, page_nums: int = 299, display: int = 500):
        workers = workers if workers else os.cpu_count()
        while True:
            page_list = self.filter_request(display=display, page_nums=page_nums)
            if not page_list:
                break
            with ThreadPoolExecutor(max_workers=workers) as pool:
                for page in page_list:
                    task = pool.submit(self.spider, display, page)
                    task.add_done_callback(self.parse)


class GeoDownloader:
    def __init__(self, accession_list: Iterable = None, download_dir: str = None, history_dir: str = None,
                 success_filepath: str = None, error_filepath: str = None):
        self.session = Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76'}
        self.session.headers = self.headers
        self.download_dir = download_dir if download_dir else 'download'
        self.history_dir = history_dir if history_dir else 'history'

        self.success_filepath = success_filepath if success_filepath else f'{self.history_dir}/download_success.txt'
        self.error_filepath = error_filepath if error_filepath else f'{self.history_dir}/download_error.txt'

        self.success_f = None
        self.error_f = None
        self.error_list = []
        self.accession_list = set(accession_list) if accession_list else None
        self.func_download_map = {}
        self.func_init_map = {}
        self.init_func_map()

        if not os.path.exists(self.history_dir):
            os.mkdir(self.history_dir)
        if not os.path.exists(self.download_dir):
            os.mkdir(self.download_dir)

    def init_func_map(self):
        self.func_download_map[GeoDataType.SeriesMatrix] = self.download_series_matrix
        self.func_init_map[GeoDataType.SeriesMatrix] = self.download_series_matrix_init

    def get_download_func(self, date_type: str):
        return self.func_download_map.get(date_type, None)

    @Timeit(prefix='成功读取并完成过滤')
    def filter_request_list(self, request_list: set, desc: str = 'Accession'):
        """ 读取并过滤 request 列表 """
        print(f'正在读取 {desc} 列表')
        total_request_count = len(request_list)
        filter_string = f'\t--> 共有 {desc} 数量：{total_request_count}'
        if os.path.exists(self.success_filepath):
            self.success_f = open(self.success_filepath, mode='a+')
            self.success_f.seek(0)
            downloaded_request_list = {line.strip() for line in self.success_f}
            request_list = request_list - downloaded_request_list
            filter_string += f', 成功下载：{len(downloaded_request_list)}'
        else:
            self.success_f = open(self.success_filepath, mode='a+')

        if os.path.exists(self.error_filepath):
            self.error_f = open(self.error_filepath, mode='a+')
            self.error_f.seek(0)
            error_request_list = {line.strip() for line in self.error_f}
            request_list = request_list - error_request_list
            filter_string += f', 下载失败(404)：{len(error_request_list)},  还剩：{len(request_list)}'
        else:
            self.error_f = open(self.error_filepath, mode='a+')
        print(filter_string)

        return request_list

    def download_series_matrix_url(self, accession_list: Iterable = None, series_matrix_url_filepath: str = None,
                                   async_on: bool = False):
        if accession_list and type(accession_list) != set:
            accession_list = set(accession_list)
        elif self.accession_list:
            accession_list = self.accession_list
        else:
            raise Exception("accession_list can't is None")
        self.series_matrix_url_filepath = series_matrix_url_filepath if series_matrix_url_filepath else f'{self.history_dir}/series_matrix_urls.txt'
        self.series_matrix_url_f = open(self.series_matrix_url_filepath, mode='a')
        while True:
            print('-*-' * 22)
            accession_list = self.filter_request_list(request_list=accession_list, desc='Accession')
            print('-*-' * 22)
            if len(accession_list) > 0:
                if async_on:
                    asyncio.run(self.download_series_matrix_url_init_async())
                else:
                    with ThreadPoolExecutor(max_workers=10) as pool:
                        futures_list = (pool.submit(self.get_series_matrix_url, accession) for accession in
                                        accession_list)
                        for future in futures.as_completed(futures_list):
                            if isinstance(future.result(), Exception):
                                print(future.result())
            else:
                break
        self.success_f.close()
        self.error_f.close()
        self.series_matrix_url_f.close()

    def get_series_matrix_url(self, accession):
        """ 请求Series_matrix url """
        url = f'https://ftp.ncbi.nlm.nih.gov/geo/series/{accession[:-3]}nnn/{accession}/matrix/'
        print(url)
        response = self.session.get(url)
        if response.status_code == 200:
            html = etree.HTML(response.text)
            href_list = html.xpath('//pre/a[position() > 1]/@href')
            for href in href_list:
                series_matrix_url = f'{url}{href}'
                self.series_matrix_url_f.write(f'{series_matrix_url}\n')
            self.success_f.write(f'{accession}\n')
            self.series_matrix_url_f.flush()
            self.success_f.flush()
        elif response.status_code == 404:
            self.error_f.write(f'{accession}\n')
            self.error_f.flush()

        print(accession, response.status_code)

    async def download_series_matrix_url_init_async(self, accession_list):
        """ 异步下载 series_matrix_url 初始化"""
        conn = aiohttp.TCPConnector(ssl=False, limit=100, use_dns_cache=True)
        semaphore = asyncio.Semaphore(50)
        async with aiohttp.ClientSession(connector=conn, headers=self.headers) as session:
            await asyncio.gather(
                *[asyncio.create_task(self.get_series_matrix_url_async(session, accession, semaphore)) for accession in
                  accession_list])

    async def get_series_matrix_url_async(self, session, accession, semaphore):
        """ 异步下载 series_matrix url """
        url = f'https://ftp.ncbi.nlm.nih.gov/geo/series/{accession[:-3]}nnn/{accession}/matrix/'
        print(url)
        try:
            async with semaphore:
                with async_timeout.timeout(60):
                    async with session.get(url=url) as response:
                        if response.status == 200:
                            text = await response.text()
                            html = etree.HTML(text)
                            href_list = html.xpath('//pre/a[position() > 1]/@href')
                            for href in href_list:
                                series_matrix_url = f'{url}{href}'
                                self.series_matrix_url_f.write(f'{series_matrix_url}\n')
                            self.success_f.write(f'{accession}\n')
                            self.series_matrix_url_f.flush()
                            self.success_f.flush()
                        elif response.status == 404:
                            self.error_f.write(f'{accession}\n')
                            self.error_f.flush()
                        print(accession, response.status)
        except Exception as e:
            print(f'{accession} 请求失败', e)

    def download_series_matrix_init(self, series_matrix_url_filepath: str = None):
        """ 下载series_matrix 初始化 """
        if not series_matrix_url_filepath:
            self.download_series_matrix_url()
        self.series_matrix_url_filepath = series_matrix_url_filepath if series_matrix_url_filepath else f'{self.history_dir}/series_matrix_urls.txt'
        with open(self.series_matrix_url_filepath, mode='r') as f:
            url_list = {line.strip() for line in f}
        return self.filter_request_list(request_list=url_list, desc='url')

    def download_series_matrix(self, url):
        """ 下载series_matrix """
        response = self.session.get(url=url, stream=True)
        if response.status_code != 200:
            print(f'\n{url}\t请求失败\t{response.status_code}')
            if response.status_code == 404:
                self.error_f.write(f'{url}\n')
                self.error_f.flush()
            return

        self.save_to_file(response=response, url=url)

    def save_to_file(self, response, url):
        """ 保存到文件 """
        filename = url.rsplit('/', maxsplit=1)[-1]
        content_size = int(response.headers['content-length'])

        content_size_string = f'{content_size / (1024 * 1024):.2f} MB' if content_size >= (
                1024 * 1024) else f'{content_size / 1024:.2f} KB'

        task_progressbar = tqdm(iterable=response.iter_content(1024), total=int(content_size / 1024), ncols=100,
                                unit='KB', desc=f'正在下载 -> {filename} -> {content_size_string}')
        with open(f'{self.download_dir}/{filename}', 'wb+') as f:
            for chunk in task_progressbar:
                f.write(chunk)

        self.success_f.write(f'{url}\n')
        self.success_f.flush()

    @Timeit('下载结束')
    def run(self, data_type, workers: int = None, *args, **kwargs):
        if not data_type:
            raise Exception("data_type can't is None")
        func_execute = self.get_download_func(data_type)
        if not func_execute:
            raise Exception('data_type error, must be ncbi.geo.GeoDataType elements')

        if data_type in self.func_init_map:
            url_list = self.func_init_map[data_type](*args, **kwargs)
        elif self.accession_list:
            url_list = self.accession_list
        else:
            raise Exception('init func or accession_list must one is not None!')

        if len(url_list) > 0:
            workers = workers if workers else os.cpu_count()
            with ThreadPoolExecutor(max_workers=workers) as pool:
                futures_list = (pool.submit(func_execute, url) for url in url_list)
                for future in futures.as_completed(futures_list):
                    if future.exception():
                        print(future.exception())

    def __del__(self):
        self.success_f.close()
        self.error_f.close()


class GeoParser:
    def __init__(self, finished_dir: str = None, file_list: Iterable = None, history_dir: str = None,
                 success_filepath: str = None, error_filepath: str = None):
        self.file_list = set(file_list) if file_list else None
        self.parse_dir = finished_dir if finished_dir else 'parse'
        self.history_dir = history_dir if history_dir else 'history'
        self.success_filepath = success_filepath if success_filepath else f'{self.history_dir}/parse_success.txt'
        self.error_filepath = error_filepath if error_filepath else f'{self.history_dir}/parse_error.txt'
        self.parse_func_map = {}
        self.init_func_map = {}
        self.data = []

        if not os.path.exists(self.history_dir):
            os.mkdir(self.history_dir)
        if not os.path.exists(self.parse_dir):
            os.mkdir(self.parse_dir)

        self.func_map_init()

    @Timeit(prefix='成功读取并完成过滤')
    def filter_list(self, all_list: set, desc: str = '文件'):
        """ 读取并过滤 列表 """
        print(f'正在读取 {desc} 列表')
        total_count = len(all_list)
        filter_string = f'\t--> 共有 {desc} 数量：{total_count}'
        if os.path.exists(self.success_filepath):
            self.success_f = open(self.success_filepath, mode='a+')
            self.success_f.seek(0)
            success_list = {line.strip() for line in self.success_f}
            all_list = all_list - success_list
            filter_string += f', 成功解析：{len(success_list)}'
        else:
            self.success_f = open(self.success_filepath, mode='a+')

        if os.path.exists(self.error_filepath):
            self.error_f = open(self.error_filepath, mode='a+')
            self.error_f.seek(0)
            error_list = {line.strip() for line in self.error_f}
            all_list = all_list - error_list
            filter_string += f', 解析失败：{len(error_list)},  还剩：{len(all_list)}'
        else:
            self.error_f = open(self.error_filepath, mode='a+')
        print(filter_string)
        return all_list

    def func_map_init(self):
        self.parse_func_map[GeoDataType.SeriesMatrix] = self.parse_series_matrix
        self.init_func_map[GeoDataType.SeriesMatrix] = self.series_matrix_init

    def get_parse_func(self, data_type):
        return self.parse_func_map[data_type]

    def series_matrix_init(self, file_list: Iterable = None):
        if file_list and type(file_list) != set:
            file_list = set(file_list)
        elif self.file_list:
            file_list = self.file_list
        else:
            raise Exception("file_list can't is None")

        self.series_matrix_table_dir = f'{self.parse_dir}/series_matrix_table'
        if not os.path.exists(self.series_matrix_table_dir):
            os.mkdir(self.series_matrix_table_dir)

        print('-*-' * 22)
        filter_file_list = self.filter_list(all_list=file_list, desc='文件')
        print('-*-' * 22)
        return filter_file_list

    def parse_series_matrix(self, filepath: str):
        filename = os.path.split(filepath)[-1]
        accession_platform = filename.strip('_series_matrix.txt')
        platform = None
        if '-' in accession_platform and len(accession_platform.split('-')) == 2:
            accession, platform = accession_platform.split('-')
        else:
            accession = accession_platform
        try:
            item = {}
            item['accession'] = accession
            item['platform'] = platform
            item['series_matrix_filepath'] = filepath
            with open(filepath, mode='r', encoding='utf-8') as f:
                series_matrix = ''
                for line in f:
                    if line.startswith('!series_matrix_table_begin'):
                        series_matrix = f.read().replace('!series_matrix_table_end', '').strip()
                        break
                    elif line.strip() and len(line.strip().split('\t', maxsplit=1)) == 2:
                        name, content = line.strip().split('\t', maxsplit=1)
                        name = name.strip('!').replace('"', '').strip()
                        if not name:
                            continue
                        content = content.replace('"', '')
                        if name in item:
                            item[name] += f' {content}'
                        else:
                            item[name] = content
                self.data.append(item)

            series_matrix_table_filename = f'{self.series_matrix_table_dir}/{filename}'
            if not os.path.exists(series_matrix_table_filename):
                with open(f'{self.series_matrix_table_dir}/{filename}', mode='w', encoding='utf-8') as f:
                    f.write(series_matrix)

            print(f'{filename} 解析完成')
        except Exception as e:
            print(filename, e)

    def to_file(self):
        df = DataFrame(data=self.data)
        if os.path.exists(self.save_filename):
            df.to_csv(self.save_filename, index=False, encoding='utf_8_sig', mode='a')
        else:
            df.to_csv(self.save_filename, index=False, encoding='utf_8_sig')
        for filepath in df['series_matrix_filepath']:
            self.success_f.write(f'{filepath}\n')
        print(f'数据已保存至 {self.parse_dir} 文件夹')

    @Timeit("解析结束")
    def run(self, data_type, workers: int = None, save_filename: str = None, *args, **kwargs):
        if not data_type:
            raise Exception("data_type can't is None")

        self.save_filename = save_filename if save_filename else f'{self.parse_dir}/series_matrix_info.csv'

        func_execute = self.get_parse_func(data_type)
        if not func_execute:
            raise Exception('data_type error, must be ncbi.geo.GeoDataType elements')
        if data_type in self.init_func_map:
            file_list = self.init_func_map[data_type](*args, **kwargs)
        elif self.file_list:
            file_list = self.file_list
        else:
            raise Exception('init func or file_list must one is not None!')

        if len(file_list) > 0:
            print('开始解析')
            workers = workers if workers else os.cpu_count()
            with ThreadPoolExecutor(max_workers=workers) as pool:
                futures_list = (pool.submit(func_execute, file) for file in file_list)
                for future in futures.as_completed(futures_list):
                    if future.exception():
                        print(future.exception())

            self.to_file()
