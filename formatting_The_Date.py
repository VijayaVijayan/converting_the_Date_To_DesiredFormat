import datetime
def converting_Date(date_string):
    given_input = datetime.datetime.strptime(date_string,"%Y/%d/%m")
    formatted_input = given_input.strftime("%A,%Y %b %d")
    print(formatted_input)
converting_Date("2023/11/03")