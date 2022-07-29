# Explore Ireland

<!-- Screengrab of website goes here later -->

Live link to Application: (https://explore-ireland.herokuapp.com/)

This Python & Django application is a tourism based memory sharing platform, designed to allow users to share their experiences of "The Emerald Isle". Users can upload their photos of locations and describe their experience with text and location information. Other users can also comment and like on these pictures, as well as upload their own images into the main homepage feed.

It is intended to be a promotional tool for tourism in Ireland, highlighting some of the superb attractions available here, and also serve as an engaging discussion utility for users who wish to converse on their own and other users favourite locations and memories of Ireland.

<hr>

# UX (User Experience)

## Target Audience
The target audience for this application are potential tourists to Ireland, adults coming from a wide demographic area, who wish to explore new destinations and share their experiences with others. The application targets no particular subset of people, purely the tourist who wants to explore and is eager to advise others on their own experiences in Ireland.

## User Stories
The 2 types of user who can access this application are the Site User, and the Admin user. The Site User can utilise all the expected aspects of a image sharing application such as this, such as signing up, uploading pictures and commenting/liking. The Admin Users functionality is limited to the more administrative tasks in the backend of the application, such as moderating comments. The user stories of this application are listed as follows:

+ Create New Account: As a Site User I can register a new account so that I can create content and comment/like other content
+ View List of Locations: As a Site User I can view a list of location posts so that I can select one to view more details
+ View Single Location: As a Site User I can choose a single location post so that I can view the full post information
+ View Likes/Comments: As a Site User / Admin I can view the number of likes and comments on a location so that I can quickly view the popularity of a post
+ Manage My Content: As a Site User I can create, read, update, delete or publish my own content so that I can easily manage my site content
+ Approve Comments: As an Admin User I can approve or disapprove comments so that I can monitor any questionable comments
+ Like/Unlike a Location: As a Site User I can like and unlike a location so that I can interact with the site contents
+ Add Comment to Location: As a Site User I can add a comment to a location post so that I can stay involved in the conversation

## Wireframes
The following images show wireframes of the 2 primary designs of the application. These wireframes were created using [Balsamiq Wireframes](https://balsamiq.com/).

### Wireframe of Home Page of Application
This wireframe shows the main landing page of the application, whether user is logged in or not. It gives a feel for the general layout of the page, and where the location posts will appear and what format they will take.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/WireframeHomepage.png">

### Wireframe of Location Post page
This wireframe shows the individual location page, with the like and comment features only available to users who are logged in, blank spaces appearing in those places for users not logged in.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/WireframePostPage.png">

## Agile Methodology
I used the Kanban board feature in the github project repo to layout the user stories required for this application. As I completed each sprint of work to realise a feature, I moved the user story issue across the kanban board in stages, from "To do" to "in progress" and finally "done".

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/agile.jpg">

<hr>

# System Design
Once the system requirements from the Site Users perspective was finalized, a design of information flow was completed to demonstrate how the required data models were needed for the backend of this application. The following entity relationship (ER) diagram displays the relationship between 3 data models used in Explore Ireland - the User, the Location post, and the Comment. This diagram was created at (https://app.diagrams.net/).

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/ER_diagram.jpg">

## Entity Relationships
The relationships between the data models in this application are as follows:
+ Locations - Comments (1 To Many): A location post can have many comments
+ Users - Locations (1 To Many): A user can post many locations

<hr>

# Application Features

## Base Template
The 2 areas common to all viewports throughout the application are the header and footer sections, which were coded into a "base.html" template in the django framework and thus appear commonly across the site.

### Header

This section is the main header of the application, incorporating a site logo to the left, and the main navbar to the right. The navbars responsiveness to different screen sizes is provided by Bootstraps media queries, and the contents of the navbar links change dependant on if the user is logged in or not. Also to the right of the logo, some welcome text appears when the user is logged in, displaying the users username and giving a good visual indication that they are successfully logged in.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-navbar.jpg">

### Footer

This section is similar in design to the header section, with just some basic info text centered accompanying some dummy social media icon links

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-footer.jpg">

## Homepage

### Hero Image

The first section of the home page content is a hero/banner image, designed for effective visual attraction to the site. The background image shows a typical Irish location, with some introductory text layed on top to give a quick description of what the site entails.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-hero.jpg">


### Location Post List

The second section of the home page is the list of Location Posts with the headline "What people are sharing". This is a 3 column of grid of all posts by users, the most recent being first in the list. Each post has an image and some basic information about each post, with more info being available on clicking on each.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-posts.jpg">

## Location Post Page

When a user clicks on an individual location, a view appears showing a larger image of the location, textual descriptions and a heart icon where the user can like or unlike this post. This section appears floated to the left, with a comment form on the right where the user can submit feedback on this location.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-onepost.jpg">

Below this section lies the comments section, taking up full width of page and display all relevant comment information with the most recent comment appearing at top of the list

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-comments.jpg">

## Add/Edit Location Page

This separate page allows the user to upload their own location and provides the summernote text editor if they wish to include a more customizable description of the location. The view for editing a location uses an almost identical page to this, the only differnce being the button at the bottom showing "Change Location" label. In the form, the user has the choice to publish their post, or save as a draft which they later choose to publish on site.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-addedit.jpg">

## My Locations Page

This page shows all the locations that a user has uploaded, and allows them to delete or edit them as they wish. It also includes a "Publish" button, which allows the user to make their post go live on the site, if they chose to save their post as a draft when they added it.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-locations.jpg">

## Login Page

This is a standard login page using a combination of Bootstrap and a Django plugin called Crispy Forms, which enables display of a simple login form with username and password with a submit button.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-login.jpg">

## Signup Page

This is similar to the login page in terms of being produced by combining Bootstrap and Crispy Forms customization. It allows the user to enter the necessary details and displays a prompt tooltip if any of the form fields are left empty on submitting.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/features/features-signup.jpg">

<hr>

# Technologies Used

The following is a list of the various technologies employed to build this project

+ HTML5 - Hypertext markup language used to give the website its overall structure and semantic value.
+ CSS3 - Cascading Style Sheets used to apply consistent styles across all sections of the application.
+ Bootstrap5 - CSS framework to assist in rapid site development. Augmented by some custom CSS also.
+ JavaScript - Javascript coding used sparingly to make alert messages fade out and disappear.
+ Git/Gitpod - Gitpod used as development platform to build incremental versions of the application and Git commands to backup these changes to Github.
+ Heroku - Heroku platform used for hosting the deployed application.
+ PostgreSQL - This was used as the database storage for the application, it was added as a Resource in the Heroku hosting platform settings.
+ Cloudinary - A cloud based storage platform where the location images are uploaded to and stored on.
+ Django - Python based web application framework used to build the application.
+ Font Awesome - Fontawesome toolkit imported into HTML files and its icons used to show button icons and logo.
+ Balsamiq Wireframes - Downloadable software to create the wireframe mockups.

<hr>

# Code Validation

## HTML Validation
I used the online validator at (https://validator.w3.org/) to check the HTML of the application. All of the applications frontend views were checked, with warnings/errors as follows:

### Homepage
+ Consider adding a lang attribute to the html start tag to declare the language of this document. (This warning appeared for all pages across the site as it originates in the base HTML template and thus affects all views)
+ An img element must have an alt attribute

### Single Location Page
+ No p element in scope but a p end tag seen.

The last error took some investigation as it did not appear in the template code. However, I discovered that it originated in the summernote text editor, when text describing the location was copied and pasted in from another source, some unintended html tags were also copied in. This was solved by editing the location description in the summernote editor, using the "Code View" button to help remove unwanted html tags.

All of these issues were fixed and the site now complies with HTML standards.
