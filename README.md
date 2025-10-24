# LittleLemon
Coursera

#Does the application connect the backend to a MySQL database?

mysql -u -p
'USER': 'admindjango',   
'PASSWORD': 'employee@123!',

mysql -u admindjango -p
PASSWORD': 'employee@123!'



#Are the menu and table booking APIs implemented?
http://127.0.0.1:8000/restaurant/menu/
http://127.0.0.1:8000/restaurant/menu/1
http://127.0.0.1:8000/restaurant/booking/tables/



#Is the application set up with user registration and authentication?
http://127.0.0.1:8000/auth/users/

created user
testuser
employee@123!

http://127.0.0.1:8000/auth/token/login/
Token =>e29ded21a30e633c0fe1064af1e5197e6fcc4670


#Does the application contain unit tests?
DASE_Dir/tests
(venv) PS D:\Business\Coursera\capstone\LittleLemon\BASE_DIR> python manage.py test


#Can the API be tested with the Insomnia REST client?
GET
http://127.0.0.1:8000/restaurant/menu/
http://127.0.0.1:8000/restaurant/menu/1
http://127.0.0.1:8000/restaurant/booking/tables/

USER: testuser
Password: employee@123!
Token: e29ded21a30e633c0fe1064af1e5197e6fcc4670



