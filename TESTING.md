# TESTING
## Manual Testing

Testing was done throughout site development, for each before it was feature before it was merged into the master file
Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different devices and browser to ensure issues were caught and where possible fixed during development.
| Page | User Actions | Expected Results | Y/N | Comments |
| ---- | ------------ | ---------------- | --- | -------- |
| Sign in | | | |          |
| 1      | Click on Sign in button | Redirection to Sign in page | Y   | |
| 2      |  Click on Sign up button | Redirection to Sign Up page | Y   | |
| Log out| Click on log out button | Redirection to Log Out page | Y   | |
| Header navbar |  | |    | |
| 1. Home     | Click on Home button | Redirection to Home page | Y   | |
| 2 Information     | Click on Information button | Redirection to information website | Y   | |
| 3. Admin site     | Click on Admin site button | Redirection to Sjango admin site | Y   | |
| 4. Comment CRUD     | Click on Comment CRUD button | Redirection to comment CRUD page | Y   | |
| 5. Log Out     | Click on Log Out button | Redirection to Log Out page | Y   | |
| Your Account | Click on Account button | Redirection to Your account page | Y   | |
| Your Connection | Click on Your Connection button | Redirection to home page | This is only dummy link nav and will be future improvement  | |
| Chat  | Click on Chat button | Redirection to Home page | This is only dummy link nav and will be future improvement  | N |
| Most Popular Place    | Click on Most Popular Place button | Redirection to most popular place page | N   | |
| Transport   | Click on Transport button | Redirection to Transport booking website  | Y   | |
| Thai Travel News   | Click on Thai Travel News button | Redirection to Thai travel news website | Y   | |

## Testing
### Chrome
![Test home page new user](documentation/test-home-page-chrome.png)
![Tst home page user chrome](documentation/test-home-page-admin-chrome.png)
### Firefox
![Test home page user fierfox](documentation/test-home-page-user-firefox.png)
![Test home page admin](documentation/test-chrome.png)
### Brave
![Test home page brave](documentation/test-brave-home-page.png)
![Test home page brave](documentation/test-brabe-home-page.png)
## Python validation Testing
pep8ci Python Linter
![Admin pep8 test](documentation/admin-pep8.png)
![Apps pep8 test](documentation/app-pep8.png)
![Forms pep8 test](documentation/forms-pep8.png)
![Model pep8 test](documentation/model.pep8.png)
![Tests pep8 test](documentation/test-pep8.png)
![URL home app pep8 test](documentation/urls-home-app-pep8.png)
![Views pep8 test](documentation/views-pep8.png)
![asgi pep8](documentation/asgi-pep8.png)
![urls social media project pep8](documentation/url-social-media-project-pep8.png)
![wsgi pep8](documentation/wsgi-pep8.png)
![settings pep8](documentation/setting-pep8.png)
## HTML validation
- Home page
![Home page html validation](documentation/home-page-html-validation.png)

- Your account page
![Your account page html validation](documentation/your-account-page-html-validation.png)

- Most popular page

 **The error appear because of Django form variable**
![Most popular page html validation](documentation/most-popular-page-html-validation.png)

![Comment CRUD page html validation1](documentation/comment-crud-page-html-validation1.png)
![ Comment CRUD page html validation2](documentation/comment-crud-page-html-validation2.png)
![Comment CRUD page html validation3](documentation/comment-crud-page-html-validation3.png)
![Comment CRUD page html validation4](documentation/comment-crud-page-html-validation4.png)
![]()



## Lighthouse Report
### Lighthouse new user page report
![Test lighthouse new user](documentation/lighthouse-tes-new-usert.png)
### Lighthouse user page report

![Test lighthouse user](documentation/lighthouse-test-user.png)
### Lighthouse admin page report
- User page
![Test lighthouse user](documentation/lighthouse-test-admin.png)
- Your account page
![Test lighthouse your account page](documentation/lighthouse-test-your-account-page.png)
- Most popular page
![Test lighthouse most popular place page](documentation/lighthouse-test-your-account-page.png)
- Sign up page
![Test lighthouse sign up page](documentation/lighthouse-test-signup-page.png)
- Comment CRUD page 
![Comment CRUD lighthouse analyze](documentation/comment-crud-lighthouse-analyze.png)
## Solved bugs
- Removed stray end tag in base.html
![Bug fixed in base.html1](documentation/stray-end-tag-bug-fixed1.jpeg)
![Bug fixed in base.html2](documentation/stray-end-tag-bug-fixed2.jpeg)
## Future Improvement
- Add a function to edit the post for the user.
- Add reply comments in post comment sections.
- Create your connection app and manage the connection function.
