
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResumeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#router and register our ResumeViewSet
router = DefaultRouter()
router.register(r'resumes', ResumeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]

