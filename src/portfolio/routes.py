from portfolio import views

routes = [
    ("GET", "/api/image/<image_id>", views.image.get),
    ("GET", "/api/images", views.image.list),
    ("POST", "/api/images", views.image.create),
    ("PATCH", "/api/images/<image_id>", views.image.update),
    ("GET", "/api/user/<user_id>", views.user.get),
    ("POST", "/api/user/login", views.user.login),
    ("GET", "/api/group/<group_id>", views.group.get),
    ("GET", "/api/groups", views.group.list),
    ("POST", "/api/groups", views.group.create),
    ("PATCH", "/api/group/<group_id>", views.group.update),
]
