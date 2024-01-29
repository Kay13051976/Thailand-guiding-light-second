# Main Features:
  - Each page has a navbar in the header and left section.

  ## Navbar 
  ### Header navbar:
  **Access to pages according to the user role**
  - The Navbar has two subsections :
1. User's section, which is visible to all users :
  - Logo, which redirects to the home page
     
  ![Logo](documentation/logo-in-header.png)

  - Header nav bar
  ![Header user image](documentation/header-user-image.png)


    - Home button, which redirects the user to the home page
    - The information button redirects the user to the Thailand tourism information website.
    - Logout button, which redirects the user to the logout
    - Access to page table

  | User Name | Sign in | Sign up | Comment |
  | ------- | --------- | ------- | ------- |
  | New user | Yes | Yes | Yes | - |
  | User | Yes | Yes | Yes | - |

2. Admin's section, which is visible for all admin:
    if the user is an admin 

   ![Header with admin site](documentation/header-with-admin-site.png)


    - Access to page table

  | User Name | Home | Information | Admin site | Logout | Comment |
  | --------- | ---- | ----------- | ---------- | ------ | ------- |
  | Admin | Yes | Yes | Yes | Yes | - |
  | New User | Yes | Yes | No | Yes | - |
  | User | Yes | Yes | No | Yes | - |

 
  ### Left navbar section:
  - Your Account button, which redirects the user to Your account page.
  - Your Connection button, which redirects the user to the connection page(Future Improvement).
  - Chat button, which redirects the user to the popover chat box(Future improvement).
  - Most Popular place button, which redirects the user to the most popular page.
  - Travel Agent, which redirects the user to the travel agent's external link.
  - Accommodations button, which redirects the user to the accommodation website page.
  - Transport button, which redirects the user to the transport booking website.
  - Thai Travel News, which redirects the user to the external link Thai Travel News.

**The simplistic design of the Navbar is based on the decision to make the use of the web app easy for all users.**

  - ![Left navbar section](documentation/left-nav.png)


    - Access to page table
      
| Page Name | Your Account | Most Popular Page| Your Connection | Chat | Most Popular | Travel Agent | Accommodations | Transport | Thai Travel News | Comment |
| --------- | ----------------- | ------------ | --------------- | ---- | ------------ | ------------ | -------------- | --------- | ---------------- | ------- |
| Admin      | Yes               | Yes       | Dummy link       | Dummy link   | Yes | Yes | Yes | Yes | Yes |  Future improvement  |
| New User      | Yes               | Yes       |         | Dummy link   | Yes | Yes | Yes | Yes | Yes |  Future improvement |
| User      | Yes               | Yes       |         | Dummy link   | Yes | Yes | Yes | Yes | Yes |  Future improvement |


## Home page :
![Admin home page](documentation/admin-home-page.png)
![User home page](documentation/user-home-page.png)
![New user home page](documentation/new-user-home-page.png)
  ### Laptop home page has 
  - header navbar
  **header section has a logo in the top left corner. There is also an eye-catching image**
  ![Admin navbar in header](documentation/admin-navbar-in-header.png)

  - Left navbar section
  **The left section nav has a list of nav link buttons that are nice and clear with an icon on the front, which will navigate the user directly to what they need to do and connect.**
  ![Left navbar section](documentation/left-nav.png)
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
  **The mobile home page has a hamburger dropdown. It will show a navbar when you click on the hamburger icon and in the dropdown menu, you will have an admin site nav to navigate to the Django panel for admin**
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
  ![Log out form page](documentation/logout-page-image.png)

  - login page
  ![Sign in page](documentation/sign-in-page.png)
  
  - sign up page
  ![Sign up page](documentation/sign-up-page.png)

