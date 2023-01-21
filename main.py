from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, JSONResponse, HTMLResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def func4():
    return FileResponse("public/index.html")


@app.get("/users/{id}")
def users(id):
    return {"user_id": id}


@app.get("/dowload")
def dowload():
    return FileResponse("public/index.html", filename="file001", media_type="application/octet-stream")


"""@app.get("/")
def func1():
    mestext1 = {"message": "Hello METANIT.COM"}
    json_data1 = jsonable_encoder(mestext1)
    return JSONResponse(content=json_data1, media_type="text/plain")  # {"message": "Hi Yugin23"}"""


@app.get("/q")
def finc2():
    return JSONResponse(content={"message": "hello word"})  # {"message": "hello word"}


@app.get("/w")
def func3():
    text1 = "hoololo relo olo"
    return Response(content=text1, media_type="text/plain")
