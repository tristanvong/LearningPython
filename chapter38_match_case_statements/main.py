# python version of switch case => more concise way to write bunch of if elif else

def get_month_by_num(month_nr):
    match month_nr:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"
        case _: # wildcard if other cases arent met same as default keyword in other languages
            return "Unknown month"

month = int(input("enter a month nr: "))
print(get_month_by_num(month))