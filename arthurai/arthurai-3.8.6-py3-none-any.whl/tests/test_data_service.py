import pytest
import pathlib
import os
import math
import pandas as pd
import tempfile
import shutil

from arthurai.core.data_service import DatasetService
from arthurai.core import util

def test_chunk_parquet_image_set_single_file():
    # create test parquet set
    image_dir = pathlib.Path(__file__).parent.absolute()
    image_path = os.path.join(image_dir, "data", "test_image.png")

    # we want to generate 400 MB of image data, to ensure we get 2 chunks
    target_size = 400000000 # 400 MB in bytes
    image_size = os.path.getsize(image_path)
    num_images = math.ceil(target_size / image_size)

    # make test data, all with same image path, avoid having to commit 400MB of data to repo
    image_col_name = 'image'
    extra_col_name = 'extra' # dummy column, ensure we aren't loosing columns
    source_directory = tempfile.mkdtemp()
    image_col_data = [image_path for i in range(num_images)]
    df = pd.DataFrame({image_col_name: image_col_data, extra_col_name: 1})
    df.to_parquet(os.path.join(source_directory, 'test.parquet'))

    output_directory = DatasetService.chunk_parquet_image_set(source_directory, image_col_name)

    # validate no data loss
    files = util.retrieve_parquet_files(output_directory)
    total_chunked_count = 0
    for file in files:
        df = pd.read_parquet(file)
        total_chunked_count += len(df)

        # don't lose columns
        assert extra_col_name in df

        # image chunk can be at most image_size + ~300MB, we check size after adding file
        chunk_size = len(df) * image_size
        assert chunk_size  - 300000000 <= image_size
    assert total_chunked_count == num_images

    # cleanup
    shutil.rmtree(source_directory)
    shutil.rmtree(output_directory)


def test_chunk_parquet_image_set_mult_small_files():
    # create test parquet set
    image_dir = pathlib.Path(__file__).parent.absolute()
    image_path = os.path.join(image_dir, "data", "test_image.png")

    # generate 400 MB of image data
    target_size = 400000000 # 400 MB in bytes
    image_size = os.path.getsize(image_path)
    num_images = math.ceil(target_size / image_size)

    # make test data, all with same image path, avoid having to commit 400MB of data to repo
    image_col_name = 'image'
    extra_col_name = 'extra' # dummy column, ensure we aren't loosing columns
    source_directory = tempfile.mkdtemp()
    image_col_data = [image_path for i in range(num_images)]
    df = pd.DataFrame({image_col_name: image_col_data, extra_col_name: 1})

    # make 10 files, so each file will be ~40MB of image data
    expected_row_count = 0
    for i in range(10):
        sampled_df = df.sample(frac=0.1)
        sampled_df.to_parquet(os.path.join(source_directory, f'test_{i}.parquet'))
        expected_row_count += len(sampled_df)
    
    output_directory = DatasetService.chunk_parquet_image_set(source_directory, image_col_name)

    # validate no data loss
    files = util.retrieve_parquet_files(output_directory)
    total_chunked_count = 0
    for file in files:
        df = pd.read_parquet(file)
        total_chunked_count += len(df)

        # don't lose columns
        assert extra_col_name in df

        # image chunk can be at most image_size + ~300MB, we check size after adding file
        chunk_size = len(df) * image_size
        assert chunk_size  - 300000000 <= image_size
    assert total_chunked_count == expected_row_count

    # cleanup
    shutil.rmtree(source_directory)
    shutil.rmtree(output_directory)


def test_chunk_parquet_image_set_mult_big_files():
    # create test parquet set
    image_dir = pathlib.Path(__file__).parent.absolute()
    image_path = os.path.join(image_dir, "data", "test_image.png")

    # we want to generate 400 MB of image data, to ensure we get 2 chunks
    target_size = 400000000 # 400 MB in bytes
    image_size = os.path.getsize(image_path)
    num_images = math.ceil(target_size / image_size)

    # make test data, all with same image path, avoid having to commit 400MB of data to repo
    image_col_name = 'image'
    extra_col_name = 'extra' # dummy column, ensure we aren't loosing columns
    source_directory = tempfile.mkdtemp()
    image_col_data = [image_path for i in range(num_images)]
    df = pd.DataFrame({image_col_name: image_col_data, extra_col_name: 1})

    # break 400 MB dataset into 360MB and 40MB files
    small_df = df.sample(frac=0.1)
    small_df.to_parquet(os.path.join(source_directory, 'small_test.parquet'))
    df.iloc[0:-len(small_df)].to_parquet(os.path.join(source_directory, 'big_test.parquet'))

    output_directory = DatasetService.chunk_parquet_image_set(source_directory, image_col_name)


    # validate no data loss
    files = util.retrieve_parquet_files(output_directory)
    total_chunked_count = 0
    for file in files:
        df = pd.read_parquet(file)
        total_chunked_count += len(df)

        # don't lose columns
        assert extra_col_name in df

        # image chunk can be at most image_size + ~300MB, we check size after adding file
        chunk_size = len(df) * image_size
        assert chunk_size  - 300000000 <= image_size
    assert total_chunked_count == num_images

    # cleanup
    shutil.rmtree(source_directory)
    shutil.rmtree(output_directory)








