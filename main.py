from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os
from fastapi.openapi.docs import get_swagger_ui_html

from fastapi import HTTPException

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"msg": "Hello, FastAPI!"}


@app.get("/fail")
def fail():
    raise HTTPException(status_code=400, detail="This always fails")


@app.get("/docs", include_in_schema=False)
def custom_swagger_ui():
    html_path = "static/custom_swagger.html"
    print(f"Looking for custom Swagger UI at {html_path}")
    try:
        if os.path.exists(html_path):
            print(f"Loading custom Swagger UI from {html_path}")
            with open(html_path, encoding="utf-8") as f:
                html_content = f.read()
            return HTMLResponse(html_content)
        else:
            print(
                f"Custom Swagger UI not found at {html_path}, redirecting to default docs"
            )
            return RedirectResponse(url="/default-docs")
    except Exception:
        print(
            f"Excetion occurred while loading custom Swagger UI, redirecting to default docs"
        )
        return RedirectResponse(url="/default-docs")


@app.get("/default-docs", include_in_schema=False)
def default_docs():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url, title="FastAPI - Swagger UI"
    )


print("Routes loaded:")
for route in app.routes:
    print(route.path)
