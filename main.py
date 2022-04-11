# run with $ uvicorn main:app --reload

from fastapi import FastAPI, Request, UploadFile, File, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List
from utils import save_file



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
# mount the uploads folder:
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

templates = Jinja2Templates(directory="templates")




@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})
    # return {"message": "Hello World"}

    

@app.get("/color-palette-extractor", response_class=HTMLResponse)
async def col_palette_extractor(request:Request):
    return templates.TemplateResponse("color_palette_extractor.html", {"request": request})

# @app.post("/imgs/upload", status_code=status.HTTP_201_CREATED)
@app.post("/imgs/upload", status_code=status.HTTP_200_OK)
async def imgs_upload(images: List[UploadFile] = File(...)):
    print("uploaded:")
    print(images)

    # TODO: give unique name!

    saved_images = []
    # TODO: check if file exists for success!!
    try:
        for file in images:
            contents = await file.read()
            save_file(file.filename, contents, folder="uploads")
            print("filename:", file.filename)
            saved_images.append({"id": file.filename, "originalName":file.filename, "url": file.filename})

        # return {"status":"success!", "data": [file.filename for file in images]}
        # return {"status":"success!", "data": {"uploadedFiles": [file.filename for file in images]}}
        return {"status":"success!", "data": saved_images}

    except:
        return {"status":"error!", "data": saved_images}




# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}