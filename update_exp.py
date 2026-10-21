import os
from datetime import datetime

import requests

url = "https://raw.githubusercontent.com/lindemann09/flanker_snarc/refs/heads/flanker2/"
filename = "flanker_snarc2.py"

response = requests.get(f"{url}{filename}")

if os.path.exists(filename):
    timestamp = datetime.now().strftime("%m%d%H%M")
    os.rename(filename, f"{filename}.{timestamp}.bkp")

# Save the file
with open(filename, "wb") as file:
    file.write(response.content)


