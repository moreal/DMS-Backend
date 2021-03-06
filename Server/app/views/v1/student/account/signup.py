from binascii import hexlify
from datetime import datetime
from hashlib import pbkdf2_hmac

from flask import Blueprint, Response, current_app, request
from flask_restful import Api


from app.models.account import SignupWaitingModel, StudentModel, AdminModel
from app.models.apply import GoingoutApplyModel, StayApplyModel


from app.views.v1 import BaseResource

api = Api(Blueprint('student-signup-api', __name__))


@api.resource('/verify/id')
class IDVerification(BaseResource):
    
    def post(self):
        """
        ID 중복체크
        """
        id = request.form['id']

        student = StudentModel.objects(id=id).first()
        admin = AdminModel.objects(id=id).first()
        if any((student, admin)):
            # ID already exists
            return Response('', 204)
        else:
            return Response('', 200)


@api.resource('/verify/uuid')
class UUIDVerification(BaseResource):
    
    def post(self):
        """
        UUID에 대한 가입 가능 여부 검사
        """
        uuid = request.form['uuid']

        signup_waiting = SignupWaitingModel.objects(uuid=uuid)
        if signup_waiting:
            # Signup available
            return Response('', 200)
        else:
            return Response('', 204)


@api.resource('/signup')
class Signup(BaseResource):
    
    def post(self):
        """
        회원가입
        API 내부에서 한 번 더 ID 중복체크와 UUID 가입 가능 여부를 검사함
        """
        uuid = request.form['uuid']
        id = request.form['id']
        pw = request.form['pw']

        signup_waiting = SignupWaitingModel.objects(uuid=uuid).first()
        student = StudentModel.objects(id=id).first()
        # To validate

        if not signup_waiting:
            # Signup unavailable
            return Response('', 205)

        if student:
            # Already signed
            return Response('', 204)

        # --- Create new student account_admin

        name = signup_waiting.name
        number = signup_waiting.number

        signup_waiting.delete()

        pw = hexlify(pbkdf2_hmac(
            hash_name='sha256',
            password=pw.encode(),
            salt=current_app.secret_key.encode(),
            iterations=100000
        )).decode('utf-8')
        # pbkdf2_hmac hash with salt(secret key) and 100000 iteration

        StudentModel(
            id=id,
            pw=pw,
            name=name,
            number=number,
            signup_time=datetime.now(),
            goingout_apply=GoingoutApplyModel(apply_date=datetime.now()),
            stay_apply=StayApplyModel(apply_date=datetime.now())
        ).save()

        return Response('', 201)
