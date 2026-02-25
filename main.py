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

@app.get("/categories/{cat_id}/items")
def get_item_by_category(cat_id: int):
    result = [item for item in items if item ["category_id"] == cat_id]
    if not result:
        raise HTTPException(status_code=404, detail="Данной категории нет!")
    return result