from fastapi import FastAPI

app = FastAPI()

# Now let get the home page for the endpoint 

@app.get("/")
async def red_root():
    return {"Message": "this is A BookShelf Assignment Project"}