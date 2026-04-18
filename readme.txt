I have attached the requirements file.
use the commands,
1. python -m venv venv_name
2. pip install -r requirements.txt

I have attached the mysql dump file to create the database nevertheless, paste it into MySQL workbench.
the following command in a terminal will work successfully in copying my structure of database,
mysql -u root -p entropyzero < your_dump_file.sql
NOTE : Create a database named entropyzero first before pasting the given command in a terminal of choice, 
create database entropyzero;
use entropyzero;

Sorry for inconvenience and mismatch of working environments.