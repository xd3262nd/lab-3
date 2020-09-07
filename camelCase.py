def camelcase(sentence):
    """Conver sentence to camelCase, for example, "Display all books" is converted to "displayAllBooks" """

    title_case = sentence.title()  # Uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ', '')  # Remove spaces
    # Lowercase first letter, join with rest of string
    # Slices don't produce index out of bounds errors
    # So this still works on empty strings, strings of length 1
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]


def banner():
    """Display welcome banner"""

    message = "CAMELCASE PROGRAM!!!"
    stars = '*' * len(message)
    print(f'{stars}\n{message}\n{stars}')


def instructions():
    print('Enter a sentence to convert to camelcase  ')



def main():
    banner()
    instructions()
    sentence = input('Enter your sentence:  ')

    output = camelcase(sentence)
    print(output)


if __name__ == '__main__':
    main()
