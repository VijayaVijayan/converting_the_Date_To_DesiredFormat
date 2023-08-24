from dateutil.parser import parse
def converting_Date():
    date_string = input("Enter the date: ")
    desired_format = input("Enter the desired format: ")
    given_input = parse(date_string)
    formatted_input = given_input.strftime(desired_format)
    print(formatted_input)
converting_Date()