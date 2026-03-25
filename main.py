from fastapi import FastAPI

app = FastAPI()

# The BookShelf Initial Data
BOOKS = [
    {
        "title": "AI Agent Programming in Python",
        "author": "Trent Aldridge",
        "category": "Technology"
    },
    {
        "title": "Dream Count",
        "author": "Chimamanda Ngozi Adichie",
        "category": "Fiction"
    },
    {
        "title": "FastAPI & MCP in Python",
        "author": "Todd Chandler",
        "category": "Technology"
    },
    {
        "title": "The Midnight Train",
        "author": "Matt Haig",
        "category": "Fantasy"
    },
    {
        "title": "London Falling",
        "author": "Patrick Radden Keefe",
        "category": "Non-Fiction"
    },
    {
        "title": "Atomic Habits Workbook",
        "author": "James Clear",
        "category": "Self-Help"
    }
]

# Now let get the home page for the endpoint 

@app.get("/")
async def read_root():
    return {"Message": "this is A BookShelf Assignment Project"}

@app.get("/books")
async def read_all_books():
    return BOOKS