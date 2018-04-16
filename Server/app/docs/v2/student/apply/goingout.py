GOINGOUT_GET = {
    'tags': ['신청'],
    'description': '외출신청 정보 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '외출신청 정보 조회 성공',
            'examples': {
                'application/json': {
                    'sat': True,
                    'sun': False
                }
            }
        },
        '204': {
            'description': '외출신청 정보 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

GOINGOUT_POST = {
    'tags': ['신청'],
    'description': '''외출신청
    신청 가능 시간: 월요일 - 금요일 22:00
    금요귀가, 토요귀가 시 외출 신청 불가능
    ''',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'sat',
            'description': '토요일 외출 여부',
            'in': 'json',
            'type': 'bool',
            'required': True
        },
        {
            'name': 'sun',
            'description': '일요일 외출 여부',
            'in': 'json',
            'type': 'bool',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '외출신청 성공'
        },
        '204': {
            'description': '외출신청 실패(신청 가능 시간 아님)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
