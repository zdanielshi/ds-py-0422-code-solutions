# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = {
    'year': [
        2009, 2011, 2005, 2016, 2001,
        2012, 2019, 2007, 2021, 2018,
        2010, 2013, 2006, 2017, 2015,
        2014, 2008, 2004, 2003, 2020,
        2002
    ],
    'unemployment_rate': [
        8, 10, 6, 5, 5,
        9, 4, 5, 7, 4,
        11, 8, 5, 5, 6,
        7, 5, 6, 6, 4,
        6
    ]
}

# Write your code below this line:

# Get the last-appearing series point, as a dict with the column names as keys.

def last_data_point(keys, data_series):
  last_year = data_series['year'][-1]
  last_rate = data_series['unemployment_rate'][-1]
  dictionary = { keys[0]:last_year , keys[1]:last_rate }
  return dictionary

print(last_data_point(columns, unemployment_rates))
print("---")

# Get the first five series points, in the order they appear, as a list of
# tuples.

def first_five_data_points(data_series):
  first_five_years = data_series['year'][0:5] # get first 5 items in year as list
  first_five_rates = data_series['unemployment_rate'][0:5] # get first 5 items in ue rate as list
  merged_list = []
  for i in range(0,len(first_five_years)): # run a loop for the range of the first five lists
    merged_list.append([first_five_years[i], first_five_rates[i]]) # append the merged values to merged list
  return merged_list # return merged list

print(first_five_data_points(unemployment_rates))
print("---")

# Check if the years 2000 and 2010 are each included in the data series.

def years_present(year, data_series):
  present = year in data_series['year']
  return present

print(years_present(2000,unemployment_rates))
print(years_present(2010,unemployment_rates))
print("---")

# Get the unemployment rate for the most recent year.

def latest_year_unemployment(data_series):
  years = data_series['year'] # separate out the years list
  rates = data_series['unemployment_rate']
  max_year = max(years) # find the highest value year
  index = years.index(max_year) # return the index value of the year
  rate = rates[index] # find the value of that index position in rates
  return rate # return

print(latest_year_unemployment(unemployment_rates))
print("---")

# Get all the unique years included in the series, as a set.

def unique_years(data_series):
  years = data_series['year'] # separate years into list
  years_set = set(years) # turn list into set
  return years_set # return the set

print(unique_years(unemployment_rates))
print("---")

# Get the list of the unemployment rates, ordered by year.

def ordered_by_year(data_series):
  years_list = data_series['year'] # separate out the list of years
  rates_list = data_series['unemployment_rate'] # separate out the list of rates
  years_list, rates_list = zip(*sorted(zip(years_list, rates_list))) # zip, sort, zip
  return rates_list #return the rates list

print(ordered_by_year(unemployment_rates))
print("---")

# Get the largest unemployment rate.

def highest_unemployment_rate(data_series):
  rates_list = data_series['unemployment_rate'] # separate out rates into list
  max_rate = max(rates_list) # find the max value
  return max_rate

print(highest_unemployment_rate(unemployment_rates))
print("---")

# Create a new series, in the same format as the original, with the
# "employment rate" instead of the "unemployment rate" (the rates are listed in
# percentages).

def employment_rates(data_series):
  e_rates_dict = {} # create a new dict
  e_rates_list = [] # create new e rates list
  years_list = data_series['year'] # separate years to list
  ue_rates_list = data_series['unemployment_rate'] # seprate ue rates to list
  for x in ue_rates_list: # run loop on ue rates
    e_rates_list.append(100-x) # calc e rates and append to e rates list
  e_rates_dict['year'] = years_list # add year to new dict
  e_rates_dict['employment_rate'] = e_rates_list # add rates to new dict
  return e_rates_dict# return new dict

print(employment_rates(unemployment_rates))
print("---")

# Create a new series, in the same format as the original, but only containing
# the series points where the unemployment rate is at least 7.

def rates_over_7(data_series):
  years_list = data_series['year'] # create a years list
  rates_list = data_series['unemployment_rate'] # create a rates list
  years_over_7 = [] # define a over 7 years list
  rates_over_7 = [] # define a over 7 rates list
  new_dict = {} # define a new dict
  for i in range(0,len(years_list)): # do an iterable
    if rates_list[i] >= 7: # filter for rates values over 7
      years_over_7.append(years_list[i]) # append to over 7 years list
      rates_over_7.append(rates_list[i]) # append to over 7 rates list
  new_dict['year'] = years_over_7 # add over 7 years to new dict
  new_dict['unemployment_rate'] = rates_over_7 # add over 7 rates to new dict
  return new_dict # return new dict

print(rates_over_7(unemployment_rates))
print("---")

# Create a dict containing the count of the number of times each unemployment
# rate appears in the series.

def count_ue_rates(data_series):
  all_ue_rates = unemployment_rates['unemployment_rate']
  unique_ue_rates = {}
  for x in all_ue_rates: # run a loop for all ue rates list
    if x in unique_ue_rates: # if value is existing
      unique_ue_rates[x] += 1 # incremenet existing key by 1
    else: # if value is new
      unique_ue_rates[x] = 1 # create new key, increment by 1
  return unique_ue_rates # return the dictionary with unique rates count

print(count_ue_rates(unemployment_rates))
