import logging
import traceback
from django.db import IntegrityError
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from base import literals
from base.exceptions import InvalidKeyException
from base.models import Dictionary
from base.serializers import DictionarySerializer
from base.util.api_response import error_response, results_response
from base.util.trace_id_generator import write_debug


@api_view(['GET'])
def index(request):
    return Response(data="ok", status=status.HTTP_200_OK)


# @api_view(['GET', 'POST'])
# def manage_dictionary(request):
#     if request.method == 'POST':
#         try:
#             language = request.data['language']
#         except KeyError:
#             return Response(error_response("'language' key missing"),
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         dic = Dictionary(language=language, user=request.user)
#         dic.save()
#
#         return Response(data=language,
#                         status=status.HTTP_200_OK)
#
#     elif request.method == 'GET':
#         # dic = Dictionary(user=request.user)
#         dic = Dictionary.objects.filter(user=request.user)
#         dictionaries = DictionarySerializer(dic, many=True)
#
#         paginator = PageNumberPagination()
#         paginator.page_size = 5
#         result_page = paginator.paginate_queryset(dic, request)
#         serializer = DictionarySerializer(result_page, many=True)
#         return paginator.get_paginated_response(serializer.data)
#         # return Response(dictionaries.data,
#         #                 status=status.HTTP_200_OK)

class manage_dictionary(GenericAPIView):
    def post(self, request):

        write_debug("wololo")
        logger = logging.getLogger("__name__")

        logger.warning('tesetsetstestsetes ')
        if literals.LANGUAGE_KEY not in request.data:
            raise InvalidKeyException(f"Key should be named '{literals.LANGUAGE_KEY}'. Data received: {request.data}")

        language = request.data[literals.LANGUAGE_KEY]
        dictionaryModel = Dictionary(language=language, user=request.user)

        try:
            dictionaryModel.save()
        except IntegrityError:
            return Response(error_response(f"Language {language} already added"),
                            status=status.HTTP_409_CONFLICT)
        dictionaries = DictionarySerializer(dictionaryModel).data

        return Response(dictionaries,
                        status=status.HTTP_200_OK)

    def get(self, request):
        dic = Dictionary.objects.filter(user=request.user)
        dictionaries = DictionarySerializer(dic, many=True).data
        #
        # paginator = PageNumberPagination()
        # paginator.page_size = 5
        # result_page = paginator.paginate_queryset(dic, request)
        # serializer = DictionarySerializer(result_page, many=True)
        # return paginator.get_paginated_response(serializer.data)
        # return Response(dictionaries.data,
        #                 status=status.HTTP_200_OK)
        return self.get_paginated_response(self.paginate_queryset(dictionaries))
