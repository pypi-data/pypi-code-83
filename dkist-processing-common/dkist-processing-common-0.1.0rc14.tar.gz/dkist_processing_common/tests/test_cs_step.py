import random
from collections import defaultdict
from typing import Dict
from typing import List
from typing import Tuple

import numpy as np
import pytest
from dkist_data_simulator.dataset import key_function
from dkist_data_simulator.spec122 import Spec122Dataset

from dkist_processing_common.parsers.cs_step import CSStep
from dkist_processing_common.parsers.l0_fits_access import L0FitsAccess


class CalibrationSequenceDataset(Spec122Dataset):
    def __init__(
        self,
        array_shape: Tuple[int, ...],
        time_delta: float,
        instrument="visp",
    ):
        self.num_frames_per_CS_step = 5

        # Make up a Calibration sequence. Mostly random except for two clears and two darks at start and end, which
        # we want to test
        self.pol_status = [
            "clear",
            "clear",
            "test polarizer",
            "test polarizer",
            "test polarizer",
            "clear",
            "clear",
        ]
        self.pol_theta = [0.0, 0.0, 60.0, 60.0, 120.0, 0.0, 0.0]
        self.ret_status = ["clear", "clear", "clear", "test retarder", "clear", "clear", "clear"]
        self.ret_theta = [0.0, 0.0, 0.0, 45.0, 0.0, 0.0, 0.0]
        self.dark_status = [
            "DarkShutter",
            "FieldStop",
            "FieldStop",
            "FieldStop",
            "FieldStop",
            "FieldStop",
            "DarkShutter",
        ]

        self.num_steps = len(self.pol_theta)
        dataset_shape = (self.num_steps * self.num_frames_per_CS_step,) + array_shape[1:]
        super().__init__(dataset_shape, array_shape, time_delta, instrument=instrument)
        self.add_constant_key("DKIST004", "PolCal")

    @property
    def cs_step(self) -> int:
        return self.index // self.num_frames_per_CS_step

    @key_function("PAC__004")
    def polarizer_status(self, key: str) -> str:
        return self.pol_status[self.cs_step]

    @key_function("PAC__005")
    def polarizer_angle(self, key: str) -> float:
        return self.pol_theta[self.cs_step]

    @key_function("PAC__006")
    def retarter_status(self, key: str) -> str:
        return self.ret_status[self.cs_step]

    @key_function("PAC__007")
    def retarder_angle(self, key: str) -> float:
        return self.ret_theta[self.cs_step]

    @key_function("PAC__008")
    def gos_level3_status(self, key: str) -> str:
        return self.dark_status[self.cs_step]


class NonPolCalDataset(Spec122Dataset):
    def __init__(self):
        super().__init__(
            dataset_shape=(4, 2, 2), array_shape=(1, 2, 2), time_delta=1, instrument="visp"
        )  # Instrument doesn't matter
        self.add_constant_key("DKIST004", "Dark")  # Anything that's not PolCal


@pytest.fixture(scope="session")
def grouped_cal_sequence_headers() -> Dict[int, List[L0FitsAccess]]:
    ds = CalibrationSequenceDataset(array_shape=(1, 2, 2), time_delta=2.0)
    header_list = [d.header() for d in ds]
    expected_cs_dict = defaultdict(list)
    for i in range(ds.num_steps):
        for j in range(ds.num_frames_per_CS_step):
            expected_cs_dict[i].append(L0FitsAccess.from_header(header_list.pop(0)))

    return expected_cs_dict


@pytest.fixture(scope="session")
def non_polcal_headers() -> List[L0FitsAccess]:
    ds = NonPolCalDataset()
    obj_list = [L0FitsAccess.from_header(d.header()) for d in ds]
    return obj_list


def test_equal_correct(grouped_cal_sequence_headers):
    """
    Given: A set of PolCal headers
    When: Converting them to CSStep objects and comparing them
    Then: All headers belonging to the same step produce CSStep objects that are equal
    """
    for cs_header_list in grouped_cal_sequence_headers.values():
        for i in range(len(cs_header_list)):
            assert CSStep(cs_header_list[0]) == CSStep(cs_header_list[i])


@pytest.mark.parametrize("stepnum", [pytest.param(i, id=f"step {i}") for i in range(7)])
def test_not_equal_correct(grouped_cal_sequence_headers, stepnum):
    """
    Given: A set of PolCal headers
    When: Converting them to CSStep objects and comparing them
    Then: All objects from a single step are not equal to all objects from other steps
    """
    for i in range(7):
        if i != stepnum:
            assert CSStep(grouped_cal_sequence_headers[stepnum][0]) != CSStep(
                grouped_cal_sequence_headers[i][0]
            )


def test_not_equal_non_CS_Step_type(grouped_cal_sequence_headers):
    """
    Given: A PolCal header and resulting CSStep object
    When: Testing equality with a non CSStep object
    Then: An error is raised
    """
    cs_step = CSStep(grouped_cal_sequence_headers[0][0])
    with pytest.raises(TypeError):
        _ = cs_step == 1


def test_order_correct(grouped_cal_sequence_headers):
    """
    Given: A set of PolCal headers
    When: Converting them to CSStep objects and ordering them
    Then: The step objects are correctly ordered by observe time
    """
    cs_step_list = [CSStep(header) for header in sum(grouped_cal_sequence_headers.values(), [])]
    random.shuffle(cs_step_list)  # Just to mix it up a bit
    time_list = [c.obs_time for c in cs_step_list]
    cs_sort_idx = np.argsort(cs_step_list)
    time_sort_idx = np.argsort(time_list)
    assert np.array_equal(cs_sort_idx, time_sort_idx)
