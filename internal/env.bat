
cd %~dp0
call conda env remove --name datavis
call conda env create -f env.yml --force
call conda activate datavis
pip install -U kaleido

