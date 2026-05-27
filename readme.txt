===========================================================================================================

SETTING UP VIRTUAL ENVIRONMENT :

I have attached the requirements file.
use the commands,

Windows :
python -m venv Sorter_venv
Sorter_venv\Scripts\activate

MacOS : 
python3 -m venv Sorter_venv
source Sorter_venv/bin/activate

============================================================================================================

SETTING UP SQL :

I have attached the mysql dump file to create the database nevertheless, paste it into MySQL work bench.
the following command in a terminal will work successfully in copying my structure of database,

mysql -u root -p entropyzero < your_dump_file.sql

NOTE : Create a database named entropyzero first before pasting the given command in a terminal of choice, 
create database entropyzero;
use entropyzero;

=============================================================================================================

PULL THE CODE :

install git on your computer
in the git bash,
git clone https://github.com/sagnickkarak-create/EntropyZero

make sure that cwd is correct

==============================================================================================================

THANK YOU

==============================================================================================================

