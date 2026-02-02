from fastapi import FastAPI
import uvicorn

from api import items, root


def main():
    app = FastAPI()
    app.include_router(root.router)
    app.include_router(items.router)
    uvicorn.run(app, host="127.0.0.1", port=8200)

if __name__ == "__main__":
    main()
