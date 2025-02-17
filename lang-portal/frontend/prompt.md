# Frontend Prompt Document
We would like to build a Japanese language learning web app.

## Role/Profession
Frontend Developer

## Project Description

### Project Brief

We are building a Japanese Language learning web-app which serves the following purposes:
    - a portal to launch study activities
    - to store, group and explore japanese vocabulary
    - to review study progress

### Technical Requirements
- React.js as the frontend library
- Tailwind CSS as the css framework
- Vite.js as the local development server
- Typescript for the programming language
- ShadCN for components

### Frontend Routes
This is a list of routes for our web-app we are building.
Each of these routes are a page and we'll describe them in more details under the pages heading.

/dashboard
/study-activites
/study-activites/:id
/words
/words/:id
/groups
/groups/:id
/sessions
/settings

The default route / should forward to dashboard

### Global Components
#### Navigation

THere will be a horizontal navigation bar with the following links:
- Dashboard
- Study Activities
- Words
- Word Groups
- Sessions
- Settings

#### Breadcrumbs
 Beneath the navigation there will be breadcrumbs so users can easily see where they are. Examples of breadcrumbs

 Dashboard
 Study Activities > Adventure MUD
 Study Activities > Typing Tutor
 Words > 
 Word Groups > Core Verbs

 ### Pages

 #### Dashboard

 This page provides a summary of the student's progression

 - Last Session

 #### Study Activities Index

 The route for this page /study-activities

 This is a grade of cards which represent an activity

 A card has a :
 - thumbnail
 - title
 - "Launch" button
 - View button

 The Launch button will open a new address in a new tab.
 Study activities are their own apps, but in order for them to launch they need to be provided a group_id

 eg. localhost:8081?group_id=4

 This page requires no pagination because there is unlikely to be more than 20 possible study activities

 The view button will go to the Student Activities Show Page.

 #### Study Activities Show
 The route for this page /study-activities/:id

 This page will have an information section will contain:
 - thumbnail
 - title
 - description
 - launch button

 There will be a list of sessions for this study activity
 - a session item will contain
    - Group name: so you know what group name was used for the sessions
    - This will be a link to the Group Show Page
    - Start Time: When the session was created in YYYY-MM-DD HH:MM format (12 hours)
    - End Time: When the last word_review_item was created
    - Review Items: the number of review items

### Words Index

The route for this page /words

This is a table of words with the following cells:

- Japanese: the Japanese word with Kanji
    - This will also contain a small button to play the sound of the word
    - The Japanese word will be a link to the Words Show page
- Romaji: the romaji version of the word
- English: The english version of the word
- Correct: Number of correct word review items
- Wrong: Number of wrong word review items

There should only be 50 words displayed at a time

There needs to be pagination
- Previous button: grey out if you cannot go further back
- Page 1 of 3: With the current page bolded
- Next button: greyed out if you cannot go any further forwarded

All table headings should be sortable, If you click it will toggle between ASC and DESC.

An ascii arrow should indicate direction and the column being sorted with ASC pointing down and DESC pointing up.

### Words Show

The route for this page /words/:id

### Word Groups Index

The route for this page /word-groups

This is the table of word groups with the following cells:
- Group Name: The name of the group
    - This will be a link to Word Groups Show
- Words: The number of words associated with this group

This page contains the same sorting and pagination logic as the Words Index page

### Words Groups Show

The route for this page /words-groups:id

This has the same components as Words Index but its scoped to only show words that are associated with this group.

### Sessions Index
The route for this page /sessions

This page contains a list of sessions similar to Study Activities Show

This page contains the same sorting and pagination logic as the Shows Index page


### Settings Page

The route for this page /settings

Reset History Button: This has a button that allows us to reset the entire database.
We need to confirm this action in a dialog and type the word reset me to confirm

Dark Mode Toggle: This is a toggle that changes from light to dark theme.

