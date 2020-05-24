import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTH_DATA = ['1', '2', '3', '4', '5', '6', 'all']

DAY_DATA = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter"""

    print('Hello! Let\'s explore some US bikeshare data!')
    city = str(input("Would you like to see data for Chicago, New York City, or Washington? \n").lower())
    while city not in CITY_DATA.keys():
        city = input("That is not a valid city. Please enter the city you would like to explore: Chicago, New York City, or Washington. Check for spelling errors. \n").lower()
    month = input("Would you like to filter data for just one month? If so, enter the month number. If not, enter 'All' \n").lower()
    while month not in MONTH_DATA:
        month = input("That is not a valid month. Please enter the number corresponding to month you would like to explore:\n").lower()
    day = str(input("Would you like to filter data down to a specific day of the week? If not, enter 'All' \n").title())
    while day not in DAY_DATA:
        day = str(input("That is not a valid day. Please enter the day of the week you would like to explore:\n").title())

    return city, month, day

def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day"""

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name() #ojo, might have to change to weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['Start_End_Station'] = df['Start Station']+' '+ df['Start Station']
    if month != 'all':
        month = MONTH_DATA.index(month)+1
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    print("This analysis will use the following data:\n-City: {}\n-Month: {}\n-Day of the week: {}".format(city, month, day))
    print('-'*40)
    return df


def time_stats(df, city, month, day):
    """Display statistis on travel times

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        specified by user
        (str) city -  city used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) month -  month used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) day - day used to analyze data. Used to display filters at the
        beginning of the stats display
    Returns:
        (int) common_month - month number with most rides
        (int) common_day - day name with most rides
        (int) common_hour - start hout with most rides
        (int) count_common_month - count of trips with common_month
        (int) count_common_day - count of trips with common_day
        (int) count_common_hour - count of trips with common_hour"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('Filters: City: {}. Month: {}. Day of the week: {}\n'.format(city, month, day))

    if month == 'all' and day == 'All':
        common_month = df['month'].mode()[0] # TO DO: get the most common month
        count_common_month = (df['month'] == common_month).sum()
        print('The most common month of travel is: {}. Count of trips: {}'.
              format(common_month, count_common_month))
        common_day = df['day_of_week'].mode()[0] # TO DO: display the most common day of week
        count_common_day = (df['day_of_week'] == common_day).sum()
        print('The most common day of travel is: {}. Count of trips: {}'.
              format(common_day, count_common_day))
        common_hour = df['hour'].mode()[0] # TO DO: display the most common start hour
        count_common_hour = (df['hour'] == common_hour).sum()
        print('The most common hour to start travel is: {}. Count of trips: {}'.
              format(common_hour, count_common_hour))

    elif month == 'all' and day != 'All':
        common_day = day
        count_common_day = ""
        common_month = df['month'].mode()[0] # TO DO: get the most common month
        count_common_month = (df['month'] == common_month).sum()
        print('The most common month of travel is: {}. Count of trips: {}'.
              format(common_month, count_common_month))
        common_hour = df['hour'].mode()[0] # TO DO: display the most common start hour
        count_common_hour = (df['hour'] == common_hour).sum()
        print('The most common hour to start travel is: {}. Count of trips: {}'.
              format(common_hour, count_common_hour))

    elif month != 'all' and day == 'All':
        common_month = month
        count_common_month = ""
        common_day = df['day_of_week'].mode()[0] # TO DO: display the most common day of week
        count_common_day = (df['day_of_week'] == common_day).sum()
        print('The most common day of travel is: {}. Count of trips: {}'.
              format(common_day, count_common_day))
        common_hour = df['hour'].mode()[0] # TO DO: display the most common start hour
        count_common_hour = (df['hour'] == common_hour).sum()
        print('The most common hour to start travel is: {}. Count of trips: {}'.
              format(common_hour, count_common_hour))
    else:
        common_month = month
        count_common_month = ""
        common_day = day
        count_common_day = ""
        common_hour = df['hour'].mode()[0] # TO DO: display the most common start hour
        count_common_hour = (df['hour'] == common_hour).sum()
        print('The most common hour to start travel is: {}. Count of trips: {}'.
              format(common_hour, count_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return common_month, common_day, common_hour, count_common_month, count_common_day, count_common_hour


def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        specified by user
        (str) city -  city used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) month -  month used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) day - day used to analyze data. Used to display filters at the
        beginning of the stats display

    Returns:
        (int) common_start_station - start station  with most rides
        (int) common_end_station - end station with most rides
        (int) common_start_end_station - start end combo station with most rides
        (int) count_common_start_station - count of trips with common_start_station
        (int) count_common_end_station - count of trips with ccommon_end_station
        (int) count_common_start_end - count of trips with count_common_start_station"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('Filters: City: {}. Month: {}. Day of the week: {}\n'.format(city, month, day))

    common_start_station = df['Start Station'].mode()
    count_common_start_station = (df['Start Station'] == common_start_station).sum()
    print('Most common start station is {}. Count of trips: {}'.
          format(common_start_station, count_common_start_station))
    common_end_station = df['End Station'].mode()
    count_common_end_station = (df['End Station'] == common_end_station).sum()
    print('Most common end station is {}.Count of trips: {}'.
          format(common_start_station, count_common_end_station))
    common_start_end_station = df['Start_End_Station'].mode()
    count_common_start_end = (df['Start_End_Station'] == common_start_end_station).sum()
    print('Most common combination of start and end station is {}. Count of trips {}'.
          format(common_start_end_station, count_common_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return common_start_station, common_end_station, common_start_end_station, count_common_start_station, count_common_end_station, count_common_start_end


def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        specified by user
        (str) city -  city used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) month -  month used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) day - day used to analyze data. Used to display filters at the
        beginning of the stats display

    Returns:
        (int) total_trip_duration - sum of all trip duration. Unit: minutes
        (int) average_trip_duration - average of all trip duration. Unit: minutes"""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('Filters: City: {}. Month: {}. Day of the week: {}\n'.format(city, month, day))

    total_trip_duration = df['Trip Duration'].sum()
    print("The total trip duration is {} minutes".format(total_trip_duration))
    average_trip_duration = df['Trip Duration'].mean()
    print("The average trip duration is {} minutes".format(average_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return total_trip_duration, average_trip_duration

def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        specified by user
        (str) city -  city used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) month -  month used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) day - day used to analyze data. Used to display filters at the
        beginning of the stats display
    Returns:
        count_user_types - DataFrame with count of users by User Type
        count_gender - DataFrame with count of users by Gender
        (int) earliest_year - earliest year of birth
        (int) most_recent_year - most recent year of birth
        (int) common_year - most common year of birth"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('Filters: City: {}. Month: {}. Day of the week: {}\n'.format(city, month, day))

    count_user_types = df['User Type'].value_counts()
    print("Count of types of users: \n {}\n".format(count_user_types))

    count_gender = ""
    earliest_year = ""
    most_recent_year = ""
    common_year = ""

    if city != 'washington':
        count_gender = df['Gender'].value_counts()
        print("Count of users by gender: \n {}\n".format(count_gender))
        earliest_year = df['Birth Year'].min()
        print("The oldest riders were born {}".format(earliest_year))
        most_recent_year = df['Birth Year'].max()
        print("The youngest riders were born {}".format(most_recent_year))
        common_year = df['Birth Year'].mode()[0]
        print("Most of the riders were born {}".format(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return count_user_types, count_gender, earliest_year, most_recent_year, common_year

def display_data(df, city, month, day):
    """Displays raw data.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        specified by user
        (str) city -  city used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) month -  month used to analyze data. Used to display filters at the
        beginning of the stats display
        (str) day - day used to analyze data. Used to display filters at the
        beginning of the stats display
    Returns:
        df - a portion of the original DataFrame every time displaying 5 more rows"""

    count = 5
    answers = ('yes', 'no')
    answer = input("Now that we have seen the statistics, would you like to see raw data? Answer yes or no: ")
    while answer not in answers:
        answer = input('That is not a valid answer. Please answer yes or no, would you like to see raw data? ').lower()
    if answer == 'yes':
        print('\nFilters: City: {}. Month: {}. Day of the week: {}\n'.format(city, month, day))
        print(df[0:count])
    while True:
        answer_2 = input("Would you like to see more data? Answer yes or no: ")
        while answer_2 not in answers:
            answer_2 = input('That is not a valid answer. Please answer yes or no, would you like to see more raw data? ').lower()
        if answer_2 == 'yes':
            count += 5
            print('Filters: City: {}. Month: {}. Day of the week: {}\n'.format(city, month, day))
            print(df[0:count])
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city, month, day)
        display_data(df, city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
