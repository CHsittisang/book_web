import uvicorn


if __name__ == '__main__':
    # uvicorn.run(app, host="0.0.0.0", port=80 ,debug=True)
    uvicorn.run("backend.main:app", host="localhost", port=8080, reload=True)