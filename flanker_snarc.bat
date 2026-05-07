if not exist "venv\" (
    python -m venv venv
)

call venv\Scripts\activate
python -m pip install expyriment requests

python flanker_snarc.py
