from django.contrib import admin
from django.urls import path
from .views.about import get_views_about
from .views.board import insert_board
from .views.board import select_board_list

urlpatterns = [
    path('about/', get_views_about),

    # 게시글 다중 조회
    path('selectBoardList/', select_board_list),

    # 게시글 한건 조회
    path('insertBoard/', insert_board),
]
