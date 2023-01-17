from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def func1():
    mestext1 = {"message": "Hello METANIT.COM"}
    json_data1 = jsonable_encoder(mestext1)
    return JSONResponse(content=json_data1, media_type="text/plain")  # {"message": "Hi Yugin23"}


@app.get("/q")
def finc2():
    return JSONResponse(content={"message": "hello word"})  # {"message": "hello word"}


@app.get("/w")
def func3():
    text1 = "hoololo relo olo"
    return Response(content=text1, media_type="text/plain")
