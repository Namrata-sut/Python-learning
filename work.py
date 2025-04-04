# # namrata, pcotcvc
# def caesarCipher(s, k):
#     k = k % 26
#     alphabets_lower = 'abcdefghijklmnopqrstuvwxyz'
#     alphabets_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#     rotated_lower = alphabets_lower[k:] + alphabets_lower[:k]
#     rotated_upper = alphabets_upper[k:] + alphabets_upper[:k]
#
#     result = []
#
#     for char in s:
#         if char in alphabets_lower:
#             index = alphabets_lower.index(char)
#             result.append(rotated_lower[index])
#         elif char in alphabets_upper:
#             index = alphabets_upper.index(char)
#             result.append(rotated_upper[index])
#         else:
#             result.append(char)
#
#     return ''.join(result)
#
#
# st = 'namr-ata'
# n = 2
#
# print(caesarCipher(st, n))

import pandas as pd

# # Generate some data for DataFrame
# data = {
#    'Name': ['Steve', 'Lia', 'Vin', 'Katie'],
#    'Age': [32, 28, 45, 38],
#    'Gender': ['Male', 'Female', 'Male', 'Female'],
#    'Rating': [3.45, 4.6, 3.9, 2.78]
# }
# # Creating the DataFrame
# df = pd.DataFrame(data)
#
# # Display the DataFrame
# print(df)
#
# print("\nDataFrame Index Object Type:",df.index.dtype)

# import pandas as pd
#
# # Creating a CategoricalIndex
# categories = pd.CategoricalIndex(['a','b', 'a', 'c'])
# df = pd.DataFrame({'Col1': [50, 70, 90, 60], 'Col2':[1, 3, 5, 8]}, index=categories)
# print("Input DataFrame:\n",df)
#
# print("\nDataFrame Index Object Type:",df.index.dtype)

# import pandas as pd
#
# # Creating a IntervalIndex
# interval_idx = pd.interval_range(start=0, end=4)
#
# # Creating a DataFrame with IntervalIndex
# df = pd.DataFrame({'Col1': [1, 2, 3, 4], 'Col2':[1, 3, 5, 8]}, index=interval_idx)
#
# print("Input DataFrame:\n",df)
#
# print("\nDataFrame Index Object Type:",df.index.dtype)

# import pandas as pd
#
# # Create MultiIndex
# arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
# multi_idx = pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
#
# # Create a DataFrame with MultiIndex
# df = pd.DataFrame({'Col1': [1, 2, 3, 4], 'Col2':[1, 3, 5, 8]}, index=multi_idx)
#
# print("MultiIndexed DataFrame:\n",df)

# import pandas as pd
#
# # Create DatetimeIndex
# datetime_idx = pd.DatetimeIndex(["2020-01-01 10:00:00", "2020-02-01 11:00:00"])
#
# # Create a DataFrame with DatetimeIndex
# df = pd.DataFrame({'Col1': [1, 2], 'Col2':[1, 3]}, index=datetime_idx )
#
# print("DatetimeIndexed DataFrame:\n",df)


