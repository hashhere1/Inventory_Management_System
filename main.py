from fastapi import FastAPI
from routers import user,categories, suppliers, products, inventory, sales,authentication
from database import Base,engine
import uvicorn

app = FastAPI()

app.include_router(user.router)
app.include_router(categories.router)
app.include_router(suppliers.router)
app.include_router(products.router)
app.include_router(inventory.router)
app.include_router(authentication.router)
app.include_router(sales.router)
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)

