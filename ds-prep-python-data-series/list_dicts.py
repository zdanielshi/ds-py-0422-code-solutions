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
    {"unemployment_rate": 8, "year": 2013},
    {"unemployment_rate": 5, "year": 2006},
    {"unemployment_rate": 5, "year": 2017},
    {"unemployment_rate": 6, "year": 2015},
    {"unemployment_rate": 6, "year": 2002},
    {"unemployment_rate": 4, "year": 2019},
    {"unemployment_rate": 9, "year": 2012},
    {"unemployment_rate": 4, "year": 2018},
    {"unemployment_rate": 6, "year": 2003},
    {"unemployment_rate": 5, "year": 2007},
    {"unemployment_rate": 11, "year": 2010},
    {"unemployment_rate": 7, "year": 2014},
    {"unemployment_rate": 6, "year": 2004},
    {"unemployment_rate": 5, "year": 2016},
    {"unemployment_rate": 6, "year": 2005},
    {"unemployment_rate": 7, "year": 2021},
    {"unemployment_rate": 5, "year": 2001},
    {"unemployment_rate": 4, "year": 2020},
    {"unemployment_rate": 10, "year": 2011},
    {"unemployment_rate": 8, "year": 2009},
    {"unemployment_rate": 5, "year": 2008}
]

# Write your code below this line:
# Get the last-appearing series point, as a dict with the column names as keys.
def last_data_series(data_series):
  return data_series[-1]

print(last_data_series(unemployment_rates))
print("---")

# Get the first five series points, in the order they appear, as a list of
# tuples.

def first_five_data_series(data_series):
  rate_list = [] ## define rates list
  years_list = [] ## define years list
  for x in data_series: ## run a loop for all rows
    rate_list.append(x['unemployment_rate']) ## append rates values to rates list
    years_list.append(x['year']) ## append years values to years list
  merged_list = [(years_list[i], rate_list[i]) for i in range(0,len(years_list))] ## merge lists together into a list of tuples
  merged_list_first_five = merged_list[0:5]
  return merged_list_first_five ## isolate for the first five values

print(first_five_data_series(unemployment_rates))
print("---")

# Check if the years 2000 and 2010 are each included in the data series.

def check_years_present(data_series, year_value):
  years_list = []
  for x in data_series: ## run a loop to isolate each row
    years_list.append(x['year']) ## index the 'year' to return the year values
  return year_value in years_list ## append the individual year values to list

print(check_years_present(unemployment_rates, 2000)) ## check for 2000
print(check_years_present(unemployment_rates, 2010)) ## check for 2000
print("---")

# Get the unemployment rate for the most recent year.
def ue_rate_most_recent_year(data_series):
  years_list = [] ## define a years_list
  rates_list = [] ## define a rates list
  for x in data_series: ## run a loop to isolate each row
    years_list.append(x['year']) ## append years values to the years_list
    rates_list.append(x['unemployment_rate']) ## append unemployment rate values to the rates list
  highest_year = years_list.index(max(years_list)) ## return the index value of the highest year
  highest_year_rate = rates_list[highest_year] ## apply that index value to the rates list
  return highest_year_rate ## return the rate

print(ue_rate_most_recent_year(unemployment_rates))
print("---")

# Get all the unique years included in the series, as a set.
def unique_years(data_series):
  years_list = [] ## define a years list
  for x in data_series: ## run a loop to isolate each row
    years_list.append(x['year']) ## append years values to the years list
  unique_years_set = set(years_list) ## convert the unique years list to a set
  return unique_years_set ## return the set

print(unique_years(unemployment_rates))
print("---")

# Get the list of the unemployment rates, ordered by year.
def ordered_by_year(data_series):
  years_list = [] ## define a years_list
  rates_list = [] ## define a rates list
  for x in data_series: ## run a loop to isolate each row
    years_list.append(x['year']) ## append years values to the years_list
    rates_list.append(x['unemployment_rate']) ## append unemployment rate values to the rates list
  merged_list = [(years_list[i], rates_list[i]) for i in range(0,len(years_list))] ## merge the lists together
  merged_list.sort() ## sort the years column
  return merged_list

print(ordered_by_year(unemployment_rates))  ## print
print("---")

# Get the largest unemployment rate.
def largest_ue_rate(data_series):
  rates_list = [] ## define a rates list
  for x in data_series: ## run a loop to isolate each row
    rates_list.append(x['unemployment_rate']) ## append the rates values to the rates list
  return max(rates_list)## return the highest value from the rates list

print(largest_ue_rate(unemployment_rates))
print("---")

# Create a new series, in the same format as the original, with the
# "employment rate" instead of the "unemployment rate" (the rates are listed in
# percentages).
def employment_rate(data_series):
  years_list = [] ## define a years_list
  ue_rates_list = [] ## define an ue rates list
  e_rates_list = [] ## define an e rates list
  merged_list = []
  for x in data_series: ## run a loop to isolate each row
    years_list.append(x['year']) ## append years values to the years_list
    ue_rates_list.append(x['unemployment_rate']) ## append unemployment rate values to the rates list
  for x in ue_rates_list: ## calculate a list that's the inverse of rates list
    e_rates_list.append(100 - x)
  years_keys = ['year' for i in range(len(years_list))] ## generate a list of year keys that's the correct length
  e_rates_keys = ['employment_rate' for i in range(len(e_rates_list))] ## generate a list of e rate keys that's the correct length
  for i in range(len(years_list)):
    merged_list.append(dict(years_key = years_list, e_rates_keys = e_rates_list))
  return merged_list
  ## create a dictionary for each individual row
  ## append each row into a list
  ## return the list

print(employment_rate(unemployment_rates)) ## print
print("---")

# Create a new series, in the same format as the original, but only containing
# the series points where the unemployment rate is at least 7.

def high_ue_rates(data_series):
  high_ue_rate_year = [] ## define a list for high ue rate
  for x in data_series: ## run a loop for ue rates
    if x['unemployment_rate'] > 7: ## find ue rate higher than 7
      high_ue_rate_year.append(x) ## append those values to high ue rate list
  return high_ue_rate_year

print(high_ue_rates(unemployment_rates)) ## return the high ue rate list of dicts
print("---")

# Create a dict containing the count of the number of times each unemployment
# rate appears in the series.

def count_unique_rates(data_series):
  all_ue_rates = [] # define a list for all of the ue rates
  unique_ue_rates = {} # define a dictionary to store the end results
  for x in data_series: # run a loop for ue rates
    all_ue_rates.append(x['unemployment_rate']) ## extract only the individual ue rates into the list
  for x in all_ue_rates: # run a loop for all ue rates list
    if x in unique_ue_rates: # if value is existing
      unique_ue_rates[x] += 1 # incremenet existing key by 1
    else: # if value is new
      unique_ue_rates[x] = 1 # create new key, increment by 1
  return unique_ue_rates # return the dictionary with unique rates count

print(count_unique_rates(unemployment_rates))
