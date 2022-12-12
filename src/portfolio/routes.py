from portfolio import views

routes = [
    ("GET", "/api/image.get", views.image.get, ["read:db"]),
    ("GET", "/api/image.list", views.image.list, ["read:db"]),
    ("GET", "/api/user.get.<user_id>", views.user.get, ["read:db"]),
    ("POST", "/api/auth.login", views.user.login, ["read:db"]),
]
