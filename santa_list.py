from tabulate import tabulate
import sys


class Person:
    def __init__(self, f_name, l_name, age, gift, n_n):
        self.name = f_name + " " + l_name
        self.age = age
        self.gift = gift
        self.n_n = n_n

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gift: {self.gift}"


class List:
    def __init__(self):
        self.santas_list = {}

    def add_list(self, *args):
        for arg in args:
            self.santas_list[arg.name, arg.age] = ""

    def __str__(self):
        header = ["Name", "Age", "Gift"]
        new_list = []
        for (name, age), gift in self.santas_list.items():
            new_list.append([name, age, gift])
        self.formatted_list = tabulate(new_list, headers=header, tablefmt="rst")
        return self.formatted_list


def main():
    santa_list = List()
    people = []

    print("\nSANTA'S LIST!\n~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
    print("Start by entering in the information below. type 'Exit' to exit.")
    while True:
        age_value = True
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        name = input("Full Name: ").title()
        if name == "Exit":
            print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\nPerson not added to Santa's List")
            break
        while age_value is True:
            age = input("Age: ").title()
            if age == "Exit":
                print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\nPerson not added to Santa's List")
                age_value = False
                break
            try:
                age = int(age)
                break
            except ValueError:
                print(f"WARNING: ({age}) invalid entry!")
                continue
        if age_value == False:
            break
        gift = input("Gift: ").title()
        if gift == "Exit":
            print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\nPerson not added to Santa's List")
            break
        while True:
            n_n = input("Naughty or Nice?: ").title()
            if n_n == "Exit":
                print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\nPerson not added to Santa's List")
                break
            if n_n != "Naughty" and n_n != "Nice":
                print(f"({n_n}) is neither 'Naughty' or 'Nice'")
                continue
            else:
                break
        try:
            f_name = name.split(" ")[0]
            l_name = name.split(" ")[1]
            people.append([f_name, l_name, age, gift, n_n])
        except IndexError:
            print(f"~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n({name}) must be formatted as: John Doe. Re-enter person.")

    people_instances = []
    try:
        if len(people) > 0:
            for individual in people:
                people_instances.append(
                    Person(individual[0], individual[1], individual[2], individual[3], individual[4])
                )

            add_to_list(santa_list, *people_instances)

            while True:
                generate = input("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\nGenerate Santa's List? (y/n): ").lower()
                if generate == "y" or generate == "yes":
                    for people in people_instances:
                        if people.n_n == "Nice":
                            is_nice(santa_list, people)
                        elif people.n_n == "Naughty":
                            is_naughty(santa_list, people)

                    break

                elif generate == "n" or generate == "no":
                    warn = input(
                        "~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\nWARNING: Santa's List will be cleared, continue? (y/n): "
                    ).lower()
                    if warn == "y" or warn == "yes":
                        sys.exit(0)
                    elif warn == "n" or warn == "no":
                        continue
                    else:
                        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\nInvalid input\n~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
                elif generate == "exit":
                    sys.exit(0)
            print("\n~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n\tSANTA'S LIST\n~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
            print(santa_list)
            print_list(santa_list.formatted_list)
        else:
            print("No people added to Santa's List\n~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
            sys.exit(0)
    except UnboundLocalError:
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\nExiting Santa's List\n~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        sys.exit(0)


def is_nice(list_instance, *persons):
    for person in persons:
        key = person.name, person.age
        if key in list_instance.santas_list:
            list_instance.santas_list[key] = person.gift


def is_naughty(list_instance, *persons):
    for person in persons:
        key = person.name, person.age
        if key in list_instance.santas_list:
            list_instance.santas_list[key] = "\U0001F4A9"


def add_to_list(list_instance, *persons):
    for person in persons:
        list_instance.add_list(person)
    return list_instance


def print_list(finished_list):
    path = "Santa_List/santas_list.txt"
    with open(path, "w") as file:
        file.write(finished_list)


if __name__ == "__main__":
    main()
