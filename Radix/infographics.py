import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd
from radix_sort import RadixSort


data = np.load("sorted_data.npy", allow_pickle=True)
radix = RadixSort()


length_list = []
for dataset in data:
    length_list.append(len(dataset))

time_list = []
for dataset in data:
    start = time.time()
    radix.radix_sort(dataset)
    end = time.time()
    time_list.append((end-start)*1000)

step_list = []
radix.step_counting = True
for dataset in data:
    radix.radix_sort(dataset)
    step_list.append(radix.step_count)



length_series = pd.Series(length_list)
step_series = pd.Series(step_list)
time_series = pd.Series(time_list)

df = pd.concat([length_series, step_series, time_series], axis=1)
df.columns = ['Длина', 'Шаги', 'Время']
df.to_excel('results_dataframe.xlsx', index=False, sheet_name='Sheet1')
print(df)
print(df.describe())


plt.plot(length_list, step_list)
plt.title("Количество шагов от длины")
plt.xlabel("Длина")
plt.ylabel("Шаги")
plt.grid(True)
plt.show()

plt.plot(length_list, time_list)
plt.title("Время от длины")
plt.xlabel("Длина")
plt.ylabel("Время")
plt.grid(True)
plt.show()
