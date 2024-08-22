calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(s):
    count_calls()
    length = len(s)
    upper = s.upper()
    lower = s.lower()
    return (length, upper, lower)

def is_contains(s, list_to_search):
    count_calls()
    s_lower = s.lower()
    list_to_search_lower = [item.lower() for item in list_to_search]
    return s_lower in list_to_search_lower

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # True
print(is_contains('cycle', ['recycling', 'cyclic'])) # False

print(calls)
