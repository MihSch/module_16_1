from fastapi import FastAPI


app = FastAPI()









@app.get('/user/admin')
async def admin():
    return {"Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def user_id(user_id):
    return {f"Вы вошли как пользователь {user_id}"}

@app.get('/user')
async def user(username: str = 'miha', age: int = 99):
    return {f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get('/')
async def welcome(): #-> dict:
    return {'Главная страница'}

