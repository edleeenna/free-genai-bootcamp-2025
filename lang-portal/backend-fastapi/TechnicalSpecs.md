
# Technical Specs

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

## Database Schema

We have the following tables:

- words - stored vocabulary words
- words_groups - join table for words and groups. Many-to-many
- groups - thematic groups of words
- study_sessions - records of study sessions grouping word_review_items
- study_activities - a specific study activity, linking a study session to group
- word_review_items - a record of word practice, determining if the word was correct or not

### API Endpoints

