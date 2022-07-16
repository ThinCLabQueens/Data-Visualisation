@ECHO OFF
REM setlocal enabledelayedexpansion
if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit 
cd ..
python data_vis.py  --file="Plots_from_nD_data.script"
