from portfolio import views

routes = [
    ("GET", "/api/image.get", views.image.get, ["read:db"]),
    ("GET", "/api/image.list", views.image.list, ["read:db"]),
]
