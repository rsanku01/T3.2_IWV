import os
import pandas as pd
import matplotlib as plt
import numpy as np
from pathlib import Path

# vessel_data_dir = Path(os.path.abspath("..\..\InputData\Vessel_Data.xlsx").replace("\\", "/"))


vessel_data_dir = os.path.abspath("..\..\InputData")
print(vessel_data_dir)
vessel_data_ = os.path.join(vessel_data_dir, "Vessel_Data.xlsx")

print(vessel_data_)

df = pd.read_excel(vessel_data_, sheet_name="MOTOR VESSELS")  # "../../InputData/Vessel_Data.xlsx"/
print(df)

vessel_derived_dict = {
    "Wetted Surface Area": None,
    "Prismatic Coefficient": None,
    "Midship Coefficient": None,
    "Longitudinal Center of buo": None,
}

vessel_data = {
    "Ves_typ": None,  # Vessel type
    "L_oa": 2 * 40,  # Length Overall [m]
    "L_pp": None,  # Length between perpendiculars [m]
    "B": None,  # Breadth [m]
    "T": None,  # Design Draft [m]
    "sh": None,
    "V_s": None,  # Vessel speed [m/s]
    "C_B": None,  # Block Coefficient
}

prop_dat = {
    "d_prop": None,  # Propeller Diameter [m]
    "p_d": None,  # Pitch/Diameter ratio
    "no_props": None,
    "rpm": None,
    "hub_r": None,
    "t_prop": None,
    "c_prop": None,
    "EAR": None,
}

fairway_dat = {
    "h": None,  # Water depth [m]
    "W": None,  # Channel width [m]
}
