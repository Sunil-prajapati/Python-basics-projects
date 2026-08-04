from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# Create a directory to store uploaded files if it doesn't exist
UPLOAD_DIR = "uploaded_files"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Static File
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")

# Upload File Endpoint
@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    if not file.filename:
        raise HTTPException(status_code=400, detail="File not selected for upload")
    # Save the uploaded file to the specified directory
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"message": "File uploaded successfully", "filename": file.filename, "url": f"/files/{file.filename}"}

#GET File URL
@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File retrieved successfully", "filename": filename, "url": f"/files/{filename}"}