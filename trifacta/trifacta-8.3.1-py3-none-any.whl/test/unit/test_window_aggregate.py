#  Trifacta Inc. Confidential
#
#  Copyright 2020 Trifacta Inc.
#  All Rights Reserved.
#
#  Any use of this material is subject to the Trifacta Inc., Source License located
#  in the file 'SOURCE_LICENSE.txt' which is part of this package.  All rights to
#  this material and any derivative works thereof are reserved by Trifacta Inc.
import unittest

import pandas as pd

from trifacta.transform_functions.function_definitions import WindowIndexer, FrameBound, kth_largest


class TestWindowsAggregate(unittest.TestCase):
    def test_something(self):
        df = pd.DataFrame({
            'col': pd.Series([1.0, 3.0, 5.0, 7.0, 9.0, 5.0]),
        })
        self.assertEqual(df.rolling(WindowIndexer(
            start=(FrameBound.CURRENT_ROW, 1),
            end=(FrameBound.CURRENT_ROW, 1))).agg(kth_largest(k=1)).iloc[:, -1],
                         pd.Series([1.0, 3.0, 5.0, 7.0, 9.0, 5.0]))


if __name__ == '__main__':
    unittest.main()
