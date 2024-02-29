from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class IndexView(APIView):
    permission_classes = (IsAuthenticated,)
    token_class = RefreshToken

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)

    def get(self, request):
        refresh_token = self.get_token(request.user)
        access_token = str(refresh_token.access_token)
        res = {"Refresh Token": str(refresh_token), 'Access Token': access_token}
        return Response(res, status=200)