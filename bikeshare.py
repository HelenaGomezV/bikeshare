import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Specify the city. Write exit to finish. Available ' + str(cities) + ' ').lower()
        if (city in cities):
            break               
        else:
            if (city == 'exit'):
                exit()            
            else:
                print(city)
                print('Error. Not available city. Check the spelling and the list of cities')
    
    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']       
    while True:
        month = input('Specify the month. Write exit to finish. Available ' + str(months) + ' ').lower()
        if (month in months):
            break
        else:
            if (month == 'exit'):
                exit()
            else:
                print('Error. Not available city. Write exit to finish. Check the spelling and the list of months')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:        
        day = input('Specify the day. Available ' +  str(days) + ' ').lower()
        if (day in days):
            break
        else:
            if (day == 'exit'):
                exit()
            else:                
                print('Error. Not available day. Check the spelling and the list of days')


    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])    
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])    

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        print(month)
    
        # filter by month to create the new dataframe
        df = df.query('month == ' + str(month))    
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month        
    popular_month = df['month'].mode()[0]
    print('The most common month is: ', popular_month)
    # display the most common day of week        
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', popular_day_of_week)
    # display the most common start hour
    popular_start_hour = df['Start Time'].dt.hour
    popular_start_hour = popular_start_hour.mode()[0]
    print('The most common hour is: ', popular_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', popular_start_station)
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', popular_end_station)
    # display most frequent combination of start station and end station trip
    popular_combination = df['Start Station'] + ' to ' + df['End Station']
    popular_combination = popular_combination.mode()[0]
    print ('The most frequent combination of start and end station is: ', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in hours is: ', (total_travel_time/3600))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time in hours is: ', (mean_travel_time/3600))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types is: ', user_types)
    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('The counts of gender is: ', gender)
        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year is: ', earliest_birth_year)
        
        recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year is: ', recent_birth_year)
        
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year is: ', common_birth_year)
    except KeyError as e:
        print('Inexistent Key: ', e)    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_raw_data():    
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Specify the city. Write exit to finish. Available ' + str(cities) + ' ').lower()
        if (city in cities):
            break               
        else:
            if (city == 'exit'):
                exit()            
            else:                
                print('Error. Not available city. Check the spelling and the list of cities')
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    start = 0
    number_elements_to_print = 5
    while True:
        restart = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if restart.lower() != 'yes' or (start > len(df)):
            break
        else:
            print(df.iloc[start:start + number_elements_to_print])
            start = start + number_elements_to_print

def main():        
    while True:
        print_raw_data()
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
