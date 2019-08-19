from rest_framework import routers
from catalog.views import TaskViewSet # Import the view we just created

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
