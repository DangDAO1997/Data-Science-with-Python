import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

WEEK_DAYS = {
    'monday':MONDAY,
    'tuesday':TUESDAY,
    'wednesday':WEDNESDAY,
    'thursday':THURSDAY,
    'friday':FRIDAY,
    'saturday':SATURDAY,
    'sunday':SUNDAY,
    'all': -1
}

MONTHS = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'all': -1
}

def show_raw_data(df: pd.DataFrame):
    """ Show 5 raw data after filter """

    view_data = input("Would you like to view 5 rows of individual trip data? Enter 'yes' if you wanna it!: ").lower()
    if view_data == "yes":
        start_loc = 0
        while len(df.values):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue? Enter 'no' if you don't!: ").lower()
            if view_display == "no":
                break

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nInput city name:\n').lower()
        csvFile = CITY_DATA.get(city)
        if csvFile:
            break
        print("city not found")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        monthInput = input('\nInput month:\n').lower()
        month = MONTHS.get(monthInput)
        if month:
            break
        print("month not found")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        weekdayInput = input('\nInput weekday:\n').lower()
        weekday = WEEK_DAYS.get(weekdayInput)
        if weekday!= None:
            break
        print("weekday not found")
    print('-'*40)
    return city, month, weekday


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    csvFile = CITY_DATA[city]
    df = pd.read_csv(csvFile)
    df["Start Time"] = pd.to_datetime(df["Start Time"], format=f'%m/%d/%Y %H:%M')
    df["End Time"] = pd.to_datetime(df["End Time"], format=f'%m/%d/%Y %H:%M')
    df["Month"] = df["Start Time"].dt.month
    df["Weekday"] = df["Start Time"].dt.weekday
    df["Hour"] = df["Start Time"].dt.hour
    if month != -1:
        df = df[df["Start Time"].dt.month == month]
    if day != -1:
        df = df[df["Start Time"].dt.weekday == day]
    show_raw_data(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
