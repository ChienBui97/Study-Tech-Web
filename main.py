from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
app = FastAPI()
#Đọc dữ liệu và lưu dữ liệu vào file json giã lập database
DATA_TITLE = "data.json"

def loadData():
    with open(DATA_TITLE, "r") as f:
        return json.load(f)
def saveData(data):
    with open(DATA_TITLE,"w") as f:
        json.dump(data, f, indent=4)

#Tạo class Phone cho chức năng thêm sản phẩm
class Phone(BaseModel):
    id: int
    name: str
    price: int

#Học phương thức GET
@app.get("/")
def home():
    return {"message":"Server đang hoạt động"}

@app.get("/phones")
def getAllPhone():
    return loadData()

@app.get("/phones/{phone_id}")
def getPhoneByID(phone_id: int):
    for phone in loadData():
        if phone["id"] == phone_id:
            return phone
    raise HTTPException(status_code=404, detail=f"Sản phẩm có ID {phone_id} không tồn tại")

@app.get("/search")
def searchPhone(max_price: int):
    resulst = []
    for phone in loadData():
        if phone["price"] <= max_price:
            resulst.append(phone)
    return resulst

#Học phương thức POST
@app.post("/phones")
def addPhone(new_phone: Phone):
    currentPhone = loadData()
    currentPhone.append(new_phone.dict())
    saveData(currentPhone)
    return {"massege":"Đã thêm thành công "}

#Học phương thức DELETE
@app.get("/delete/{phone_id}")
def deletePhoneByID(phone_id: int):
    currentPhone = loadData()
    for index, phone in enumerate(currentPhone):
        if phone["id"] == phone_id:
            currentPhone.pop(index)
            saveData(currentPhone)
            return {"massege":f"Đã xóa thành công sản phẩm có id {phone_id}"}
    raise HTTPException(status_code=404, detail=f"Sản phẩm có ID{phone_id} không tồn tại")

#Học phương thức PUT
@app.put("/phones/{phone_id}")
def updatePhoneByID(phone_id:int, updatePhone: Phone):
    currentPhone = loadData()
    for index, phone in enumerate(currentPhone):
        if phone["id"] == phone_id:
            currentPhone[index] = updatePhone.dict()
            saveData(currentPhone)
            return {"massege":f"Đã cập nhật thành công sản phẩm có ID{phone_id}"}
    raise HTTPException(status_code=404, detail=f"Không tìm thấy sản phẩm có id{phone_id} để cập nhập")