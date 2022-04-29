# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = [
    (2005, 6),
    (2001, 5),
    (2013, 8),
    (2011, 10),
    (2017, 5),
    (2006, 5),
    (2009, 8),
    (2021, 7),
    (2002, 6),
    (2007, 5),
    (2012, 9),
    (2014, 7),
    (2003, 6),
    (2019, 4),
    (2016, 5),
    (2015, 6),
    (2018, 4),
    (2008, 5),
    (2010, 11),
    (2004, 6),
    (2020, 4)
]

# Write your code below this line:
# Get the last-appearing series point, as a dict with the column names as keys.

def last_appearing_rate(keys, values):
  last_data_point = values[-1]
  dictionary = {
    keys[0] : last_data_point[0],
    keys[1] : last_data_point[1]
  }
  return dictionary

print(last_appearing_rate(columns, unemployment_rates))
print("---")

# Get the first five series points, in the order they appear, as a list of
# tuples.
def first_five_series_points(series):
  return series[0:4]

print(first_five_series_points(unemployment_rates))
print("---")

# Check if the years 2000 and 2010 are each included in the data series.
def check_years_present(value, data_series):
  list_of_years = []
  for x in data_series:
    (year_value, rate_value) = x
    list_of_years.append(year_value)
  return value in list_of_years

print(check_years_present(2000, unemployment_rates))
print(check_years_present(2010, unemployment_rates))
print("---")

# Get the unemployment rate for the most recent year.

def ue_rate(data_series):
  data_series.sort()
  year_data = data_series[-1]
  return year_data[1]

print(ue_rate(unemployment_rates))
print("---")

# Get all the unique years included in the series, as a set.

def unique_years(data_series):
  list_of_years = []
  for x in data_series:
    (year_value, rate_value) = x
    list_of_years.append(year_value)
  unique_years = set(list_of_years)
  return unique_years

print(unique_years(unemployment_rates))
print("---")

# Get the list of the unemployment rates, ordered by year.
def ordered_by_year(data_series):
  data_series.sort()
  return data_series

print(ordered_by_year(unemployment_rates))
print("---")

# Get the largest unemployment rate.
def largest_ue_rate(data_series):
  list_of_rates = []
  for x in data_series:
    (year_value, rate_value) = x
    list_of_rates.append(rate_value)
  largest_ue_rate = max(list_of_rates)
  return largest_ue_rate

print(largest_ue_rate(unemployment_rates))
print("---")

# Create a new series, in the same format as the original, with the
# "employment rate" instead of the "unemployment rate" (the rates are listed in
# percentages).

def employment_rate(data_series):
  years_list = [] # define list of years
  ue_rates_list = [] # define list of ue rates
  e_rates_list = [] # define list of e rates
  merged_list = [] # define new merged list
  for x in data_series: # run a loop on the data series
    (year_value, rate_value) = x # unpack the tuple
    years_list.append(year_value) # append year values to list
    ue_rates_list.append(rate_value) # append ue values to list
  for y in ue_rates_list: # run a loop on the ue values
    e_rate = 100 - y # calculate the e value
    e_rates_list.append(e_rate) # append the e values to the e list
  merged_list = [(years_list[i], e_rates_list[i]) for i in range(0, len(years_list))] # merge the lists
  return merged_list # return merged list

print(employment_rate(unemployment_rates))
print("---")

# Create a new series, in the same format as the original, but only containing
# the series points where the unemployment rate is at least 7.

def high_unemployment_rates(data_series):
  high_ue = [] # define a list for UE > 7
  for x in data_series: ## run a loop of the rates
    if x[1] > 7: ## if UE value is higher than 7
      high_ue.append(x) ## append to list
  return high_ue ## return list

print(high_unemployment_rates(unemployment_rates))
print("---")

# Create a dict containing the count of the number of times each unemployment
# rate appears in the series.

def unique_values_dict(data_series):
  all_ue_rates = [] # define a list for all of the ue rates
  ue_rates_dict = {} # define a dictionary to store values
  for x in data_series: # run a loop on the ue rates
    (year_value, rate_value) = x # unpack the tuple
    all_ue_rates.append(rate_value) # append the rates value to the rates list
  for y in all_ue_rates: # run a loop for the rates list
    if y in ue_rates_dict: # if value exists
      ue_rates_dict[y] += 1 # increment existing key by 1
    else:# if value is new
      ue_rates_dict[y] = 1 # create new key, increment by 1
  return ue_rates_dict

print(unique_values_dict(unemployment_rates))
