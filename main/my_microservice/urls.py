from django.urls import include, path, re_path
from rest_framework import routers
from user import views as user_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from property.domain.views import ProductViewSet, CartViewSet

router = routers.DefaultRouter()
router.register(r"users", user_views.UserViewSet)
router.register(r"groups", user_views.GroupViewSet)

product_router = routers.DefaultRouter()
product_router.register(r'product', ProductViewSet)
cart_router = routers.DefaultRouter()
cart_router.register(r'carts', CartViewSet, basename='cart')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

schema_view = get_schema_view(
    openapi.Info(
        title="Django Property",
        default_version="v1",
        description="API Docs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="abubakersuliman@outlook.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Auth-User app
    path("auth/", include(router.urls)),
    path("product/", include(product_router.urls)),
    path('cart/', include(cart_router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Open API
    re_path(
        r"^$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    # Admin
    path("admin/", admin.site.urls),
    #   todo_app
    path("", include("property.urls")),
]
