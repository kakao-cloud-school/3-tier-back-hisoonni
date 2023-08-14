from core import models
import traceback
import datetime
import json
from django.core import serializers
from core.utils import refiner


# 게시글 다중 조회
def select_utils_boad_list(
        page=None,
        page_size=None
):
    try:
        total_count = models.TbBoard.objects.count()
        tb_board_list = list(models.TbBoard.objects.all().order_by('-board_seq').values()
                             [(page -1) * page_size: (page -1) * page_size + page_size])

        return {
            'response_code' : True,
            'response_data' : {
                'tb_board_list' : refiner.result_query_refiner(tb_board_list),
                # 'tb_board_list' : tb_board_list,
                'total_count' : total_count,
            },
            'message': '성공적으로 조회되었습니다.'
        }
    except Exception:
        print(traceback.format_exc())
        return {
            'response_code' : False,
            'message' : '서버 에러'
        }


# 게시글 등록
def insert_utils_board(board_seq=None, board_title=None, board_content=None, board_writer=None):
    try:
        if not board_title:
            return {'response_code': False, 'message': '게시판 제목을 받지 못했습니다.'}
        if not board_content:
            return {'response_code': False, 'message': '게시판 내용을 받지 못했습니다.'}
        if not board_writer:
            return {'response_code': False, 'message': '게시판 작성자를 받지 못했습니다.'}
        
        if board_seq:
            pass
        else:
            seq = None
            try:
                seq = models.TbBoard.objects.latest('board_seq').board_seq + 1
            except models.TbBoard.DoesNotExist:
                seq = 1
                
            tb_board = models.TbBoard()
            tb_board.board_seq = seq
            tb_board.board_title = board_title
            tb_board.board_content = board_content
            tb_board.board_writer = board_writer
            tb_board.save()
        
        return {'response_code': True, 'message': '게시글이 저장되었습니다.'}
    except Exception:
        print(traceback.format_exc())
        return {'response_code': False, 'message': '서버 에러'}
