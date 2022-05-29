# from urls import app
import uvicorn
import sys,os
sys.path.append(os.environ["COMMON_DIR"])

if __name__ == '__main__':
    uvicorn.run(app="app.main:app", host='0.0.0.0', port=3018,reload=True, access_log=True)