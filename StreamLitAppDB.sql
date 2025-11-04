create table FRUIT_OPTIONS (
    FRUIT_ID number,
    FRUIT_NAME varchar(25) -- supported types: https://docs.snowflake.com/en/sql-reference/intro-summary-data-types
) -- comment = '<comment>';

create file format smoothies.public.two_headerrow_pct_delim 
type = 'CSV'
skip_header = 2
field_delimiter = '%'
trim_space = TRUE;


CREATE FILE FORMAT smoothies.public.two_headerrow_pct_delim 
  TYPE = CSV
  SKIP_HEADER = 2
  FIELD_DELIMITER = '%'
  TRIM_SPACE = TRUE;