from portfolio import views

routes = [
    ("GET", "/image/<image_id>", views.image.get),
    ("GET", "/images", views.image.list),
    ("POST", "/images", views.image.create),
    ("PATCH", "/images/<image_id>", views.image.update),
    ("GET", "/user/<user_id>", views.user.get),
    ("POST", "/user/login", views.user.login),
    ("GET", "/group/<group_id>", views.group.get),
    ("GET", "/groups", views.group.list),
    ("POST", "/groups", views.group.create),
    ("PATCH", "/group/<group_id>", views.group.update),
]
