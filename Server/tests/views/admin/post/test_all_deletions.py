from app.models.post import FAQModel, NoticeModel, RuleModel

from tests.views import TCBase


class TestPostDelete(TCBase):
    """
    TC about all of post deletions

    This TC tests
        * DELETE /admin/faq
        * DELETE /admin/notice
        * DELETE /admin/rule
    """

    def setUp(self):
        """
        - Before Test

        Upload posts
        Get post ids
            * POST /admin/faq
            * POST /admin/notice
            * POST /admin/rule
        """
        TCBase.setUp(self)

        # ---

        resp = self.request(
            self.client.post,
            '/admin/faq',
            {'title': 'title', 'content': 'content'},
            self.admin_access_token
        )
        self.faq_id = self.get_response_data(resp)['id']

        resp = self.request(
            self.client.post,
            '/admin/notice',
            {'title': 'title', 'content': 'content'},
            self.admin_access_token
        )
        self.notice_id = self.get_response_data(resp)['id']

        resp = self.request(
            self.client.post,
            '/admin/rule',
            {'title': 'title', 'content': 'content'},
            self.admin_access_token
        )
        self.rule_id = self.get_response_data(resp)['id']

    def tearDown(self):
        """
        - After Test
        """
        FAQModel.objects.delete()
        NoticeModel.objects.delete()
        RuleModel.objects.delete()

        # ---

        TCBase.tearDown(self)

    def _test(self, post_id, post_type):
        """
        - Test
        Delete post with post_id, post_type
            * Validation
            (1) status code : 200
            (2) load post with modified post id
                * Validation
                1. status code: 204

        :param post_id: post id for modify
        :type post_id: str

        :param post_type: faq or notice or rule
        :type post_type: str
        """
        # -- Test --
        resp = self.request(
            self.client.delete,
            '/admin/{}'.format(post_type),
            {'id': post_id},
            self.admin_access_token
        )

        # (1)
        self.assertEqual(resp.status_code, 200)

        # (2)
        resp = self.request(
            self.client.get,
            '/{}/{}'.format(post_type, post_id)
        )

        # 1
        self.assertEqual(resp.status_code, 204)
        # -- Test --

    def test(self):
        """
        - Test
        Delete FAQ, notice, rule with self._test()

        - Exception Test
        None
        """
        # -- Test --
        self._test(self.faq_id, 'faq')
        self._test(self.notice_id, 'notice')
        self._test(self.rule_id, 'rule')
        # -- Test --
