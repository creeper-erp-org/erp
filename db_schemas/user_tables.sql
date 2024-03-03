---- USER_DETAILS Table SQL statements START

-- a datatpe to note down different genders
CREATE TYPE gender_dtype AS ENUM ('male', 'female', 'other'); 


-- function to get current timestamp which is used in triggers for user_details table
CREATE  FUNCTION update_updated_at_user_details()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql'; 


-- trigger to update the updated_at value during row update for user_details table
CREATE TRIGGER update_user_details_updated_at
    BEFORE UPDATE
    ON
        user_details
    FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_user_details();


-- user user table that contains common informations for identification
create table user_details(
	user_id serial PRIMARY KEY,
	first_name varchar NOT NULL,
	middle_name varchar,
	last_name varchar,
	email_id varchar unique NOT NULL,
	gender gender_dtype NOT NULL,
	current_address varchar NOT NULL,
	permanent_address varchar NOT NULL,
	phone_number varchar NOT NULL,
	user_type varchar not null, 
	user_role varchar default null,
	additional_information json not null,
	created_at timestamp NOT null default now(),
	updated_at timestamp NOT null default now()
); 

---- USER_DETAILS Table SQL statements END



