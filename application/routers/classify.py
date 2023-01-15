from fastapi import File, UploadFile,HTTPException
from fastapi.routing import APIRouter
from application.services.img_classify import ImgClassify
from application.utility.conversion import Conversion

img_classify = ImgClassify()
conversion = Conversion()

router = APIRouter(prefix='/img_classify')

@router.post("")
async def image_classification(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    img = await conversion.read_image(file)
    try:
        prediction = img_classify.color_classify(img)
        return {'prediction':prediction}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))