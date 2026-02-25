from time import time


def main():
    start = time()

    # Python program to create acronyms
    word = "Artificial Intelligence"
    text = word.split()
    a = ""
    for i in text:
        a = a + i[0].upper()
    print(a)

    end = time()
    execution_time = end - start
    print("Execution Time : ", execution_time)


if __name__ == '__main__':
    main()
