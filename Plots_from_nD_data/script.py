import os
from traceback import print_tb
import plotly.express as px
import pandas as pd
import plotly.io as pio
import shutil
from itertools import combinations
from tqdm import tqdm
def run():
    # Set default plot theme
    pio.templates.default = "seaborn"
    
    # Change directory
    try:
        os.chdir("Plots_from_nD_data")
    except:
        os.chdir("..")
        os.chdir("Plots_from_nD_data")
        pass
    
    # Clean previous outputs
    
    shutil.rmtree('output plots')
    # Remake file structure
    os.mkdir('output plots')
    os.mkdir('output plots/2D')
    os.mkdir('output plots/2D/html')
    os.mkdir('output plots/2D/image')
    os.mkdir('output plots/3D')
    os.mkdir('output plots/3D/html')
    os.mkdir('output plots/3D/image')
    
    
    assert len(os.listdir("input file")) <= 2, "Too many files in the input directory, please only place one file in at a time (excluding 'example.csv')"
    if len(os.listdir("input file")) == 2:
        assert "example.csv" in os.listdir("input file"), "Use only ONE input file at a time"
    for file in os.listdir("input file"):
        
        if file != "example.csv":
            data = pd.read_csv(os.path.join("input file",file),index_col=0)
            data_dict = data.to_dict()
            # 3D
            combs = list(combinations(data_dict,3))
            for ax in tqdm(combs,desc="3D Plots"):
                
                plot = px.scatter_3d(data,x=ax[0],y=ax[1],z=ax[2],text=data.axes[0])


                plot.update_layout(scene = dict(
                        xaxis = dict(
                            backgroundcolor="rgb(200, 200, 230)",
                            gridcolor="grey",
                            showbackground=False,
                            zerolinecolor="black",),
                        yaxis = dict(
                            backgroundcolor="rgb(200, 200, 230)",
                            gridcolor="grey",
                            showbackground=False,
                            zerolinecolor="black"),
                        zaxis = dict(
                            backgroundcolor="rgb(200, 200, 230)",
                            gridcolor="grey",
                            showbackground=False,
                            zerolinecolor="black",),),
                        
                        margin=dict(
                        r=10, l=10,
                        b=10, t=10)
                    )
                plot.update_traces(textposition='middle right')
                plot.write_html("output plots/3D/html/{}_vs_{}_vs_{}.html".format(ax[0],ax[1],ax[2]))
                plot.write_image("output plots/3D/image/{}_vs_{}_vs_{}.png".format(ax[0],ax[1],ax[2]))
                
            
            # 2D    
            combs = list(combinations(data_dict,2))
            for ax in tqdm(combs,desc="2D Plots"):
                
                plot = px.scatter(data,x=ax[0],y=ax[1],text=data.axes[0])

                plot.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey',zerolinecolor='black')
                plot.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey',zerolinecolor='black')
                plot.update_layout(
                        
                        
                        margin=dict(
                        r=10, l=10,
                        b=10, t=10)
                    )
                plot.update_traces(textposition='middle right')
                plot.write_html("output plots/2D/html/{}_vs_{}.html".format(ax[0],ax[1]))
                plot.write_image("output plots/2D/image/{}_vs_{}.png".format(ax[0],ax[1]))
                
    print("Results saved to 'output plots' folder")   
            
if __name__ == "__main__":
    run()