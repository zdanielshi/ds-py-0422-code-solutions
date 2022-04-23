trail_mix = {
    'm&m',
    'peanuts',
    'raisins'
  }

print(trail_mix)

# Accessing set items
## Cashews in trail_mix?
print('cashews' in trail_mix)

## Peanuts in trail mix?
print('peanuts' in trail_mix)

# Adding set items
## adding pretzels
trail_mix.add('pretzels')

## adding peanuts, banana chips, bits of jerky
more_stuff = {'peanuts', 'chips', 'bits of jerkey'}
trail_mix.update(more_stuff)

print(trail_mix)

# Removing set items
## remove m&ms
trail_mix.remove('m&m')

## discard raisins
trail_mix.discard('raisins')

print(trail_mix)

# Unions, intersections, differences
nuts = {'peanuts', 'cashews', 'almonds', 'walnuts', 'pecans'}

## set of all things are are nuts, trail mix, or both
everything = trail_mix.union(nuts)
print(everything)

## set of all nuts in trail mix
nuts_in_trail_mix = nuts.intersection(trail_mix)
print(nuts_in_trail_mix)

## set of all trail mix that are not nuts
non_nut_trail_mix = trail_mix.difference(nuts)
print(non_nut_trail_mix)

## set of all nuts that are not in trail mix
non_trail_mix_nuts = nuts.difference(trail_mix)
print(non_trail_mix_nuts)
