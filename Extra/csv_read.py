import csv

def print_fields_and_values(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(">> ", end="")
            for field, value in row.items():
                print("{}={} ".format(field, value), end="")
            print()

if __name__ == "__main__":
    print_fields_and_values('TSLA.csv')
