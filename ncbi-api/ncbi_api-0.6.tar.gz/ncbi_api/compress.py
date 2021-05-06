# -*- coding: utf-8 -*-

"""
Author     : ZhangYafei
Description: 
"""
import os
import gzip
from zyf.timer import Timeit


class Gzip:
    def __init__(self, history_dir: str = None, success_filepath: str = None, error_filepath: str = None):
        self.history_dir = history_dir if history_dir else 'history'
        self.success_filepath = success_filepath if success_filepath else f'{self.history_dir}/unzip_success.txt'
        self.error_filepath = error_filepath if error_filepath else f'{self.history_dir}/unzip_error.txt'
        if not os.path.exists(self.history_dir):
            os.mkdir(self.history_dir)

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
            filter_string += f', 成功解析：{len(success_list)}, 还剩：{len(all_list)}'
        else:
            self.success_f = open(self.success_filepath, mode='a+')

        self.error_f = open(self.error_filepath, mode='w')

        print(filter_string)
        return all_list

    def batch_file_unzip(self, file_list, unzip_dir: str = 'unzip'):
        print('-*-' * 22)
        file_list = self.filter_list(set(file_list))
        print('-*-' * 22)

        if not file_list:
            print('所有文件已全部解压完成！')
            return

        if not os.path.exists(unzip_dir):
            os.mkdir(unzip_dir)

        success_count = error_count = 0
        print('开始解压')
        for filepath in file_list:
            try:
                gzip_filename = os.path.split(filepath)[-1]
                filename = os.path.splitext(gzip_filename)[0]
                self.unzip(zip_file=filepath, save_file=f'{unzip_dir}/{filename}')
                self.success_f.write(f'{filepath}\n')
                print(f'{filepath} 解压完成')
                success_count += 1
            except Exception as e:
                self.error_f.write(f'{filepath}\t{e}\n')
                print(f'{filepath} 解压失败', e)
                error_count += 1
        print(f'本次共解压文件: {success_count + error_count}  解压成功: {success_count}  解压失败: {error_count}')

    def unzip(self, zip_file: str, save_file: str):
        with gzip.open(zip_file, mode='rb') as gz_f:
            content = gz_f.read()
            with open(save_file, mode='wb') as f:
                f.write(content)
