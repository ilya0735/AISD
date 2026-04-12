import pytest
import numpy as np
from pathlib import Path
from radix_sort import RadixSort


class Test:
    data_file = list(np.load(Path(__file__).parent / "data.npy", allow_pickle=True))

    @pytest.fixture()
    def data(self):
        return self.data_file

    @pytest.fixture()
    def sorted_data(self):
        return [sorted(dataset) for dataset in self.data_file]

    def test_sort(self, data, sorted_data):
        radix_sort = RadixSort()

        for dataset in data:
            radix_sort.radix_sort(dataset)

        assert data == sorted_data
