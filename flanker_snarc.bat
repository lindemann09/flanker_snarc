if not exist "venv\" (
    python -m venv venv
)

call venv\Scripts\activate
python -m pip install expyriment

python flanker_snarc.py
