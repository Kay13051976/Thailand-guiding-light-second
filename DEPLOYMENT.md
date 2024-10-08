# Deployment setup
 - The app was deployed to [HEROKU](https://id.heroku.com/login)
 - The database was deployed to [ElephantSQL](https://www.elephantsql.com/)
  - The static file and images was deployed to cloundinary [Cloudinary](https://cloudinary.com/)
 - The app can be reached by the [Link to Thailand Guiding Light](https://thailand-guiding-light-2fb0b0e33db8.herokuapp.com/)

## Local deployment
1. Clone the repository.
   - git clone`https://github.com/Kay13051976/Thailand-guiding-light-second.git`
2. Go to the Thailand-guiding-light-second directory.
     - `cd Thailand-guiding-light-second`
3. Create a virtual environment.
     - `python3 -m venv venv`
     - `source venv/bin/activate`
- 4. install all dependencies.
     - `pip3 install -r requirements.txt`
5. Create a env.py file
     - `touch env.py`
6. Add the following lines env.py
     - `import os`
     - `os.environ.setdefault["SECRET_KEY] = your secret key.`
     - `os.environ.setdefault["DEBUG"] = "True" or "False" depending on whether you are in development or production.`
     - `os.environ.default["ALLOW_HOSTS] = your domain name.`
     - `os.environ.default["DATABASE_URL"] = your database url.`
     - `os.environ.default[CLOUDINARY_CLOUD_NAME] = your cloudinary cloud name.`
     - `os.environ.default["CLOUDINARY_API_KEY] = your cloudinary api key`
     - `os.environ.default["CLOUDINARY_API_SECRET] = your cloudinary api secret`
7. Create and migrate the database.
     - `python3 manage.py makemigrations`
     - `python3 manage.py migrate`
     - `After migration, you will need to create a superuser.`
8. Create roles as following:
     - `python3 manage.py createsuperuser`
9. Create roles as following:

- For example
`Role.objects.create(name='Customer')`
`Role.objects.create(name='Manager')`
`Role.objects.create(name='Admin')`

10. Set the role for the superuser with the role field with id 3.

  `superuser.profile.role_id = 3`    
  `superuser.save()`

11. Go to Profiles and uncomment the default role. Make new migrations and migrate.
     - python3 manage.py makemigrations
     - python3 manage.py migrate

After the following steps, you will ensure that the app is working correctly, and any other user registered in your app will only have access as a new user. The rest of the roles will be controlled by the admin

12. Run the server.
     - python3 manage.py runserver 
     **It will redirect you to the home. Click on logout and login or signup.**
- click on register or login 
        ![Home page register login image](documentation/home-page-register-login.png)

- click on Sign in or sign up
        ![Sign in page](documentation/Signin-in-image-deployment.png)

13. Access the website by the link provided in terminal. Add /admin/ at the end of the link to access the admin panel.

## The app was initially deployed to Heroku
### Heroku Deployment

1. Create a Heroku account if you don't already have one.
2. Create a new app on Heroku.
     - Go to the [Heroku](https://id.heroku.com/login)
     - Click on the "New" button.
     - Click on the "Create new app" button.
     - Choose a name for your app.
     - Choose a region.
     - Click on the "Create app" button.
3. In your app go to the "Resources" tab.
     - Add a Heroku Postgres database.
4. In your app, go to the "Setting" tab, press "Reveal Config Vars", and the following config vars if they are not already set:
     - ALLOWED_HOSTS = your heroku domain name.
     - CLOUDINARY_CLOUD_NAME = the cloud name you used when creating your cloudinary account.
     - CLOUDINARY_API_KEY = the api key you got when crated your cloudinary account.
     - CLOUDINARY_API_SECRET = the api secret you got when created your cloudinary account.
     - DATABASE_URL = the url of your heroku postgrate database.
     - EMAIL_HOST_USER = the email address you going to use to send emails.
     - DEBUG = True during development, False during production.
     - DISABLE_COLLECTIONSTATIC = 1 during development. Remove this when deploying to production.
     
5. In your app go to the "Deploy" tab.
    - If it's already possible, connect your Heroku account to your GitHub account and then click on the "Deploy" button.
    - If not, you need to copy the Heroku CLI command to connect your Heroku app and your local repository.
      - `heroku git:remote -a <your-heroku-app-name`ุ
6. Go to your local repository.
7. Login to your Heroku account in your terminal and connect your local repository to your heroku app.
     - `heroku login -i` - Enter all your Heroku credentials it will ask for.
     - Paste the command you copied from step 5 into your terminal.
8. Create Procfile.
   This project uses Keroku which is require a Procfile that specifies the commands that are executed by the app on startup. You can use a Procfile to declare a variety of process types, including: Your app's web server. Multiple types 
     - `web: gunicorn social_media_project.wsgi`
9. Create requirements.txt This can be done by running the following command.
     - `pip3 freeze > requirement.txt`
10. Add your commit to Heroku.
11. Push your changes to Heroku.
     - `git push heroku master` or 
     - `git push heroku main`
12. Check your app's logs in heroku dashboard and ensure everything is working.
13. After the development is done, you can change the `Debug` config vars to `False` and remove the `DISABLE_COLLECTSTATIC` config var from the config vars on heroku.
To get Cloudinary cloud name, API key, and API secret:
    1. go to the [Cloudinary website](https://cloudinary.com/users)
    2. Log in your account or sign up if you don't have an account.
    3. Go to the Cloudinary dashboard.
    4. At the top of the page, you will see your cloud name, API key, and API secret.
    5. To reveal API secret, hover over the API key container and click on the button that look like and eye.
    6. Copy these values and paste them into the config vars on Heroku and into your `env.py` file.
### Create Database on ElephantSQL
1. Go to [ElephantSQL](https://www.elephantsql.com/) and create a new account.
2. Create a new instance of the database.
![Crate new instance](documentation/elephant-sql-create-new-instance.png)
3. Select a name for yor database and select the free plan.
![Select plan and name](documentation/elephant-sql-select-plan-and-name.png)
4. Click "Select Region"
![Select region](documentation/elephant-sql-select-region.png)
5. Select a region close to you.
![Select region close to you](documentation/elephant-sql-select-close-region.png)
6. Click "Review"
![Click review](documentation/elephant-sqp-review.png)
7. Click "create instance"
![Click create instance](documentation/elephant-sql-create-instance.png)
8. Click on the name of your database to open the dashboard.
![Instance name list](documentation/elephant-sql-instance-list.png)
9. You will see the dashboard of your database. You will need the URL of your database to connect it to your Django project.
![Instance dashboard](documentation/elephant-sql-instance-dashboard.png)

## Create a new app on Heroku
 ### sign up with Heroku then log into your account and go to the Dashboard.
1. Click "New"
![Click new button image](documentation/heroku-new-button.png)
2. Click "Create new app"
![Heroku create new app image](documentation/heroku-create-new-app.png)
3. Give your app a name and select the region closest to you. When you're done, click "Create app" to confirm.
![Heroku create app button image](documentation/heroku-create-app-button.png)
**Heroku app names must be unique. If yours isn't, Heroku will give you a warning that looks like the image below**
4. Navigate to your Heroku dashboard and select the app you have just created.
![Heroku app name list image](documentation/heroku-app-name-list.png)
5. On your app dashboard click on the Deploy tab.
![Heroku app dashboard deploy tab](documentation/heroku-app-dashboard.png)
6. In the Deployment method section enable GitHub integration by clicking on Connect to GitHub
**if you have not deployed a project from GitHub before then, you will be asked to authenticate with GitHub.**
![Heroku connect GitHub section](documentation/hetoku-connect-github-section.png)
7. Start typing your project repo name into the search box and click Search. A list of repositories from your GitHub account should appear. Click on the GitHub repo you want to deploy from.
![Heroku search repo to connect image](documentation/heroku-serch-repo-to-connect.png)
8. Scroll to the bottom of the page and click Deploy Branch to start a manual deployment of the main branch.
![Heroku deploy branch button image](documentation/heroku-deploy-branch-button.png)
9. Heroku will start to deploy the current state of a branch to this app.
![Heroku view build log image](documentation/heroku-view-build-log-log.png)
You can click on "View build log" to view the code. When loading completed click on open app on top right corner.
![Heroku view build log detail image](documentation/heroku-view-build-log-detail.png)
Click on Details
![Heroku dangerous site warning image](documentation/heroku-dangerous-site-warning1.png)
Click on "this unsafe site" the sign in and sign up page of the website will appear
![Heroku dangerous site this unsafe site image](documentation/heroku-dangerous-site-this-unsafe-site1.png)
sign up to create account or sign in to your account.
![Heroku home page view](documentation/heroku-home-page-view.png)
