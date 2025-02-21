
# Backend Technical Specs

## Business Goal: 
A language learning school wants to build a prototype of learning portal which will act as three things:
Inventory of possible vocabulary that can be learned
Act as a  Learning record store (LRS), providing correct and wrong score on practice vocabulary
A unified launchpad to launch different learning apps

You have been tasked with creating the backend API of the application.

## Technical Restrictions:
- The backend will be using Python 
- The database will be SQLite3
- The API will be built using FastAPI
- The API will always return JSON
- THere will be no authentication or authorisation
- everything will be treated as a single user

## Directory Structure

```text
backend-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers/
│       ├── __init__.py
|       ├── dashboard.py
│       ├── words.py
│       ├── words_groups.py
|       ├── word_review_items.py
│       ├── groups.py
│       ├── study_sessions.py
│       └── study_activities.py
├── db/
│   ├── migrations/
│   └── seeds/
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_words.py
│   ├── test_words_groups.py
│   ├── test_groups.py
│   ├── test_study_sessions.py
│   └── test_study_activities.py
├── words.db
├── requirements.txt
└── README.md
```
## Database Schema

Our database will be a single sqlite database called `words.db` that will be in the root of the project folder of `backend-fastapi`

We have the following tables:

- words - stored vocabulary words
    - id integer
    - japanese string
    - romaji string
    - english string
    - parts json
- words_groups - join table for words and groups. Many-to-many
    - id integer
    - word_id integer
    - group_id integer
- groups - thematic groups of words
    - id integer
    - name string
- study_sessions - records of study sessions grouping word_review_items
    - id integer
    - group_id integer
    - created_at datetime
    - study_activity integer
- study_activities - a specific study activity, linking a study session to group
    - id integer
    - study_session_id integer
    - created_at datetime
- word_review_items - a record of word practice, determining if the word was correct or not
    - word_id integer
    - study_session_id integer
    - correct booleanz
    - created_at datetime

## API Endpoints

### GET /api/dashboard/last_study_session
Returns information about the last study session
#### JSON response
```json
{
  "id": 123,
  "group_id": 456,
  "created_at": "2023-10-01T12:00:00Z",
  "study_activity_id": 789,
  "group_id": 456,
  "name": "Basic Greetings"  
}
```

###  GET /api/dashboard/study_progress
#### JSON response
```json
{
  "total_words_studied": 150,
  "total_study_sessions": 10,
  "total_active_groups": 3,
  "study_streak": 5
}
```
### GET /api/dashboard/quick-stats
Returns quick overview statistics
#### JSON response

```json
{
  "success_rate": 0.80,
  "total_study_sessions": 4,
  "total_active_groups": 3,
  "study_streak": 4
}
```

### GET /api/study_activities/:id

#### JSON response
```json
{
  "id": 1,
  "name": "Vocabulary Practice",
  "thumbnail_url": "https://example.com/thumbnails/vocab_practice.png",
  "description": "Practice your vocabulary with this activity."
}
```
### GET /api/study_activities/:id/study_sessions

#### JSON response
```json
{
  "items": [
    {
      "id": 101,
      "activity_name": "Vocabulary Quiz",
      "group_name": "Beginner Group",
      "start_time": "2023-01-05T10:00:00Z",
      "end_time": "2023-01-05T11:00:00Z",
      "review_items_count": 20
    },
    {
      "pagination": 102,
      "current_page": 1,
      "total_pages": 5,
      "end_time": 100,
      "items_per_page": 20
    }
  ]
}
```

### POST /api/study_activities
    - required params: group_id, study_activity_id

#### Request Params
- group_id integer
- study_activity_id integer

#### JSON response
``` json
{
  "id": 101,
  "group_id": 1,
}
```
### GET /api/words
    - pagination with 100 items per page

#### JSON response
```json
{
  "items": [
    {
      "id": 1,
      "japanese": "こんにちは",
      "romaji": "konnichiwa",
      "english": "hello",
      "correct_count": 10,
      "wrong_count": 2
    },
    {
      "id": 2,
      "japanese": "ありがとう",
      "romaji": "arigatou",
      "english": "thank you",
      "correct_count": 15,
      "wrong_count": 1
    }
    // ... up to 100 items
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 10,
    "total_items": 1000,
    "items_per_page": 100
  }
}
```
### GET /api/words/:id

#### JSON response
```json
{
  "id": 1,
  "japanese": "こんにちは",
  "romaji": "konnichiwa",
  "english": "hello",
  "correct_count": 10,
  "wrong_count": 2,
  "groups": [
    {
      "id": 1,
      "name": "Greetings"
    },
    {
      "id": 2,
      "name": "Common Phrases"
    }
  ]
}
```

### GET /api/groups
    - pagination with 100 items per page
#### JSON response
```json
{
  "items": [
    {
      "id": 1,
      "name": "Beginner Vocabulary",
      "word_count": 50
    },
    {
      "id": 2,
      "name": "Intermediate Vocabulary",
      "word_count": 75
    }
    // ... up to 100 items
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 10,
    "total_items": 1000,
    "items_per_page": 100
  }
}
```

### GET /api/groups/:id
#### JSON response
```json
{
  "id": 1,
  "name": "Beginner Vocabulary",
  "stats": 
    {
      "total_word_count": 50
    }
}
```

### GET /api/groups/:id/words
#### JSON response
```json
{
  "items": [
    {
      "id": 1,
      "japanese": "こんにちは",
      "romaji": "konnichiwa",
      "english": "hello",
      "correct_count": 10,
      "wrong_count": 2
    },
    {
      "id": 2,
      "japanese": "ありがとう",
      "romaji": "arigatou",
      "english": "thank you",
      "correct_count": 15,
      "wrong_count": 1
    }
    // ... up to 100 items
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 10,
    "total_items": 1000,
    "items_per_page": 100
  }
}
```

### GET /api/groups/:id/study_sessions
#### JSON response
```json
{
  "items": [
    {
      "id": 101,
      "activity_name": "Vocabulary Practice",
      "group_name": "Beginner Group",
      "start_time": "2023-01-05T10:00:00Z",
      "end_time": "2023-01-05T11:00:00Z",
      "review_items_count": 20
    },
    {
      "id": 102,
      "activity_name": "Vocabulary Practice",
      "group_name": "Beginner Group",
      "start_time": "2023-01-06T10:00:00Z",
      "end_time": "2023-01-06T11:00:00Z",
      "review_items_count": 25
    }
  ],
"pagination": {
    "current_page": 1,
    "total_pages": 10,
    "total_items": 1000,
    "items_per_page": 100
  }
}
```

### GET /api/study_sessions
#### JSON response
```json
{
  "items": [
    {
      "id": 101,
      "activity_name": "Vocabulary Practice",
      "group_name": "Beginner Group",
      "start_time": "2023-01-05T10:00:00Z",
      "end_time": "2023-01-05T11:00:00Z",
      "review_items_count": 20
    },
    {
      "id": 102,
      "activity_name": "Vocabulary Practice",
      "group_name": "Beginner Group",
      "start_time": "2023-01-06T10:00:00Z",
      "end_time": "2023-01-06T11:00:00Z",
      "review_items_count": 25
    }
    // ... up to 100 items
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 10,
    "total_items": 1000,
    "items_per_page": 100
  }
}
```

### GET /api/study_sessions/:id
#### JSON response
```json
{
  "id": 1,
  "activity_name": "Vocabulary Practice",
  "group_name": "Beginner Group",
  "start_time": "2023-01-05T10:00:00Z",
  "end_time": "2023-01-05T11:00:00Z",
  "review_items_count": 20
}
```

### GET /api/study_sessions/:id/words
#### JSON response
```json
{
  "items": [
    {
      "id": 1,
      "japanese": "こんにちは",
      "romaji": "konnichiwa",
      "english": "hello",
      "correct_count": 10,
      "wrong_count": 2
    },
    {
      "id": 2,
      "japanese": "ありがとう",
      "romaji": "arigatou",
      "english": "thank you",
      "correct_count": 15,
      "wrong_count": 1
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 10,
    "total_items": 1000,
    "items_per_page": 100
  }
}
```


### POST /api/reset_history
#### JSON response
```json
{
    "success": true,
    "message": "Study history has been reset"
}
```
### POST /api/full_reset
#### JSON response
```json
{
    "success": true,
    "message": "Study history has been reset"
}
```
### POST /api/study_sessions/:id/words/:word_id/review
#### Request Params
- id (study_session_id) integer
- word_id integer
- correct boolean

#### Request Payload
```json
{
    "correct": true
}
```

#### JSON response
```json
{
  "success": true,
  "study_session_id": 1,
  "word_id": 2,
  "correct": true,
  "created_at": "2023-01-01T12:00:00Z",
  "updated_at": "2023-01-01T12:00:00Z"
}

```

## Scripts (Tasks)

### Initialise Database
This task will initialize the sqlite database called `words.db`

### Migrate Database
This task will run a series of migrations sql files on the database

Migrations live in the  `migration` folder.
The migration files will be run in order of their file name.
The files names should look like this:

```sql
0001_init.sql
0002_create_words_table.sql
```


### Seed data
This task will import json files and transform them into target data for our database.

All seed files live in the `seeds` folder
All seed files should be loaded. 

In our task we should have DSL to specify each seed file and its expected group word name. 

```json
[
  {
    "japanese": "こんにちは",
    "romaji": "konnichiwa",
    "english": "hello"
  },
  ...
]

```