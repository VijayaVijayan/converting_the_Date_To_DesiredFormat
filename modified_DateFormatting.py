import datetime

def is_valid_format_code(symbol):
    valid_format_codes = [
        "%a", "%A", "%w", "%d", "%b", "%B", "%m", "%y", "%Y",
        "%H", "%I", "%p", "%M", "%S", "%f", "%Z", "%j", "%U",
        "%W", "%c", "%C", "%x", "%X", "%%", "%G", "%u", "%V"
    ]
    return any(symbol.startswith(valid) for valid in valid_format_codes)

def converting_Date():
    format_mapping = {
        "%a": "Weekday as Sun, Mon",
        "%A": "Weekday as full name as Sunday, Monday",
        "%w": "Weekday as decimal no as 0, 1, 2...",
        "%d": "Day of month as 01, 02",
        "%b": "Months as Jan, Feb",
        "%B": "Months as January, February",
        "%m": "Months as 01, 02",
        "%y": "Year without century as 11, 12, 13",
        "%Y": "Year with century 2011, 2012",
        "%H": "24 Hours clock from 00 to 23",
        "%I": "12 Hours clock from 01 to 12",
        "%p": "AM, PM",
        "%M": "Minutes from 00 to 59",
        "%S": "Seconds from 00 to 59",
        "%f": "Microseconds 6 decimal numbers"

    }

    try:
        date_string = input("Enter the date (YYYY/DD/MM %H:%M:%S): ")
        given_input = datetime.datetime.strptime(date_string, "%Y/%d/%m %H:%M:%S")
        print("\nAvailable format codes:")
        for symbol, description in format_mapping.items():
            print(f"{symbol}: {description}")
        format_string = input("\nEnter the desired format: ")
        invalid_format_codes = [symbol for symbol in format_string.split() if not is_valid_format_code(symbol)
                                          and not any(symbol.startswith(char) for char in ['(', '['])]

        if invalid_format_codes:
            print("Invalid format code:", ','.join(invalid_format_codes))
            return
        try:
            formatted_input = given_input.strftime(format_string)
            print("Formatted date:", formatted_input)
        except ValueError as ve:
            print("Invalid format:", ve)
    except ValueError as e:
        print("VALUE ERROR:", e)
converting_Date()