from fastapi import APIRouter, UploadFile, File
from fastapi.responses import Response
from src.core.storing import Storage

router = APIRouter()

@router.get("/clean")
def cleandb() -> dict:
    store = Storage(router.configuration)
    store.reset()
    store.reset_files()
    return {"success": True}

@router.post("/ddmodels")
def postddmodel(identifier: int, version: int, file: UploadFile = File(...)) -> dict:
    store = Storage(router.configuration)
    retval = store.postDDModel(identifier, version, file)
    return {"success": retval}

@router.get("/ddmodels", responses={200: {"content": {"application/x-binary": {}}}}, response_class=Response)
def getddmodel(identifier: int, version: int) -> dict:
    store = Storage(router.configuration)
    retval = store.getDDModel(identifier, version)
    return Response(retval, media_type="application/x-binary")

@router.post("/mbmodels")
def postmbmodel(identifier: int, version: int, file: UploadFile = File(...)) -> dict:
    store = Storage(router.configuration)
    retval = store.postMBModel(identifier, version, file)
    return {"success": retval}

@router.get("/mbmodels")
def getmbmodel(identifier: int, version: int) -> dict:
    store = Storage(router.configuration)
    retval = store.getMBModel(identifier, version)
    return { "success": retval is not None, "content": retval}

@router.post("/matforpat")
def postrepomodel(configuration_name: str, file: UploadFile = File(...)) -> dict:
    store = Storage(router.configuration)
    store.postImg(configuration_name, file)
    return {"success": True}
