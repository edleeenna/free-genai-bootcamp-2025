from fastapi import FastAPI
from app.routers import words, words_groups, groups, study_sessions, study_activities, word_review_items, dashboard
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(words.router)
app.include_router(words_groups.router)
app.include_router(groups.router)
app.include_router(study_sessions.router)
app.include_router(study_activities.router)
app.include_router(word_review_items.router)
app.include_router(dashboard.router)