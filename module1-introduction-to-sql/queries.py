''' SQL queries for the unit 3 module 1 projet'''


#  How many total Characters are there?
TOTAL_CHARACTERS = '''
SELECT COUNT(character_id)
FROM charactercreator_character
'''
# How many of each specific subclass?
TOTAL_SUBCLASS = '''
SELECT SUM (tbl.count)
FROM
SELECT COUNT(*) AS count FROM charactercreator_necromancer
UNION ALL
SELECT COUNT(*) AS count FROM armoy_weapon
'''
# How many total Items?
TOTAL_ITEMS: 

# How many of the Items are weapons?
WEAPONS: 

# How many of the items are not weapons?
NON_WEAPONS: 

# How many Items does each character have? (Return first 20 rows)
CHARACTER_ITEMS: 

# How many Weapons does each character have? (Return first 20 rows)
CHARACTER_WEAPONS: 

# On average, how many Items does each Character have?
AVG_CHARACTER_ITEMS:

# On average, how many Weapons does each character have?
AVG_CHARACTER_WEAPONS: 
