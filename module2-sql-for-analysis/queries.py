''' Queries for sqlite to PostGreSQL pipeline'''


SELECT_ALL = '''
    SELECT * FROM {}
'''
# test table creation
create_test_table_statement = '''
    CREATE TABLE IF NOT EXISTS test_table (
        id SERIAL PRIMARY KEY,
        name varchar(20),
        age INT
);
'''
# test insert statement 
insert_statement = '''
    INSERT INTO test_table (name, age)
    VALUES 
    (
        'Steven',
        25
    ),
    (
        'Alfred',
        85
    );
'''
# rpg table creation
create_character_table = '''
    CREATE TABLE IF NOT EXISTS charactercreator_character (
        character_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        level INT,
        exp INT,
        hp INT,
        strength INT,
        intelligence INT,
        dexterity INT,
        wisdom INT
);
'''
# rpg insert statement 
INSERT_STATEMENT = '''
    INSERT INTO charactercreator_character(
        character_id,
        name,
        level,
        exp,
        hp,
        strength,
        intelligence,
        dexterity,
        wisdom
        ) VALUES {};
'''

# titanic table creation
create_titanic_table = '''
    CREATE TABLE IF NOT EXISTS titanic_table (
        Index_ID SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(100),
        Sex VARCHAR(10),
        Age INT,
        SiblingsSpouses INT, 
        ParentsChildren INT,
        Fare INT
    );
'''

# titanic insert statement
T_INSERT_STATEMENT = '''
    INSERT INTO titanic (
        Index_ID,
        Survived,
        Pclass,
        Name,
        Sex,
        Age,
        SiblingsSpouses INT, 
        ParentsChildren INT,
        Fare INT
    );
'''

