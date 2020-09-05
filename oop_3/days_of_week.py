def get_day_of_week(day_of_week: int) -> str:
    days = {
        1: "Mon",
        2: "Tue",
        3: "Wed",
        4: "Thu",
        5: "Fri",
        6: "Sat",
        7: "Sun"
    }
    return days.get(day_of_week, "Incorrect value")


def main():
    print(get_day_of_week(1))


if __name__ == "__main__":
    main()
