# Main Features:
  - Each page has a navbar in the header and left section.
## Home page :
- Admin Home Page
![Admin home page](documentation/home-page-image1.png)

- User Home Page
![User home page](documentation/user-home-page.png)

- New User Home Page
![New user home page](documentation/new-user-home-page.png)
  ## Navbar 
  ### Header navbar:
  **Access to pages according to the user role**
  - The Navbar has two subsections :
1. User's section, which is visible to all users :
  - Logo, which redirects to the home page
     
  ![Logo](documentation/logo-in-header.png)

  - Header nav bar for user and admin
  ![Header user image](documentation/header-laptop-image.png)


    - Home button: which redirects the user to the home page
    - The information button: redirects the user to the Thailand tourism information website.
    - Search Bar: This interface element is designed to help users quickly and efficiently find specific information or items. It enhances the user experience by enabling easy access to relevant content (planned for future enhancement).
    - Welcome Message & Username Display: Displays a welcome message and the user's name to confirm that they are on their account page, enhancing the user experience.

  ### Left navbar section:
 
  **The left section nav has a list of nav link buttons that are nice and clear with an icon on the front, which will navigate the user directly to what they need to do and connect.**

**The navbar's simplistic design is intentionally crafted to ensure ease of use for all users of the web app.**

### Admin's Left Navbar: This section is visible to all users identified as admins. This section includes two navigation links.


![Header with admin site](documentation/admin-left-section-image.png)
- Admin Site Navigation Link: Directs to the admin panel, allowing for the creation, reading, updating, and deletion (CRUD) of information from both admin and user accounts.

![Administration panel image](documentation/administration-panel-image.png)

- Comment Management Navigation Link: Directs to the admin comment management page, where admins can efficiently create, read, update, and delete comments using a user-friendly interface.

![Comment management page image](documentation/admin-comment-management-page.png)

  - The comment management page has a notifications function.

![Comment management page notification image](documentation/comment-management-page-notification.png)

   - The comment management page has an All comments detail table make it easy to manage.
![Comment management table image ](documentation/comment-management-table.png)

**Access to page table**

| Welcone:User Name | Admin Site | Comment Management |
  | ------- | --------- | ------- |
  | Admin | Yes | Yes | Yes |
  | New user | No | No | No | 
  | User | Yes | No| No| 

  ### User's Left navbar section:

   ![Use left navbar section](documentation/left-navbar-section.png)

  - Your Profile Account button, which redirects the user to Your account page.

  ![User profile page image](documentation/user-profile-page.png)
  - Your Connection button, which redirects the user to the connection page.
  - Chat button, which redirects the user to the popover chat box(Future improvement).
  - Most Popular place button, which redirects the user to the most popular page.
   ![Most popular page1 image](documentation/most-popular-page1.png)
   ![Most popular page2 image](documentation/most-popular-page2.png)
  - Travel Agent, which redirects the user to the travel agent's external link.
  - Accommodations button, which redirects the user to the accommodation website page.
  - Transport button, which redirects the user to the transport booking website.
  - Thai Travel News, which redirects the user to the external link Thai Travel News.
  - Logout button, which redirects the user to logout/signup page.
  ![Sign out page image](documentation/sign-out-page1.png)
    - when the user click sign out which redirects the user to the sing in and sign up page.
  ![Sign in and sign up page image](documentation/sign-in-and-sign-up-page.png)


    **Access to page table**

  | user | Welcome:User Name | Home | Information | Admin site | Comment Management | Profile | Your Connection | Chat | Most Popular Place | Travel Agent | Accommodations | Transport | Thai Travel News | Logout |
  | --------- | ---- | ------- | ----- | ------ | ------- | -------- | ------- | ------ | ----- | ----- | ---- | ---- | ------ | -----|
  | Admin | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
  | New User | No | Yes | Yes | No | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
  | User | Yes | Yes | Yes | No | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

## Main Section: 
Comprises the Account Owner's Post Creation Section and the Post Display Section.

  - Account Owner's Post Creation Section: includes a profile image of the account owner, an input field for entering the post header, and a 'Choose File' option for uploading images or files. Below these, there is a 'Post' button that submits the content to the Post Display Section.

  ![User account post section image](documentation/user-account-post-section.png)


- Display post section

  - The Display Post Section: has a user image in a circle shape, and the name, three dots vertical iacon on the same line, underneath has a carousel to display multiple images.

  ![Display post section image](documentation/display-post-section-image.png)

    - Three Dots Vertical Icon: Features a hover function that displays a navigation menu, allowing the post owner to easily edit or delete their posts.

     ![Three dots vertical icon hover image](documentation/three-dots-vertical-hover.png)

     - Edit Post; redirect user to the edit post page so the post owner can delete individual or image and add new image and edit header to update the post.

       ![Edit post page image](documentation/edit-post-page.png)
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

  - Comment CRUD page
  ![Mobile comment crud image1](documentation/mobile-comment-crud-image1.png)
  ![mobile comment crud image2](documentation/mobile-comment-crud-image2.png)


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

