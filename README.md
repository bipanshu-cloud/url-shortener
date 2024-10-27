URL Shortener
A simple yet powerful URL shortener built with FastAPI and Python. This application enables users to shorten long URLs, facilitating easier sharing and access.

Features
URL Shortening: Generate a shortened URL for any given long URL.
Redirection: Automatically redirect users from the shortened URL to the original long URL.
Error Handling: Graceful handling of invalid URLs and server errors.

Installation
Prerequisites
Python 3.6 or higher
pip (Python package installer)

PI Endpoints
Shorten a URL
Endpoint: /shorten
Method: POST
Request Body:

How It Works
Submit a URL: Users input a long URL via the /shorten endpoint.
Hash Generation: The application generates a unique hash for the long URL using MD5.
Store Mapping: The mapping between the short URL and the original URL is stored in a dictionary.
Accessing Short URL: When the short URL is accessed, users are redirected to the original long URL.
Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
