import research


def main():
    data = research.load_file()
    year = get_year()

    max_births = max_births_in_day(data, year)
    print(
        f'{max_births[0].date_of_month}/{max_births[0].month}/{max_births[0].year} has {max_births[0].births} births')

    births_in_year = count_births_in_year(data, year)

    print(f'In {year} were born {births_in_year:,} babies')


def get_year():
    try:
        year = int(input('Choose the year (2000-2014) '))
        if year < 2000 or year > 2014:
            raise ValueError
    except ValueError:
        year = 2000
        print(
            f'You may only input year between 2000 and 2014. Default value is {year}')

    return year


def max_births_in_day(data, year):
    years = [r for r in data if r.year == year]
    sort_year = sorted(years, key=lambda r: -r.births)

    return sort_year[:5]


def count_births_in_year(data, year):
    years = [r for r in data if r.year == year]
    return sum(r.births for r in years)


if __name__ == "__main__":
    main()
