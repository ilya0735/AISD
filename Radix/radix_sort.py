class RadixSort:
    def __init__(self):
        self._step_counting = False
        self._step_counter = 0


    @staticmethod
    def _counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(len(arr)):
            arr[i] = output[i]

    def _counting_sort_with_step(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
            self._step_counter += 1

        for i in range(1, 10):
            count[i] += count[i - 1]
            self._step_counter += 1

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
            self._step_counter += 1

        for i in range(len(arr)):
            arr[i] = output[i]
            self._step_counter += 1


    def radix_sort(self, arr):
        if not arr:
            return

        if self._step_counting:
            self._step_counter = 0

        max_val = max(arr)

        if self._step_counting:
            exp = 1
            while max_val // exp > 0:
                self._counting_sort_with_step(arr, exp)
                exp *= 10
                self._step_counter += 1
        else:
            exp = 1
            while max_val // exp > 0:
                self._counting_sort(arr, exp)
                exp *= 10


    @property
    def step_count(self):
        return self._step_counter

    @property
    def step_counting(self):
        return self._step_counting

    @step_counting.setter
    def step_counting(self, value):
        self._step_counting = value