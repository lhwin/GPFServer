from pydantic import BaseModel
from typing import Optional

class DataDiscoverItem(BaseModel):
    satelite_dir: str
    oceantide_dir: str

class OceanTideItem(BaseModel):
    Sat_ID: str
    Data_version: str
    AUX_YCZ: Optional[str] = None
    Product_Type: str
    Start_date: str
    End_date: str

    Match_Data_Type: Optional[str] = None
    MSS_PATH: Optional[str] = None
    FES2014_PATH: Optional[str] = None
    order_id: Optional[str] = None
    input: str          # 主卫星输入目录
    input_AUX: Optional[str] = None      # 辅助验潮站输入目录
    output: Optional[str] = None
    outputFileType: Optional[str] = None
    proc_name: Optional[str] = None
    version: Optional[str] = None

class SelfCrossItem(BaseModel):
    Sat_ID: str
    Data_version: str
    Product_Type: str
    Start_date: str
    End_date: str
    Match_time: str
    Template_docx: str
    order_id: str
    input: str                          # 输入目录（NC/H5），单输入
    output: Optional[str] = None
    outputFileType: Optional[str] = None
    proc_name: Optional[str] = None
    version: Optional[str] = None
    Select_Area: Optional[str] = None
    distance_to_coast: Optional[int] = None
    ocean_depth: Optional[int] = None
    wind_speed: Optional[str] = None

class Sig0CrossItem(BaseModel):
    Sat_ID: str
    Data_version: str
    AUX_Sat: str
    Product_Type: str
    Start_date: str
    End_date: str
    Match_time: str
    Template_docx: str
    order_id: str
    input: str
    input_AUX: str
    output: Optional[str] = None
    outputFileType: Optional[str] = None
    proc_name: Optional[str] = None
    version: Optional[str] = None

class StarCrossItem(BaseModel):
    Sat_ID: str
    Data_version: str
    AUX_Sat: Optional[str]=None
    Product_Type: str
    Start_date: str
    End_date: str
    Match_time: str
    Template_docx: str
    order_id: str
    # 必填目录
    input: str        # 主卫星输入目录
    input_AUX: Optional[str]=None    # 辅助卫星输入目录
    # 添加可选字段
    Select_Area: Optional[str] = None
    distance_to_coast: Optional[int] = None
    ocean_depth: Optional[int] = None
    wind_speed: Optional[str] = None
    output: Optional[str] = None
    outputFileType: Optional[str] = None
    proc_name: Optional[str] = None
    version: Optional[str] = None
    Match_Data_Type: Optional[str] = None