from portfolio import views

routes = [
    ("GET", "/image/<image_id>", views.image.get),
    ("GET", "/images", views.image.list),
    ("GET", "/user/<user_id>", views.user.get),
    ("POST", "/user/login", views.user.login),
]
