from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="NewStyleAPI")

categories = [
    {
        'id': 1, 'name': 'Пальто'
    },
    {
        'id': 2, 'name': 'Платья и Комбинизоны'
    },
    {
        'id': 3, 'name': 'Джемперы и Кардиганы'
    },
    {
        'id': 4, 'name': 'Джинсы'
    },
    {
        'id': 5, 'name': 'Брюки'
    },
    {
        'id': 6, 'name': 'Куртки'
    },
    {
        'id': 7, 'name': 'Купальники'
    },

]

items = [
    {'id': 1, 'name': 'Пуховик', 'category_id': 1},
    {'id': 2, 'name': 'Ветровка', 'category_id': 1}
]

@app.get("/categories")
def get_categoties():
    return categories
    

@app.get("/items")
def get_all_items():
    return items

