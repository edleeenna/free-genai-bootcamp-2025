
# Frontend Technical Specs

## Pages

### Dashboard `/dashboard`

#### Purpose
The purpose of this page is to provide a summary of learning and act as the default page when a user visits the web app.

#### Components
This page contains the following components
- Last study session
    shows last activity used
    shows when last activity used
    summarises wrong vs correct from last activity
    has a link to the group
- Study progress
    - total words studied
        - across all study session show the total words studied out of all possible words in our database
    - display a mastery progress e.g. 0%
    -
- Quick states
    - success rate e.g. 80%
    - total study sessions e.g. 4
    - total active groups e.g. 3
    - study streak e.g. 4 days
- Start studying button
    - goes to study activites page

#### Needed API endpoints

We'll need the following API endpoints to power this page

GET /api/dashboard/last_study_session
GET /api/dashboard/study_progress
GET /api/dashboard/quick-stats

### Study Activities Index `/study-activities`

#### Purpose
The purpose of this page is to show a collection of study activities with a thumbnail and its name, to either launch or view the stufy activity.

#### Components

- Study Activity card
    - shows a thumbnail of the study activity
    - the name of the study activity
    - a launch button to take to the launch page
    - the view page to view more information about past study sessions for this study activity

#### Needed API endpoints

- GET /api/study_activities

### Study Activity Show `/study_activities/:id`

#### Purpose
The purpose of this page is to show the details of a study activity and its past study sessions.

#### Components
- name of study activity
- Thumbnail of study activity
- Description of study activity
- Launch button 
- Study Activities Paginated List
  - id
  - activity name
  - group name
  - start time
  - end time (inferred by the last word_review_item submitted)
  - number of review items

#### Needed API endpoints
- GET /api/study_activities/:id
- GET /api/study_activities/:id/study_sessions

### Study Activities Launch `/study_activities/:id/launch`

#### Purpose
The purpose of this page is to launch a study activity

#### Components
-  name of study activity
- Launch form
    - select field for group
    - launch now button

#### Behaviour

After the form is submitted, a new tab opens with the study activity based on its URL provided in the database. ALso after form is submitted the page will redirect to the study session show page.

#### Needed API Endpoints
- POST /api/study_activities

### Words Index `/words`

#### Purpose
The purpose of this page is to show all words in our database.

#### Components
- Paginated Word List
    - Columns
        - Japanese
        - Romaji
        - English
        - Correct Count
        - Wrong Count
    - Pagination with 100 items per page
    - Clicking the Japanese word will take us to the word show page

#### Needed API Endpoints
- GET /api/words

### Word Show `/words/:id`

#### Purpose
The purpose of this page is to show informaiton about a specific word.

#### Components
- Japanese
- Romaji
- English
- Study Statistics
    - Correct Count
    - Wrong Count
- Word groups
    - shown as a series of pulls e.g. tags
    - when group name is clicked it will take us to the group show page


#### Needed API Endpoints

- GET /api/words/:id

### Word Groups `/groups`

#### Purpose
The purpose of this page is to show a list of groups in our database.

#### Components
- Paginated Group List
    - Columns
        - Group Name
        - Word Count
    - Clicking the group name will take us to the group show page

#### Needed API Endpoints
- GET /api/groups

### Word Show `/groups/:id`

#### Purpose
The purpose of this page is to show information about a specific group.

#### Components
- Group name
- Group Statistics
    - Total word count
- Words in Group (Paginated list of words)
    - Should use the same component as the words index page.
- Study Sessions (Paginated list of Study Sessions)
    - Should use the same component as the study sessions index page

#### Needed API Endpoints
- GET /api/groups/:id (the name and group stats)
- GET /api/groups/:id/words
- GET /api/groups/:id/study_sessions


### Study Sessions Index `/study_sessions`

#### Purpose
The purpose of this page is to show a list of study sessions in our database.

#### Components
- Paginated Study Session List
    - Columns
        - Id
        - Activity Name
        - Group Name
        - Start Time
        - End Time
        - Number of Review Items
    - Clicking the study session id will take to the study session show page

#### Needed API Endpoints

- GET /api/study_sessions


### Study Session Show `/study_sessions/:id`

#### Purpose
The purpose of this page is to show information about a specific study session

#### Components

- Study Session Details
    - Activity Name
    - Group Name
    - Start Time
    - End Time
    - Number of Review Items
- Words Review Items (Paginated List of Words)
    - Should use the same component as the words index page

#### Needed API Endpoints
- GET /api/study_sessions/:id
- GET /api/study_sessions/:id/words


### Settings Page `/settings`

#### Purpose
The purpose of this page is to make configurations to the study portal

#### Components
- Theme selection e.g. Light, Dark, System Default
- Different Language Selection (Future Scope)
- Reset History Button
    - this will delete all study sessions and word review items
- Full Reset Button
    - this will drop all tables and re-create with Seed Data

#### Needed API Endpoints
- POST /api/reset_history
- POST /api/full_reset