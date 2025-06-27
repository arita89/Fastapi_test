from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"msg": "Hello, FastAPI!"}

@app.get("/docs", include_in_schema=False)
def custom_swagger_ui():
    html_path = "static/custom_swagger.html"
    try:
        if os.path.exists(html_path):
            with open(html_path, encoding="utf-8") as f:
                html_content = f.read()
            return HTMLResponse(html_content)
        else:
            return RedirectResponse(url="/default-docs")
    except Exception:
        return RedirectResponse(url="/default-docs")

@app.get("/default-docs", include_in_schema=False)
def default_docs():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="FastAPI - Swagger UI"
    )
