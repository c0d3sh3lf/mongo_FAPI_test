import uvicorn

def main():
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True, log_level="debug", workers=4)

if __name__ == "__main__":
    main()