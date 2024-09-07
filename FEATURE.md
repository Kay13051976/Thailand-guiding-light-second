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
 
 Which is visible to all users :

  ![Header nav with login logout image](documentation/header-nav-with-login-logout.png)

  ![Header user image](documentation/header-laptop-image.png)

  - Logo, which redirects to the home page
     
  ![Logo](documentation/logo-in-header.png)

  - Home button: which redirects the user to the home page
  - The information button: redirects the user to the Thailand tourism information website.
  - Search Bar: This interface element is designed to help users quickly and efficiently find specific information or items. It enhances the user experience by enabling easy access to relevant content (planned for future enhancement).
  - Register button: which redirects the user to the rigister page.
  - Login button: which redirects the user to the login page.
  - Welcome Message & Username Display: Features a welcome message alongside the user's name, confirming their presence on their account page. The username also serves as a link that redirects to the account owner's profile page, enhancing user experience.

  ### Left navbar section:

   **Display Section Based on User Role**
 
  **The left section nav has a list of nav link buttons that are nice and clear with an icon on the front, which will navigate the user directly to what they need to do and connect.**

### Admin's Left Navbar: This section is visible to all users identified as admins. This section includes two navigation links.

![Header with admin site](documentation/admin-left-section-image.png)
- Admin Site: Directs to the admin panel, allowing for the creation, reading, updating, and deletion (CRUD) of information from both admin and user accounts.

![Administration panel image](documentation/administration-panel-image.png)

- Comment Management: Directs to the admin comment management page, where admins can efficiently create, read, update, and delete comments using a user-friendly interface.

![Comment management page image](documentation/admin-comment-management-page.png)

  - The comment management page has a notifications function to confirm task completion for the admin.

![Comment management page notification image](documentation/comment-management-page-notification.png)

   - The comment management page has an All comments detail table make it easy to manage.

![Comment management table image ](documentation/comment-management-table.png)


**Access to page table**

  | User | Welcone:User Name | Admin Site | Comment Management |
  | ------- | --------- | ------- | ----- |
  | Admin | Yes | Yes | Yes | Yes |
  | New user | No | No | No | No |
  | Regular User | Yes | No| No| No |

  ### User's Left navbar section:
  
Visibility: This section is accessible to all users, including administrators

   ![User left navbar section](documentation/left-navbar-section.png)

  - Profile Account Button: Redirects users to their account page, where new users can upload their image and enter personal information. Existing users can update their image and information as needed.

  ![User profile page image](documentation/user-profile-page.png)
  ![New User profile page image](documentation/new-user-profile-page.png)

  - Your Connection Button: Redirects users to the Connections page, where the account owner can accept or cancel connection requests, or disconnect from existing connections.

  ![Your connection page image](documentation/your-connection-page.png)

  - Chat button, which redirects the user to the popover chat box(Future improvement).
  - Most Popular Places Button: Redirects users to the Most Popular Places page. Here, users can click links to connect with travel agents who support the website. Enhancements to this feature are planned for future improvement.

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


- Display post section: Features a circular user image alongside the user's name and a three-dot vertical icon at the top. Below, a carousel displays multiple images. Underneath the carousel, there are four icons: a heart, a comment bubble, a share symbol, and a connect icon. Users can interact with the post by clicking the heart to express liking the post, the comment bubble to leave their thoughts, the share symbol to copy the post link, and the connect icon to link up with the post owner.

  ![Display post section image](documentation/display-post-section-image.png)

  - Three Dots Vertical Icon: Features a hover function that displays a navigation menu, allowing the post owner to easily edit or delete their posts.

     ![Three dots vertical icon hover image](documentation/three-dots-vertical-hover.png)

    
    - Delete Post: This option allows the post owner to delete a post. Upon selecting 'Delete', a confirmation popup appears. If the user clicks 'Yes, Proceed', an alert confirming successful deletion will display. After clicking 'OK' on the alert, the user will be redirected to the homepage where the post was originally displayed.

    ![Delete post popup confirmation image](documentation/delete-post-popup-confirmation.png)

    **an alert confirming successful image**
    ![Allert post deleted successfully image](documentation/alert-post-deleted-successfully.png)

     - Edit Post: Redirects the user to the edit post page, where the post owner can delete individual or multiple images, add new images, and edit the header to update the post.

       - ![Edit post page image](documentation/edit-post-page.png)
        - **Image delete notification**
        ![Image delete notification](documentation/edit-your-post-image-delete-notification.png)

         - **Post sucessfully update notification**
        ![Post successfully update notification image](documentation/edit-your-post-update-notification.png)



    #### Heart icon, comment icon, share icon, connect icon, input field
    ![Heart, comment, share, connect icon image](documentation/post-icon-image.png)

    - Heart Icon: Clicking this icon toggles a 'like' for the post, increasing or decreasing the like count on its badge accordingly.
    - Comment Icon: Opens the comment section under the post. Users can view all comments made by others. Users can edit, delete, or reply to comments made by others. also user can reply the reply. Users can also reply to replies, facilitating deeper interaction.
    ![Comment reply for post image](documentation/comment-reply-for-post.png)
    - Share Icon: Allows users to share the post by copying its URL link.
    - Connect Icon: Sends a connection request to the post owner when clicked. If the post owner accepts, the connection count increases; if declined, there is no change.
    - Input Field: Users can type their comments here and press enter to post. Each new comment will update the comment count accordingly.

   #### Advertisement left section
    - Advertising Display: Advertisements paid for by clients are displayed and managed by the website administrator. Each advertisement includes a navigation link to the client’s external website, promoting their involvement with Thailand Guiding Light.
    ![Advert left section image](documentation/advert-left-section.png)

     #### Footer
    - Footer Layout: The footer is divided into three sections: 'Get in Touch', 'Customer Service', and 'Information'. Each section contains links to relevant pages. 

    ![Footer image](documentation/footer-image.png)

    - Get in Touch Section 
        - Social Media Icons: The Facebook, Twitter, YouTube, and Instagram icons provide direct links to our respective social media pages, facilitating easy access for users to connect with us.
    - Customer Service Section: This section contains four navigation links to assist with various customer service inquiries.
         - Thailand Guiding Light Ads: Currently a placeholder link without functionality.
         - Thailand Guiding Light Support: Another 
         placeholder link without functionality.
         - About Us: Redirects users to the About page, which details the website’s foundation, purpose, and introduces the staff.
         - Contact Us: Features a Google Maps link for navigation, a simple form for sending inquiries to the website administrator, and provides contact details including address, phone number, email, and hours of operation.
      - Information Section: This section contain two navigation links.
         - General Terms & Conditions: Currently a placeholder link without functionality.
         - Data Protection & GDPR: Currently a placeholder link without functionality.
    
    **All links currently without functionality are planned for future development.**


### Mobile home page
  **The mobile home page has a hamburger dropdown. It will show a navbar when you click on the hamburger icon and in the dropdown menu, you will have an admin site nav to navigate to the Django panel for admin and Comment Management: This feature provides a straightforward and user-friendly interface, allowing admins to create, read, update, and delete comments efficiently.**
  - mobile home page for admin
   - ![Mobile admin home page1 image](documentation/mobile-admin-home-page1.png)

   - ![Mobile admin home page2 image](documentation/mobile-admin-home-page2.png)

   - ![Mobile admin home page3 image](documentation/mobile-admin-home-page3.png)

   - ![Mobile admin home page4 image](documentation/mobile-admin-home-page4.png)

- Mobile Menu Toggle: Opens the hamburger menu.
  - admin
  ![Mobile admin hamburger open page user](documentation/mobile-admin-hamburger-page.png)

  - regular user
   -  ![Mobile regular user hamburger open page user](documentation/mobile-user-hamburger-page.png)

  - new user
  ![Mobile new user hamburger open page user](documentation/mobile-new-user-hamburger-page.png)

- mobile toggle menu open for admin
![Mobile admin toggle menu open image](documentation/mobile-admin-toggle-menu-open.png)

- mobile tool toggle menu open for admin
  ![Mobile admin toggle nav menu open image](documentation/mobile-admin-toggle-nav-menu-open.png)

- Mobile Tool Toggle: Opens the tool menu on mobile devices for the all user.
  ![Mobile user toggle nav menu open image](documentation/mobile-user-toggle-nav-menu-open.png)
 

 ## Profile page
  - This page has the primary data; this page allows the user to add or edit profile image, account name, full name, email address, phone number 
    - It has an avatar as a default if the user don't want to display their image
      - Your profile page
       - ![Mobile profile page1](documentation/mobile-profile-page1.png)

       - ![Mobile profile page2](documentation/mobile-profile-page2.png)

## Most popular page

  - ![Mobile most popular page1 image](documentation/mobile-most-popular-page1.png)

  - ![Mobile most popular page2 image](documentation/mobile-most-popular-page2.png)

  - ![Mobile most popular page3 image](documentation/mobile-most-popular-page3.png)

  - ![Mobile most popular page4 image](documentation/mobile-most-popular-page4.png)


## Your connection page
Connection Management: Account owners can view sent and received connection requests, as well as their current connections. They have the ability to accept, cancel, or disconnect friend requests directly from the connection list.
  - ![Mobile your connection page1](documentation/mobile-your-connection-page1.png)


- ![Mobile your connection page2](documentation/mobile-your-connection-page2.png)


## Allauth and Access pages :

  - Logout page
  
  ![Log out form page](documentation/logout-page-image.png)

  - login page
  ![Sign in page](documentation/sign-in-page.png)

  - sign up page
  ![Sign up page](documentation/sign-up-page.png)

