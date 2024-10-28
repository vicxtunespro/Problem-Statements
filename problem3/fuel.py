def get_fraction():
    fraction = input("Fuel Fraction: ")
    nume, deno = fraction.split('/')
    deno = int(deno)
    nume = int(nume)
    convert_pec(nume, deno)

def convert_pec(a, b):
    feul_pec = round((a/b) * 100)

    if feul_pec <= 1:
        print("E")
    elif feul_pec == 100:
        print("F")
    else:
        print(f"Fuel Pecentage: {feul_pec}%")


def main():
    while True:
        try:
            get_fraction()
            return
        except ValueError:
            print("Value not a string")
        except ZeroDivisionError:
            print("Impossible to divid by zero")


if __name__ == '__main__':
    main()