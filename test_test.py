from typing import Any
import unittest
from stopTimes import StopTimes


class TestsForFlakyApi(unittest.TestCase):
    def test_flakyAPITestCorrectId(self):
        self.correctId = StopTimes("490009276E")
        # if no error, returns a list
        self.assertTrue(type(self.correctId.getStationData()), dict[str, Any])

    def test_flakyApiTestWrongId(self):
        self.wrongId = StopTimes("1")

        # error case returns string error
        self.assertEqual(self.wrongId.getStationData(), 'error')


if __name__ == '__main__':
    unittest.main()
