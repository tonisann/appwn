from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

'''@app.get("/")
def read_root():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)'''


@app.get("/")
def root():
    return {"massaje": "Hello Yujin"}


@app.get("/about")
def about():
    return {"messeje": "how are you"}
