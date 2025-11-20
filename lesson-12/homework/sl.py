Exercise 1: Threaded Prime Number Checker
import threading

def is_prime(n):
    """Проверка, является ли число простым"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    """Проверяет диапазон чисел и добавляет простые числа в общий список"""
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    """Главная функция для многопоточной проверки простых чисел"""
    threads = []
    result = []
    step = (end - start) // num_threads
    for i in range(num_threads):
        sub_start = start + i * step
        sub_end = start + (i + 1) * step if i != num_threads - 1 else end
        t = threading.Thread(target=check_primes, args=(sub_start, sub_end, result))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    result.sort()
    return result

# Пример использования
if __name__ == "__main__":
    primes = threaded_prime_checker(1, 100, num_threads=4)
    print("Prime numbers:", primes)




Exercise 2: Threaded File Processing (Word Count)
import threading
from collections import Counter

def count_words(lines, result):
    """Считает количество слов в переданных строках"""
    counter = Counter()
    for line in lines:
        words = line.strip().split()
        counter.update(words)
    result.append(counter)

def threaded_file_word_count(file_path, num_threads=4):
    """Многопоточный подсчет слов в файле"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    threads = []
    results = []
    step = len(lines) // num_threads

    for i in range(num_threads):
        sub_lines = lines[i * step : (i + 1) * step] if i != num_threads - 1 else lines[i * step :]
        t = threading.Thread(target=count_words, args=(sub_lines, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Объединяем результаты всех потоков
    final_count = Counter()
    for counter in results:
        final_count.update(counter)

    return final_count

# Пример использования
if __name__ == "__main__":
    word_count = threaded_file_word_count("example.txt", num_threads=4)
    print("Word occurrences:", word_count)
