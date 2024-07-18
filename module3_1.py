global calls
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(my_string):
    count_calls()
    result = (len(my_string), str.upper(my_string), str.lower(my_string))
    return result


def is_contains(my_string, list_to_search):
    count_calls()
    my_string = str.upper(my_string)
    for i in range(0, len(list_to_search)):
        list_to_search[i] = str.upper(str(list_to_search[i]))
    if my_string in list_to_search:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
