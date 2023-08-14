from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json

from hisoonni_back.utils.board import insert_utils_board
from hisoonni_back.utils.board import select_utils_boad_list


# 게시글 다건 조회
@csrf_exempt
def select_board_list(request):
    data = json.loads(request.body)
    return JsonResponse(
        data=select_utils_boad_list(
        page = data.get('page', None),
        page_size = data.get('page_size', None),
        )
    )



# 게시글 등록
@csrf_exempt
def insert_board(request):
    data = json.loads(request.body)
    return JsonResponse(
        data=insert_utils_board(
        board_seq=data.get('board_seq', None),
        board_title=data.get('board_title', None),
        board_content=data.get('board_content', None),
        board_writer=data.get('board_writer', None)
        )
    )