import os
from configs.config import Config_holder
if __name__ == "__main__":
    os.system("python -m uvicorn main:app --reload")