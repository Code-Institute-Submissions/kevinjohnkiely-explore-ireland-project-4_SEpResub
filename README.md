# Explore Ireland

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/exploreireland.jpg">

Live link to Application: (https://explore-ireland.herokuapp.com/)

This Python & Django application is a tourism based memory sharing platform, designed to allow users to share their experiences of "The Emerald Isle". Users can upload their photos of locations and describe their experience with text and location information. Other users can also comment and like on these pictures, as well as upload their own images into the main homepage feed.

It is intended to be a promotional tool for tourism in Ireland, highlighting some of the superb attractions available here, and also serve as an engaging discussion utility for users who wish to converse on their own and other users favourite locations and memories of Ireland.

# Table of Contents

- [Explore Ireland](#explore-ireland)
  * [Login Details to Test Application](#login-details-to-test-application)
- [UX (User Experience)](#ux--user-experience-)
  * [Target Audience](#target-audience)
  * [User Stories](#user-stories)
    + [User Stories for Site User](#user-stories-for-site-user)
    + [User Stories for Admin User](#user-stories-for-admin-user)
  * [Wireframes](#wireframes)
    + [Wireframe of Home Page of Application](#wireframe-of-home-page-of-application)
    + [Wireframe of Location Post page](#wireframe-of-location-post-page)
  * [Agile Methodology](#agile-methodology)
- [System Design](#system-design)
  * [Entity Relationships](#entity-relationships)
- [Application Features](#application-features)
  * [Base Template](#base-template)
    + [Header](#header)
    + [Footer](#footer)
  * [Homepage](#homepage)
    + [Hero Image](#hero-image)
    + [Location Post List](#location-post-list)
  * [Location Post Page](#location-post-page)
  * [Add/Edit Location Page](#add-edit-location-page)
  * [My Locations Page](#my-locations-page)
  * [Login Page](#login-page)
  * [Signup Page](#signup-page)
- [Technologies Used](#technologies-used)
- [Code Validation](#code-validation)
  * [HTML Validation](#html-validation)
    + [Homepage](#homepage-1)
    + [Single Location Page](#single-location-page)
  * [CSS Validation](#css-validation)
  * [Javascript Validation](#javascript-validation)
  * [Python Validation](#python-validation)
- [Testing](#testing)
  * [Cross Browser Testing](#cross-browser-testing)
  * [Compatibility Testing](#compatibility-testing)
  * [Responsiveness Testing](#responsiveness-testing)
    + [Header/Navbar/Hero Image](#header-navbar-hero-image)
    + [List of Locations](#list-of-locations)
    + [My Locations Page](#my-locations-page-1)
    + [Single Location Page](#single-location-page-1)
  * [User Testing](#user-testing)
  * [Performance Testing](#performance-testing)
- [Bugs & Errors](#bugs---errors)
  * [Page Not Found](#page-not-found)
  * [Duplicate Slug](#duplicate-slug)
  * [Hero Image Missing](#hero-image-missing)
- [Considerations for Improvements](#considerations-for-improvements)
- [Deployment Methodology](#deployment-methodology)
- [Credits](#credits)


## Login Details to Test Application

Username: kevin
Password: test12345

<hr>

# UX (User Experience)

## Target Audience
The target audience for this application are potential tourists to Ireland, adults coming from a wide demographic area, who wish to explore new destinations and share their experiences with others. The application targets no particular subset of people, purely the tourist who wants to explore and is eager to advise others on their own experiences in Ireland.

## User Stories
The 2 types of user who can access this application are the Site User, and the Admin user. The Site User can utilise all the expected aspects of a image sharing application such as this, such as signing up, uploading pictures and commenting/liking. The Admin Users functionality is limited to the more administrative tasks in the backend of the application, such as moderating comments. The user stories of this application are listed as follows:

### User Stories for Site User

+ Create New Account: As a Site User I can register a new account so that I can create content and comment/like other content
+ View List of Locations: As a Site User I can view a list of location posts so that I can select one to view more details
+ View Single Location: As a Site User I can choose a single location post so that I can view the full post information
+ View Likes/Comments: As a Site User I can view the number of likes and comments on a location so that I can quickly view the popularity of a post
+ Manage My Content: As a Site User I can create, read, update, delete or publish my own content so that I can easily manage my site content
+ Like/Unlike a Location: As a Site User I can like and unlike a location so that I can interact with the site contents
+ Add Comment to Location: As a Site User I can add a comment to a location post so that I can stay involved in the conversation

### User Stories for Admin User
+ Approve Comments: As an Admin User I can approve or disapprove comments so that I can monitor any questionable comments

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
Once the system requirements from the Site Users perspective was finalized, a design of information flow was completed to demonstrate how the required data models were needed for the backend of this application. The following entity relationship (ER) diagram displays the relationship between 4 data models used in Explore Ireland - the User, the Location post, the User Profile and the Comment. This diagram was created at (https://app.diagrams.net/).

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/ER_diagram.png">

## Entity Relationships
The relationships between the data models in this application are as follows:
+ Locations - Comments (1 To Many): A location post can have many comments
+ Users - Locations (1 To Many): A user can post many locations
+ Users - Profile (1 to 1): A user can post just one user profile

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

## CSS Validation
There was no need to test the Bootstrap supplied css of this project, however I used a custom css file to supplement these rules located at static/css/style.css. I used the online CSS Validator at (https://jigsaw.w3.org/css-validator) to test the CSS of the application, using the "by direct input" option to copy and paste in the CSS code.

No errors were found during this validation.

## Javascript Validation
I used the online validator at (https://jshint.com/) to test the very small amount of Javascript included in this application, the script code to allow the bootstrap alert messages to fade out after appearing. No errors were reported after validation.

## Python Validation
I used the online Python validator at (http://pep8online.com/) to verify all the custom Python code and files that I added to the application. The files within the system that were validated are as follows
+ exploreireland/urls.py
+ locations/admin.py
+ locations/forms.py
+ locations/models.py
+ locations/urls.py
+ locations/views.py

The only issues that showed up during validation were common complaints such as trailing whitespaces and lines too long. I formatted all documents and they all now compy with the Pep8 validations.

<hr>

# Testing

## Cross Browser Testing

The application was functionally tested across the 3 web browsers, Google Chrome, Microsoft Edge & Mozilla Firefox. The site loaded consistently across all 3 and no issues were detected on any browser.

## Compatibility Testing

I tested the site across different devices, such as the Nokia 4.2 smartphone with Android 11, Lenovo Ideapad 3 laptop with different browsers on Windows 11, and on a Dell Studio laptop with different browsers on a Linux Mint operating system. No issues were reported between these devices.

## Responsiveness Testing

I tested this application so that it would scale well on all screen sizes, using Chrome Developer Tools to regularly test the layouts during development. The Bootstrap CSS framework provided all the breakpoints, and the key features of the application respond on smaller sceen sizes as follows:

### Header/Navbar/Hero Image

The items stack on top of each other on smallest screens, and on medium screen breakpoints the horizontal menu changes into the standard Bootstrap menu icon, which when clicked the menu items pop out vertically. The Hero image section scales well on smaller screens with the background image and necessary margins resizing for small screen sizes.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/responsive/responsive-home.jpg">

### List of Locations

On larger screen sizes this is a 3 column grid of location post details, however on medium to small screen sizes this scales back to a 1 column display.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/responsive/responsive-posts.jpg">

### My Locations Page

On larger screen sizes, the location name is listed with the respective edit/delete/publish buttons on the right on the same row, but on smaller screens the buttons stack up underneath this row.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/responsive/responsive-locations.jpg">

### Single Location Page

On smaller screen sizes, all content stacks up into one column, the location details and image first, next comes the comment form, and finally the already submitted comments below this.

## User Testing

This application was tested by another person and I noted their comments and experience using the system. Overall, they found it a quite usable and pleasant experience, but discovered one bug that is later explained in the Errors and Bugs section (page not found).

To ensure a easy user experience, it was vital to use form validation throughout the application to ensure that no empty data was being submitted by the user, by use of the "required" HTML attribute on the form input fields, the user being made aware of this as follows:

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/form-validation.jpg">

Also an important aspect of the user experience was to ensure that a user did not accidentally delete some of their content. On the My Locations page, the user is presented with a list of their own uploaded locations and a button to delete a location if they wish. Once the user clicks delete, a popup modal appears asking if they are sure they want to carry this out:

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/form-modal.jpg">

## Performance Testing

On near completion of the application I used Google Chromes Lighthouse feature to test the application peformance, the results seen below:

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/lighthouse-before.jpg">

I was happy with most of those scores, but the 75 for Best Practices required some further investigation. The error message provided was "Mixed Content: The page at 'https://explore-ireland.herokuapp.com/' was loaded over HTTPS, but requested an insecure stylesheet 'http://fonts.googleapis.com/css?".

I fixed this issue by removing the imported Google Font and using the native Bootstrap version, there was very little difference between these font styles in any case. This resulted in a much higher score for Best Practices:

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/lighthouse-after.jpg">

<hr>

# Bugs & Errors

I encountered a number of bugs during the development of this project, thankfully I was able to resolve all of these issues after some time investigating.

## Page Not Found

On the My Locations page, there is a list of the users uploaded locations and buttons to edit/publish the post. The title of each of these locations is also a link to that individual post page, and it was discovered in user testing that this link was broken if the location had not been published yet.

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/bugs/bug-no-route.jpg">

To fix this I added some conditional python code to load an alternative location title heading, one without the hyperlink so that the broken link will never be rendered to the view:

    {% if not location.status %}
        <h2 class="card-title">{{ location.title }}</h2>
    {% else %}
        <a href="{% url 'location_single' location.slug %}" class="post-link"><h2 class="card-title">{{ location.title }}</h2></a>
    {% endif %}

## Duplicate Slug 

When a user creates a new location post, I wanted it to be possible for a user to supply a location title that could be repeated in a later post, or for another user to upload a similar location with the same title, example "Cliffs of Moher". This was made possible by not setting the title field in the model to be unique. It was possible to upload the duplicate locations, but on clicking the link for this location, an error occurred relating the slug of the post as follows:

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/bugs/bug-multiple.jpg">

To fix this, I needed to give each location post a unique slug, despite having the same location title. Thus I added the following code, appending a timestamp to the location slug. I realise this is not a complete solution as it is possible, although highly unlikely, that 2 separate users could upload a location with the same title at the exact same second in time (similar timestamp), but I felt this was a good enough solution for this project.

    curr_time = datetime.now()
    date_time = curr_time.strftime("%m/%d/%Y%H:%M:%S")
    location.slug = slugify('-'.join([location.title, date_time]))

## Hero Image Missing

On my first deployment of the application to the Heroku hosting platform, I noticed that the hero/banner image on the homepage was missing, despite showing up fine on my local development environment on Gitpod. On discussion with my project mentor I diagnosed that this was an issue with the Cloudinary host not recognising images that were referenced as background images in css coming from the static folder, and this was solved by uploading the image to cloudinary, and using that file link in the css file instead, as follows:

    .jumbotron {
    background: url("https://res.cloudinary.com/dqp0vlv6x/image/upload/v1658824440/cliffs_home_ezgfp1.jpg") 50% 0 no-repeat fixed;
    min-height: 20rem;
    padding: 3rem;
    }

<hr>

# Considerations for Improvements

The following is a list of aspects of the application that could be added or improved upon, which could not be achieved due to time constraints.

+ CRUD Functionality on Comments - The user would be able to update or delete the comments they have made on location posts, similar to how they do it on their uploaded locations.
+ Search Functions - A user could search for posts by location, a utility that would be of much more usefulness once the application was populated by lots of varying content by multiple users.
+ Integration of Google Maps - A Google Maps API could be incorporated to load in each location single post page to give clear directions of where the place is in Ireland.

<hr>

# Deployment Methodology

To deploy this application to Heroku, I closely followed the very helpful Django Cheat Sheet (https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit) supplied by Code Institute for this project.

Whenever I needed to change something from the deployed version, I would navigate to the settings file and change the DEBUG variable to True so that the application would run without errors on Gitpod, and change back to False before deploying once again to Heroku.

<hr>

# Credits

+ All image content for this application came from Pexels (https://www.pexels.com/)
+ The code used to give each location a unique slug using timestamps was sourced from Stack Overflow (https://stackoverflow.com/)