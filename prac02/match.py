day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("weekday")
    case 6 | 7:
        print("weekend")

day = 4
match day:
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Looking forward to the Weekend")