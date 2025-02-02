from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer

class FAQAPIView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        for faq in faqs:
            faq.question = faq.get_translation(lang)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)
