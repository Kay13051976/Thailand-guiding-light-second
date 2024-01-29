# Main Features:
  - Each page has a navbar 

  Navbar: 
  **Access to pages according to the user role**
  | Page Name | Home | Information | Admin site | Logout |
  | --------- | ---- | ----------- | ---------- | ------ |
  | Admin | Yes | Yes | Yes | Yes |
  | User | Yes | Yes | No | Yes |

  
- The navbar has two subsections:
     1. User's section, which is visible is visible for all users:
        - if the user is an admin 
        ![Header with admin site](documentation/header-with-admin-site.png)
        - if the user is not an admin
        ![]()

     2. Logo, which redirects to the home page;
      ![Logo](documentation/logo-in-header.png)
      - home button, which redirects the user to the store page
      - information button, which redirects the user to the external link website "tourismthailand.org/home
      - admin Site button, which redirects admin to Django admin dashboard.
      - sign out, which redirects the user to logout 
      3. nav section 
      - your account, which redirects the user to the user account form and manages the user account
      
| Page Name | Most Popular Page | Your Account | Your Connnection | Chat | Most Popular | Travel Agent | Accommodations | Transport | Thai Travel News
| --------- | ----------------- | --------- | ---------- | ----------- |
| Home      | Yes               | Yes       | Yes        | Yes (Only for admin)       |
| Login     | No              | No       | No        | No         | 
| Sign up   | No               | No       | No        | No         |   
| Most popular place      | Yes               | Yes       | Yes        | Yes         | 
| Your Account      | Yes               | Yes       | Yes        | No (Only for admin)        | 


## Main Features :
  - Each page has a navbar in the header and left section.
  ### Navbar : 
  - The Navbar has two subsections :
     1. User's section, which is visible to all users :
       **if the user is logged in, the Navbar has the following feature:**
         - [User navbar in header](documentation/user-navbar-in-header.png)
            - Logo, which redirects to the home page
            - Home button, which redirects the user to the home page
            - The information button redirects the user to the Thailand tourism information website.
            - logout button, which redirects the user to the logout
            - logout form, which redirects the user to the login form and signup link to redirect to the signup form.
       ![]()

      2. Admin's section, which is only visible for admin :
       ![Admin navbar in header](documentation/admin-navbar-in-header.png)
            will have the same Navbar as the user but the admin site button will appear
            - Admin Site button, which redirects to the Django admin page. 

      3. Left Navbar section 
        - ![Left navbar section](documentation/left-navbar-section.png)
          - Your Account button, which redirects the user to the Your accont page
          - Your Connection button, which redirects the user to the connection page
          - Chat button, which redirects the user to the popover chat box
          - Most Popular place button, which redirects the user to the most popular page
          - Accommodations button, which redirects the user to the accommodation website page
          - Transport button, which redirects the user to the transport booking website
**The simplistic design of the Navbar is based on the decision to make the use of the web app easy for all users.

**Navbar looks as follows on the mobile devices**
![Mobile hamburger navbar](documentation/mobile-hamburger-navbar.png)

## Home page :
![Admin home page](documentation/admin-home-page.png)
![User home page](documentation/user-home-page.png)
![New user home page](documentation/new-user-home-page.png)
  ### Laptop home page has 
   - header navbar
  ![Admin navbar in header](documentation/admin-navbar-in-header.png)
  header section has a logo in the top left corner. There is also an eye-catching image 

   - Left section navbar
  ![Left navbar section](documentation/left-section-navbar.png)
     - The left section nav has a list of nav link buttons that are nice and clear with an icon on the front, which will navigate the user directly to what they need to do and connect. 
   - Left section advert
  ![Left section advert](documentation/left-section-advert.png)

   - Create a post section
  ![Create post section](images/create-post-section.png)
     - Create a post section that has a simple form to fill and a small default image to show if the user has not managed to load, and it has a big and bright submit post button.

   - Display post section
  ![Display post section](documentation/display-post-section.png)
     - The display post section has a user image in a circle shape, and the name on the same line underneath has a carousel to display multiple images.
  
### Mobile home page
  The mobile home page has a hamburger dropdown. It will show a navbar when you click on the hamburger icon and in the dropdown menu, you will have an admin site nav to navigate to the Django panel for admin 
    - mobile home page for new user
  ![Mobile home page new user](documentation/mobile-home-page-new-user.png)
  ![Mobile home page new user dropdown](documentation/mobile-home-page-new-user-dropdown.png)

    - mobile home page for user
  ![Mobile home page user](documentation/mobile-home-page-user.png)
  ![Mobile home page user dropdown](documentation/mobile-home-page-user-dropdown.png)

    - Mobile home page for admin
  ![Mobile home page admin](documentation/mobile-home-page-hamburger.png)
  ![Mobile home page hamburger dropdown](documentation/mobile-home-page-hamburger-dropdown.png)

 ## Your account page
  - This page has the primary data; this page allows the user to add or edit profile image, account name, full name, email address, phone number 
    - It has an avatar as a default if the user don't want to display their image
      - Your account's new user
      ![Your account page new user](documentation/your-account-page-new-user.png)
      - your account user
      ![Your account page user](documentation/your-account-page-user.png)
      - your account admin
      ![Your account page admin](documentation/your-account-page-admin.png)
### Your account page mobile
 - This page has a hamburger dropdown including four navigate nav links and the primary data in this page allows the user to add or edit profile image, account name, full name, email address, phone number 
    - It has an avatar as a default if the use doesn't want to display their image
      - Your account's new user
      ![Mobile your account page new user](documentation/mobile-your-account-page-new-user.png)
      - your account user
      ![Mobile your account page user](documentation/mobile-your-account-page-user.png)
      - your account admin
      ![Mobile your account page admin](documentation/mobile-your-account-page-admin.png)

## Most popular place
  - This page has the most popular places in Thailand that will always be on the top list to visit.
      - most popular page for users and new users
  ![Most popular place for user and new user](documentation/most-popular-page-user-and-new-user.png)
       - most popular page for admin
  ![Most popular place for admin](documentation/most-popular-page-admin.png)


  ### Most popular place mobile
   - This page has the most popular place in Thailand that will always in the top list for tourists to visit, and a hamburger dropdown to hide/show the nav link
    ![Mobile most popular page](documentation/mobile-most-popular-page-.png)
    ![Mobile most popular page hamburger dropdown](documentation/mobile-most-popular-page-hamburger-dropdown.png)

    ## Allauth and Access pages :

  - Logout page
  ![Log out form page](documentation/log-out-form.png)

  - login page
  ![Sign in page](documentation/sign-in-page.png)
  - sign up page
  ![Sign up page](documentation/sign-up-page.png)

