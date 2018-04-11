from flasgger import swag_from
from flask import Blueprint
from flask_restful import Api

from app.views.v1 import auth_required

from app.docs.v1.mixed.post.notice import *
from app.models.v2.post import NoticeModel
from app.views.v1.mixed.post import PostAPIResource

api = Api(Blueprint('notice-api', __name__))


@api.resource('/notice')
class NoticeList(PostAPIResource):
    @swag_from(NOTICE_LIST_GET)
    @auth_required
    def get(self):
        """
        공지사항 리스트 조회
        """
        return self.get_list_as_response(NoticeModel)


@api.resource('/notice/<post_id>')
class NoticeItem(PostAPIResource):
    @swag_from(NOTICE_ITEM_GET)
    @auth_required
    def get(self, post_id):
        """
        공지사항 내용 조회
        """
        return self.get_item_as_response(NoticeModel, post_id)