from uuid import uuid4

from flask import Response
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity, jwt_refresh_token_required
from flask_restful import Resource, request
from flasgger import swag_from

# 여긴 문서의 경로가 들어갈 것이다.
from app.models.account import SignupWaitingModel, StudentModel, AdminModel


class AccountControl:
    @jwt_required
    def delete(self):
        """
        학생 계정 삭제
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        number = request.form['number']
        student = StudentModel.objects(
            number=number
        )

        if not student:
            return Response('', 204)

        name = student.name
        student.delete()

        SignupWaitingModel(
            uuid=uuid4(),
            name=name,
            number=number
        ).save()

        return Response('', 200)

    @jwt_required
    def get(self):
        """
        StudentWatingModel uuid 확인
        """
        admin = AdminModel.objects(
            id=get_jwt_identity()
        ).first()

        if not admin:
            return Response('', 403)

        number = request.form['number']
        sign_up = SignupWaitingModel.objects(
            number=number
        )

        if sign_up:
            return Response(sign_up.uuid, 200)
        else:
            return Response('', 204)
