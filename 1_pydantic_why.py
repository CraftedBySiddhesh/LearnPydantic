def insert_patient_data_1(name, age):
    # No type information is given for name and age
    # Python will accept ANY type at runtime

    print(name)   # Prints whatever is passed
    print(age)    # Even wrong types are printed without complaint
    print('Inserted in data base')

# Passing age as string instead of int
insert_patient_data_1('Siddhesh', 'Thirty')


def insert_patient_data_2(name: str, age: int):
    # Type hints are ONLY for:
    # - readability
    # - IDE help
    # - static checkers (mypy)
    # They are NOT enforced at runtime

    print(name)
    print(age)
    print('Inserted in data base')

# Still passing age as string
insert_patient_data_2('Siddhesh', 'Thirty')


def insert_patient_data_3(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Inserted in data base')
    else:
        raise TypeError('Incorrect Typeerror')


def insert_patient_data_3(name: str, age: int):
    # Type hints are NOT enforced at runtime in Python

    # PROBLEM:
    # 1. type() check is too strict (no subclasses, no flexibility)
    # 2. No automatic conversion (age="30" fails)
    # 3. Only checks type, not value (age = -10 passes)
    # 4. Validation + logic mixed together
    # 5. Poor error message (no field-level info)

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Inserted in data base')
    else:
        raise TypeError('Incorrect Typeerror')
    

def update_patient_data_3(name: str, age: int):
    # Type hints are NOT enforced at runtime in Python

    # PROBLEM:
    # 1. type() check is too strict (no subclasses, no flexibility)
    # 2. No automatic conversion (age="30" fails)
    # 3. Only checks type, not value (age = -10 passes)
    # 4. Validation + logic mixed together
    # 5. Poor error message (no field-level info)

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Inserted in data base')
    else:
        raise TypeError('Incorrect Typeerror')



def insert_patient_data_4(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('Age cant be neative.')
        else:
            print(name)
            print(age)
            print('Inserted in data base')
    else:
        raise TypeError('Incorrect Typeerror')