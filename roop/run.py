#!/usr/bin/env python3

from roop import core
import os
from fastapi import FastAPI, File, UploadFile
from typing import Union
from fastapi.responses import JSONResponse
import secrets
from tempfile import NamedTemporaryFile
import shutil
import logging

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/faceswap")
def faceswap(image: UploadFile = File(...), video: UploadFile = File(...)):
    try:
        unique_file_path = f"{secrets.token_hex(16)}.mp4"
        with NamedTemporaryFile(delete=False, suffix=".png") as temp_image, \
                NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            shutil.copyfileobj(image.file, temp_image)
            shutil.copyfileobj(video.file, temp_video)
            source_path = temp_image.name
            target_path = temp_video.name
            output_path = os.path.join(os.path.dirname(
                __file__), 'content', unique_file_path)
        core.run_api(source_path, target_path, output_path,
                     frame_processor=["face_swapper", "face_enhancer"])
        return JSONResponse(status_code=200, content={"message": "Success", "file": unique_file_path})
    except Exception as e:
        logging.error(e)
        return JSONResponse(status_code=400, content={"message": "Error in reading the files"})
