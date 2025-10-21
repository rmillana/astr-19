import numpy as np

def main():
    num_entries = 1000

    x = np.linspace(0, 2, num_entries)

    y = np.sin(x)

    print(f"{'x':>10} {'sin(x)':>10}")
    print("-" * 22)

    for i in range(num_entries):
        print(f"{x[i]: 10.6f} {y[i]: 10.6f}")

if __name__ == "__main__":
    main()