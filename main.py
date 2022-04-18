# run with $ uvicorn main:app --reload

from fastapi import FastAPI, Request, UploadFile, File, status, Body
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List
from utils import save_file
# from color_palette import extractColorPaletteFromImg
from pydantic import BaseModel
from typing import Optional
import time
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
# mount the uploads folder:
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

templates = Jinja2Templates(directory="templates")


class ImgFile(BaseModel):
    id: str
    url: str
    originalName: Optional[str]
    filename: str
    folder:str


@app.post("/color-palette-extractor/perform")
def perform_extract_palette(data: ImgFile):

    # time.sleep(3) #wait 3 seconds for image to save
    print("data:", data)
    img_src = data.url
    print("img src:", img_src)
    print("folder:", data.folder)

    try:
        print("img src:", img_src)
        # commented for now because sklearn does not work with deta cloud
        # colors = extractColorPaletteFromImg(data.folder + "/" + data.filename)
        colors = ["#FF0000", "#00FF00", "0000FF"]
        print("colors:", colors)
        return {"status":"success", "colors": colors}
    except:
        return {"status": "error"}


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
    folder = "uploads"
    print("uploaded:")
    print(images)

    # TODO: give unique name!

    saved_images = []
    # TODO: check if file exists for success!!
    try:
        for file in images:
            contents = await file.read()
            save_file(file.filename, contents, folder=folder)
            print("filename:", file.filename)
            saved_images.append({"id": file.filename, "originalName":file.filename, "url": file.filename, "filename": file.filename, "folder":folder})

        # return {"status":"success!", "data": [file.filename for file in images]}
        # return {"status":"success!", "data": {"uploadedFiles": [file.filename for file in images]}}
        return {"status":"success!", "data": saved_images}

    except:
        return {"status":"error!", "data": saved_images}


@app.get("/random-challenge", response_class=HTMLResponse)
async def random_challenge(request:Request):
    return templates.TemplateResponse("random_challenge.html", {"request": request})

@app.get("/generate-rand-challenge")
async def generate_rand_challenge():
    # TODO: make a singleton to load all the dataa about animals, environments etc and load only once.
    

    # TODO: more options
    all_environments = ["forest", "street", "theater", "planet", "space", "sea", "fantasy"]

    subject_types = ["animal", "object", "general"]
    subject_type=random.choice(subject_types)
    subject = "what you whish"

    if subject_type=="animal":
        try:
            f = open('challenges_data/animals_list.txt')
            all_animals = eval(f.read())
            f.close()
        except:
            # TODO: log instead of print
            print("!! animals list file does not exist or could not be loaded... Using the default animals list")
            all_animals = ["Dog", "Cat", "Alpaca", "Rabbit", "Turtle", "Giraffe", "Bug", "Bee", "Horse", "Lion", "Ox", "Owl"]
        subject = "a " + random.choice(all_animals).lower()

    elif subject_type=="object":
        try:
            f = open("challenges_data/objects_list.txt")
            all_objects = f.read().split("\n")
        except:
            all_objects = ["vase", "flower", "window", "clothes", "tree"]
        subject = "a " + random.choice(all_objects).lower()
    else:
        try:
            f = open("challenges_data/painting_subjects1.txt")
            painting_subjs1 = f.read().split("\n")
        except:
            painting_subjs1 = ["flowers in a vase", "astronauts", "spaceship", "your dreams"]
        subject = random.choice(painting_subjs1).lower()

    #TODO: more artistic styles maybe
    try:
        f = open("challenges_data/artistic_styles.txt")
        all_artistic_styles = f.read().split("\n")
        f.close()
    except:
        all_artistic_styles = ["realism", "impressionism", "abstractionism"]

    return {"subject": subject, "subject_type":subject_type, "environment": random.choice(all_environments).lower(), "style":random.choice(all_artistic_styles).lower()}


# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


@app.get("/random-img-inspiration", response_class=HTMLResponse)
async def col_palette_extractor(request:Request):
    return templates.TemplateResponse("random_img_inspiration.html", {"request": request})
