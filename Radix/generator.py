import numpy as np

data_file = []
for data in range(100):
    dataset = []
    for size in range(np.random.randint(100, 10_000)):
        dataset.append(np.random.randint(1, 100_000))
    data_file.append(dataset)

np.save('data.npy', np.array(data_file, dtype=object))


sorted_data_file = sorted(data_file, key=lambda x: len(x))
np.save('sorted_data.npy', np.array(sorted_data_file, dtype=object))






