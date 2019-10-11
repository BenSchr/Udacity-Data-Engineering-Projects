# CREATE TABLES

############# Airbnb ##################

host_table_create=("""CREATE TABLE IF NOT EXISTS host(
    host_id INT Primary Key,
    host_name VARCHAR
);""")

location_table_create=("""CREATE TABLE IF NOT EXISTS location(
    location_id SERIAL Primary Key,
    neighbourhood_group VARCHAR,
    neighbourhood VARCHAR,
    long VARCHAR NOT NULL,
    lat VARCHAR NOT NULL
);""")

listing_table_create=("""CREATE TABLE IF NOT EXISTS listing(
    listing_id INT Primary Key,
    name VARCHAR,
    host_id INT NOT NULL REFERENCES host(host_id),
    location_id INT NOT NULL REFERENCES location(location_id),
    room_type VARCHAR,
    price INT,
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE,
    reviews_per_month FLOAT,
    calculated_host_listings_count INT,
    availability_365 INT
);""")

#######################################

############## Time ###################

date_table_create=("""CREATE TABLE IF NOT EXISTS date(
    date_id SERIAL PRIMARY KEY,
    year INT NOT NULL,
    month INT NOT NULL,
    day INT NOT NULL
);""")

#######################################


############# Weather #################
weather_table_create=("""CREATE TABLE IF NOT EXISTS weather(
    date_id INT Primary Key REFERENCES date(date_id),
    max_temp INT NOT NULL,
    min_temp INT NOT NULL,
    avg_temp INT NOT NULL,
    precipitation FLOAT NOT NULL,
    snowfall FLOAT NOT NULL,
    snowdepth FLOAT NOT NULL
);""")
#######################################


############# Jurisdiction ############
jurisdiction_table_create=("""CREATE TABLE IF NOT EXISTS jurisdiction(
    jurisdiction_id INT PRIMARY KEY, 
    jdesc VARCHAR NOT NULL
);""")
#######################################

############# Crime-Types ############
crime_type_table_create=("""CREATE TABLE IF NOT EXISTS crime_type(
    ctype_id SERIAL PRIMARY KEY,
    ky_cd INT NOT NULL,
    ofns_desc VARCHAR NULL,
    pd_cd INT NULL,
    pd_desc VARCHAR NULL
);""")
#######################################



############# Crime ###################
crime_table_create=("""CREATE TABLE IF NOT EXISTS crime(
    crime_id INT Primary Key,
    precinct INT NOT NULL,
    location_id INT NULL REFERENCES location(location_id),
    start_date_id INT NOT NULL REFERENCES date(date_id),
    end_date_id INT NULL REFERENCES date(date_id),
    completed VARCHAR NOT NULL,
    hadevelopt VARCHAR NULL,
    housing_psa INT NULL,
    jurisdiction_id INT NULL REFERENCES jurisdiction(jurisdiction_id),
    law_cat_cd VARCHAR NOT NULL,
    loc_of_occur_desc VARCHAR NULL,
    parks_nm VARCHAR NULL,
    patrol_boro VARCHAR NULL,
    ctype_id INT NULL REFERENCES crime_type(ctype_id),
    prem_typ_desc VARCHAR NULL,
    rpt_date_id INT NOT NULL REFERENCES date(date_id),
    station_name VARCHAR NULL,
    susp_age_group VARCHAR NULL,
    susp_race VARCHAR NULL,
    susp_sex VARCHAR NULL,
    vic_age_group VARCHAR NULL,
    vic_race VARCHAR NULL,
    vic_sex VARCHAR NULL,
    transit_district VARCHAR NULL     
);""")
#######################################




# Insert

date_table_insert = ("""INSERT INTO date(
year,
month,
day)
VALUES (%s,%s,%s);
""")




# MISC

getStruct=("""                            
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = %s;
""")