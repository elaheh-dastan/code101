# Structure
My sample project was QueryCraft
✔️ querycraft/ is a Django APP

This contains:

- models
- views
- URLs
- templates
- migrations
- management commands
- custom logic (services/)

This is exactly what a Django app folder should look like.

✔️ querycraft_project/ is the Django PROJECT

This contains:

- settings.py
- urls.py
- wsgi.py
- asgi.py

# ASGI vs WSGI
**Think of WSGI as a single-lane road.**

Only one request is handled at a time per worker.

Designed for synchronous (blocking) Python code.

✔️ Good for:

Classic web pages

REST APIs where each request is simple and blocking
(e.g., read from DB → return JSON)

**Think of ASGI as a multi-lane highway.**

Can handle many requests at the same time efficiently.

Supports both:

- Synchronous code
- Asynchronous code (async/await)
- Supports modern features like:
- WebSockets (real-time chat, notifications)
- Background tasks

**Django keeps both ASGI and WSGI on purpose** Think of them like two different power outlets, So can you ignore WSGI and use only ASGI but don't delete wsgi.py even if you don’t use it, Django itself expects the file to exist, and some tools (e.g., gunicorn users, old extensions) reference it. It’s harmless and tiny — leave it there.
