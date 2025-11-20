import numpy as np

# 1. Convert List to 1D Array
lst = [12.23, 13.32, 100, 36.32]
arr1 = np.array(lst)
print("1D Array:", arr1)

# 2. Create 3x3 Matrix (2-10)
arr2 = np.arange(2, 11).reshape(3, 3)
print("\n3x3 Matrix:\n", arr2)

# 3. Null Vector (10) & Update Sixth Value
arr3 = np.zeros(10)
arr3[5] = 11  # Шестой элемент (индекс 5)
print("\nNull Vector updated:", arr3)

# 4. Array from 12 to 38
arr4 = np.arange(12, 38)
print("\nArray from 12 to 37:", arr4)

# 5. Convert Array to Float Type
arr5 = np.array([1, 2, 3, 4])
arr5_float = arr5.astype(float)
print("\nArray converted to float:", arr5_float)

# 6. Celsius to Fahrenheit Conversion
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9/5 + 32
print("\nCelsius:", celsius)
print("Fahrenheit:", fahrenheit)

# 7. Append Values to Array
arr7 = np.array([10, 20, 30])
arr7_appended = np.append(arr7, [40, 50, 60, 70, 80, 90])
print("\nAppended Array:", arr7_appended)

# 8. Array Statistical Functions
arr8 = np.random.randint(0, 100, 10)
mean_val = np.mean(arr8)
median_val = np.median(arr8)
std_val = np.std(arr8)
print("\nRandom Array:", arr8)
print("Mean:", mean_val, "Median:", median_val, "Std Dev:", std_val)

# 9. Find min and max
arr9 = np.random.random((10, 10))
min_val = np.min(arr9)
max_val = np.max(arr9)
print("\n10x10 Array Min:", min_val, "Max:", max_val)

# 10. Create a 3x3x3 array with random values
arr10 = np.random.random((3, 3, 3))
print("\n3x3x3 Array:\n", arr10)
