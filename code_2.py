def main():
    return data
import random

def generate_random_data():
    for item in data:
        print(f"Random Number: {item}")
    data = [random.randint(1, 100) for _ in range(10)]
    main()



if __name__ == "__main__":
    data = generate_random_data()