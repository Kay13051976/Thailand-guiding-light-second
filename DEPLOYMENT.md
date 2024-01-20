# Deployment and Payment setup
 - The app was deployed to [HEROKU](https://id.heroku.com/login)
 - The database was deployed to [ElephantSQL](https://www.elephantsql.com/)
 - The app can be reached by the [Link](https://thailand-guiding-light-2fb0b0e33db8.herokuapp.com/)

## Local deployment
1. Clone the repository.
   - git clone`https://github.com/Kay13051976/Thailand-guiding-light-second.git`
  2. Go to the Thailand-guiding-light-second directory.
     - `cd Thailand-guiding-light-second`
 3. Create a virtual environment.
     - `python3 -m venv venv`
     - `venv/bin/activate`
4. install all dependencies.
     - `pip3 install -r requirements.txt`
5. Create a env.py file
     - `touch env.py`
6. Add th following lines env.py
     - `import os`
     - `os.environ["SECRET_KEY] = your secret key.`
     - `os.environ["DEBUG"] = "True" or "False" depending on whether you are in development or production.`
     - `os.environ["ALLOW_HOSTS] = your domain name.`
     - `os.environ["DATABASE_URL"] = your database url.`
     - `os.environ[CLOUDINARY_CLOUD_NAME] = your cloudinary cloud name.`
     - `os.environ["CLOUDINARY_API_KEY] = your cloudinary api key`
     - `os.environ["CLOUDINARY_API_SECRET] = your cloudinary api secret`
7. Create and migrate the database.