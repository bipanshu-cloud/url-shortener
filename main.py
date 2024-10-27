from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import hashlib
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# A dictionary to store the mapping of short URLs to long URLs
url_mapping = {}

class URLRequest(BaseModel):
    url: str

class URLResponse(BaseModel):
    short_url: str
    long_url: str

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    logging.error(f"An error occurred: {exc}")
    return HTMLResponse(content="Internal Server Error", status_code=500)

@app.post("/shorten", response_model=URLResponse)
async def shorten_url(request: URLRequest):
    # Create a short URL using a hash of the long URL
    short_url_hash = hashlib.md5(request.url.encode()).hexdigest()[:6]  # Taking first 6 chars
    short_url = f"http://localhost:8000/{short_url_hash}"  # Adjust for your domain

    # Store the mapping
    url_mapping[short_url_hash] = request.url

    return URLResponse(short_url=short_url, long_url=request.url)

@app.get("/{short_url_hash}")
async def redirect_to_long_url(short_url_hash: str):
    long_url = url_mapping.get(short_url_hash)
    if long_url:
        return HTMLResponse(content=f"<script>window.location='{long_url}'</script>")
    raise HTTPException(status_code=404, detail="URL not found")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <form action="/shorten" method="post">
        <input type="text" name="url" placeholder="Enter URL to shorten" required>
        <button type="submit">Shorten URL</button>
    </form>
    """
