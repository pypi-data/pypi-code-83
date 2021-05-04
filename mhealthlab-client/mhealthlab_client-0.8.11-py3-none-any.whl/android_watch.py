import glob
import os
import datetime
import pandas as pd
import numpy as np
from loguru import logger
import arus
from .constants import *
import struct


class AndroidWatch:
    def __init__(self, root_folder, pid):
        self._root = root_folder
        self._pid = pid

    def _parse_session(self):
        folders = glob.glob(os.path.join(
            self._root, "*", "*"), recursive=True)
        folders = list(filter(lambda path: os.path.isdir(
            path) and SIGNALIGNER_FOLDER_NAME not in path, folders))
        folders_as_ts = list(map(AndroidWatch.folder_name_to_date, folders))
        folders_as_ts = sorted(folders_as_ts)
        self._session_st = folders_as_ts[0]
        self._session_et = folders_as_ts[-1] + datetime.timedelta(hours=1)
        return self._session_st, self._session_et

    def _parse_baf(self, file):
        G_VAL = 9.80
        col = ["HEADER_TIME_STAMP", "X_ACCELERATION_METERS_PER_SECOND_SQUARED",
               "Y_ACCELERATION_METERS_PER_SECOND_SQUARED", "Z_ACCELERATION_METERS_PER_SECOND_SQUARED"]
        tz = os.path.basename(file).split('.')[2].split('-')[-1]

        hourdiff = int(tz[1:3])
        minutediff = int(tz[3:])

        if tz[0] == 'M':
            hourdiff = -int(tz[1:3])
            minutediff = -int(tz[3:])

        in_file = open(file, "rb")
        b = in_file.read(20)
        diction = {}
        i = 0
        while len(b) >= 20:
            t = int.from_bytes(b[0:8], byteorder='big')
            x = struct.unpack('>f', b[8:12])[0]
            y = struct.unpack('>f', b[12:16])[0]
            z = struct.unpack('>f', b[16:20])[0]
            diction[i] = {'time': t, 'x': x, 'y': y, 'z': z}
            i = i + 1
            b = in_file.read(20)

        df = pd.DataFrame.from_dict(diction, "index")
        df.columns = col
        df['HEADER_TIME_STAMP'] = pd.to_datetime(df['HEADER_TIME_STAMP'], unit='ms') + \
            datetime.timedelta(hours=hourdiff) + \
            datetime.timedelta(minutes=minutediff)
        df['X_ACCELERATION_METERS_PER_SECOND_SQUARED'] = df['X_ACCELERATION_METERS_PER_SECOND_SQUARED'] / G_VAL
        df['Y_ACCELERATION_METERS_PER_SECOND_SQUARED'] = df['Y_ACCELERATION_METERS_PER_SECOND_SQUARED'] / G_VAL
        df['Z_ACCELERATION_METERS_PER_SECOND_SQUARED'] = df['Z_ACCELERATION_METERS_PER_SECOND_SQUARED'] / G_VAL
        return df

    def _decode_if_necessary(self, filepaths):
        prefixes = set(filepath.split(".sensor")[0] for filepath in filepaths)
        result_filepaths = []
        for prefix in prefixes:
            csv_filepath = prefix + '.' + 'sensor.csv'
            baf_filepath = prefix + '.' + 'sensor.baf'
            result_filepaths.append(csv_filepath)
            if os.path.exists(csv_filepath):
                continue
            elif os.path.exists(baf_filepath):
                logger.info("sensor.csv not found, converting from baf file")
                df = self._parse_baf(baf_filepath)
                df.to_csv(csv_filepath, float_format='%.3f',
                          header=True, index=False)
                logger.info(f"{baf_filepath} decoded to {csv_filepath}.")
        return result_filepaths

    def _filter_by_daterange(self, filepaths, date_range=None):
        logger.info(f"Filter sensor files by date range: {len(filepaths)}")
        dates = np.array([pd.Timestamp(filepath.split(self._pid)[1].split(os.sep)[2]).to_numpy()
                         for filepath in filepaths])
        if date_range is None:
            return filepaths
        elif len(date_range) == 1:
            lb = pd.Timestamp(date_range[0]).to_numpy()
            selected_indices = np.where(dates >= lb)
            return [filepaths[i] for i in selected_indices]
        else:
            if date_range[0] == '':
                rb = pd.Timestamp(date_range[1]).to_numpy()
                selected_indices = np.where(dates <= rb)
                return [filepaths[i] for i in selected_indices]
            else:
                lb = pd.Timestamp(date_range[0]).to_numpy()
                rb = pd.Timestamp(date_range[1]).to_numpy()
                selected_indices = np.where(
                    (dates <= rb) & (dates >= lb))[0].tolist()
                return [filepaths[i] for i in selected_indices]

    def convert_to_actigraph(self, date_range=None, sr=50):
        self._parse_session()
        session_span = arus.plugins.signaligner.shrink_session_span(
            (self._session_st, self._session_et), date_range=date_range)
        logger.info('Session span: {}'.format(session_span))
        assert sr is not None
        filepaths = glob.glob(os.path.join(
            self._root, '*', '*', '*.sensor.*'), recursive=True)
        filepaths = list(
            filter(lambda f: SIGNALIGNER_FOLDER_NAME not in f, filepaths))

        filepaths = self._filter_by_daterange(filepaths, date_range=date_range)
        logger.info(f"Filtered sensor files by date range: {len(filepaths)}")

        filepaths = self._decode_if_necessary(filepaths)

        sensor_type = arus.mh.parse_sensor_type_from_filepath(
            filepaths[0])
        data_id = sensor_type + '-' + 'AccelerometerCalibrated'
        sub_session_markers = arus.plugins.signaligner.auto_split_session_span(
            session_span, 'W-SUN')
        logger.debug(sub_session_markers)
        for i in range(len(sub_session_markers) - 1):
            sub_session_span = sub_session_markers[i:i + 2]
            st_display = sub_session_span[0].strftime('%Y%m%d%H')
            et_display = sub_session_span[1].strftime('%Y%m%d%H')
            logger.info(
                f'Process sub session: {st_display} - {et_display} based on W-SUN')

            # set output file paths
            output_path = os.path.join(
                self._root, SIGNALIGNER_FOLDER_NAME, f'{st_display}_{et_display}_sensors', f'{self._pid}_Android_{data_id}_{st_display}_{et_display}.sensor.csv')
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            output_annotation_path = os.path.join(os.path.dirname(
                output_path.replace('sensors', 'labelsets')), f'{self._pid}_missing_{data_id}_{st_display}_{et_display}.annotation.csv')
            os.makedirs(os.path.dirname(
                output_annotation_path), exist_ok=True)
            arus.plugins.signaligner.signify_sensor_files(
                filepaths, data_id, output_path, output_annotation_path, sub_session_span, sr)

    @staticmethod
    def folder_name_to_date(folder_name):
        hour = os.path.basename(folder_name).split('-')[0]
        date = os.path.basename(os.path.dirname(folder_name))
        date_parts = date.split('-')
        ts = datetime.datetime(int(date_parts[0]), int(date_parts[1]),
                               int(date_parts[2]), int(hour), 0, 0, 0)
        return ts


if __name__ == "__main__":
    watch = AndroidWatch('D:/datasets/sample_watch_data/P1', 'P1')
    watch.convert_to_actigraph(sr=50, date_range=['', '2010-06-11'])
