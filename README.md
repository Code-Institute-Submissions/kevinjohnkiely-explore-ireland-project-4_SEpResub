# Explore Ireland

<!-- Screengrab of website goes here later -->

Live link to Application: (https://explore-ireland.herokuapp.com/)

This Python & Django application is a tourism based memory sharing platform, designed to allow users to share their experiences of "The Emerald Isle". Users can upload their photos of locations and describe their experience with text and location information. Other users can also comment and like on these pictures, as well as upload their own images into the main homepage feed.

It is intended to be a promotional tool for tourism in Ireland, highlighting some of the superb attractions available here, and also serve as an engaging discussion utility for users who wish to converse on their own and other users favourite locations and memories of Ireland.

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
<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/WireframeHomepage.png">

### Wireframe of Location Post page
<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/WireframePostPage.png">

## Agile Methodology
I used the Kanban board feature in the github project repo to layout the user stories required for this application. As I completed each sprint of work to realise a feature, I moved the user story issue across the kanban board in stages, from "To do" to "in progress" and finally "done".

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/agile.jpg">


# System Design
Once the system requirements from the Site Users perspective was finalized, a design of information flow was completed to demonstrate how the required data models were needed for the backend of this application. The following entity relationship (ER) diagram displays the relationship between 3 data models used in Explore Ireland - the User, the Location post, and the Comment. This diagram was created at (https://app.diagrams.net/).

<img src="https://github.com/kevinjohnkiely/explore-ireland-project-4/blob/main/screenshotsWireframes/ER_diagram.jpg">

## Entity Relationships
The relationships between the data models in this application are as follows:
+ Locations - Comments (1 To Many): A location post can have many comments
+ Users - Locations (1 To Many): A user can post many locations
