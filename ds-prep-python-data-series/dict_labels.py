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
    2002: 6,
    2020: 4,
    2007: 5,
    2015: 6,
    2010: 11,
    2014: 7,
    2001: 5,
    2006: 5,
    2004: 6,
    2009: 8,
    2013: 8,
    2008: 5,
    2021: 7,
    2018: 4,
    2011: 10,
    2005: 6,
    2016: 5,
    2019: 4,
    2012: 9,
    2017: 5,
    2003: 6
}

# Write your code below this line:
# Get the last-appearing series point, as a dict with the column names as keys.

def last_value(keys_values, values):
  last_item = values.popitem() ## define a list as the dict items as tuple pair
  (value1, value2) = last_item ## unpack the tuple
  dictionary = {keys_values[0]: value1,
                keys_values[1]: value2
              }
  return dictionary

print(last_value(columns, unemployment_rates))
print("---")

# Get the first five series points, in the order they appear, as a list of
# tuples.

def first_five_years(data_series):
  years_list = list(data_series.keys()) # convert keys to list
  rate_list = list(data_series.values()) # convert values to list
  merged_list = [(years_list[i], rate_list[i]) for i in range(0, len(years_list))] # merge list into list of tuples
  merged_list_first_five = merged_list[0:5]
  return merged_list_first_five # return value

print(first_five_years(unemployment_rates))
print("---")

# Check if the years 2000 and 2010 are each included in the data series.

def year_included(year, data_series):
  get_keys = data_series.keys() # return list of keys
  return year in get_keys # check year value present

print(year_included(2000, unemployment_rates))
print(year_included(20010, unemployment_rates))
print("---")

# Get the unemployment rate for the most recent year.

def highest_unemployment_rate_year(data_series):
  years_list = data_series.keys() # get the list of years as keys
  max_year = max(years_list)# return the highest value year
  return data_series[max_year] # return rate value of the high value year

print(highest_unemployment_rate_year(unemployment_rates))
print("---")

# Get all the unique years included in the series, as a set.

def unique_years(data_series):
  years_list = data_series.keys() # get the list of years as keys
  years_set = set(years_list) # convert list to set
  return years_set # return the set

print(unique_years(unemployment_rates))
print("---")

# Get the list of the unemployment rates, ordered by year.

def unemployment_rates_sorted(data_series):
  dict_items = data_series.items() # get key value items as list
  sorted_items = sorted(dict_items) # sort the list
  return sorted_items # return the sorted list

print(unemployment_rates_sorted(unemployment_rates))
print("---")

# Get the largest unemployment rate.

def highest_unemployment_rate(data_series):
  dict_values = data_series.values()
  return max(dict_values)

print(highest_unemployment_rate(unemployment_rates))
print("---")

# Create a new series, in the same format as the original, with the
# "employment rate" instead of the "unemployment rate" (the rates are listed in
# percentages).

def employment_rate(data_series):
  e_rate_list = [] # define a e rate list
  years_list = list(data_series.keys()) # convert keys to list
  ue_rate_list = list(data_series.values()) # convert values to list
  for x in ue_rate_list: # run a loop for ue rate list
    e_rate_list.append(100-x) # calc e rates, append to e rates list
  merged_dict = dict(zip(years_list, e_rate_list)) # merge year and e rate list
  return merged_dict # return dict for years and e rate

print(employment_rate(unemployment_rates)) # print
print("---")

# Create a new series, in the same format as the original, but only containing
# the series points where the unemployment rate is at least 7.

def ue_over_7(data_series):
  new_dict = {} # define an empty dict
  for key, value in data_series.items(): # create a loop for key, values
    if value >= 7: # if value > 7
      new_dict[key] = value # append to new_dict
  return new_dict #return new dict

print(ue_over_7(unemployment_rates))
print("---")

# Create a dict containing the count of the number of times each unemployment
# rate appears in the series.

def unique_ue_rates(data_series):
  dict_unique_ue_rates = {} # define a dict of ue rates
  rates_list = list(data_series.values()) # run a loop of ue rates list
  for x in rates_list: # if value is existing
    if x in dict_unique_ue_rates:
      dict_unique_ue_rates[x] += 1 # increment existing key by 1
    else: # if value is new
      dict_unique_ue_rates[x] = 1 # create new key, increment by 1
  return dict_unique_ue_rates # return the dict of ue rates

print(unique_ue_rates(unemployment_rates))
