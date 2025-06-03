import requests

# Черновик скрипта для отправки меню в систему Sodexo

url = "https://api-gdp.sodexonet.com/v2/data/push/menu"

# Заголовки запроса 
headers = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer <вставить токен>"  # TODO: вставить рабочий токен
}

# Здесь должен быть цикл загрузки CSV 
# TODO: реализовать чтение файла CSV с колонками:
# Menu_id, Date, Assortment, Receipe, Retail_Item, Retail_Price, Article, MenuPlan

# Пример структуры запроса (не используется):
# payload = {
#     "Menu_id": "...",
#     "Date": "...",
#     ...
# }

# for row in csv_data:
#     response = requests.post(url, headers=headers, json=row)
#     print(response.status_code)
