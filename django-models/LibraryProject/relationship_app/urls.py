from .views import admin_view, librarian_view, member_view
from django.urls import path
from . import views

urlpatterns = [
    # Existing URLs
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("login/", views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    # RBAC URLs
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]

urlpatterns += [
    path('admin-page/', admin_view, name='admin_page'),
    path('librarian-page/', librarian_view, name='librarian_page'),
    path('member-page/', member_view, name='member_page'),
]


