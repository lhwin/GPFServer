from OceanTide.cal.func_GLSY_ALT_AUX_YCZ_GDR_CAL import func_ycz_cal_pro
from OceanTide.match.func_GLSY_ALT_GDR_AUX_YCZ_MATCH import func_ycz_matching_pro

from SelfCross.cal.func_GLSY_ALT_AUX_Sat_GDR_CAL import func_self_cross_cal_pro
from SelfCross.match.func_GLSY_ALT_GDR_AUX_SAT_MATCH import func_self_cross_matching_pro

from StarCross.cal.func_GLSY_ALT_AUX_Sat_GDR_CAL import func_cross_cal_pro
from StarCross.match.func_GLSY_ALT_GDR_AUX_SAT_MATCH import func_cross_matching_pro

from DataOp.explorer import LocalDataExplorer
# from Sig0Cross.cal.func_GLSY_ALT_AUX_Sat_GDR_SIG0_CAL import func_cross_cal_pro

from fastapi import FastAPI
from config import *
import uvicorn
app = FastAPI()

@app.post("/data/discover")
def data_discover(item: DataDiscoverItem):
    satelite_dir = item.satelite_dir
    oceantide_dir = item.oceantide_dir
    LocalData = LocalDataExplorer(satelite_dir, oceantide_dir)
    return LocalData.discover_data()

@app.post("/selfcross/match")
def get_item(item: SelfCrossItem):
    res = func_self_cross_matching_pro(item)
    return res

@app.post("/selfcross/cal")
def get_item(item: SelfCrossItem):
    res = func_self_cross_cal_pro(item)
    return res

@app.post("/starcross/match")
def get_item(item: StarCrossItem):
    res = func_cross_matching_pro(item)
    return res

@app.post("/starcross/cal")
def get_item(item: StarCrossItem):
    res = func_cross_cal_pro(item)
    return res

@app.post("/oceantide/match")
def get_item(item: OceanTideItem):
    return func_ycz_matching_pro(item)

@app.post("/oceantide/cal")
def get_item(item: OceanTideItem):
    return func_ycz_cal_pro(item)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")