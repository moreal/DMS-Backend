EXTENSION_GET = {
    'tags': ['신청'],
    'description': '연장신청 정보 조회',
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
            'description': '연장신청 정보 조회 성공',
            'examples': {
                'application/json': {
                    'class_num': 1,
                    'seat_num': 16
                }
            }
        },
        '204': {
            'description': '연장신청 정보 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

EXTENSION_POST = {
    'tags': ['신청'],
    'description': '''연장신청
    11시 연장 신청 가능 시간: 17:30 - 20:30
    12시 연장 신청 가능 시간: 17:30 - 22:00
    자리주인이 이미 있으면 reject
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
            'name': 'class_num',
            'description': '''
            연장 학습실 번호
            1: 가온실
            2: 나온실
            3: 다온실
            4: 라온실
            5: 3층 독서실
            6: 4층 독서실
            7: 5층 열린교실
            ''',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        {
            'name': 'seat_num',
            'description': '연장 학습실 자리 번호',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '연장신청 성공'
        },
        '204': {
            'description': '연장신청 실패(신청 가능 시간 아님)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

EXTENSION_DELETE = {
    'tags': ['신청'],
    'description': '''연장 신청 취소
    
    11시 연장 신청 취소 가능 시간: 17:30 - 20:30
    12시 연장 신청 취소 가능 시간: 17:30 - 22:00
    ''',
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
            'description': '연장신청 취소 성공'
        },
        '204': {
            'description': '연장신청 취소 실패(취소 가능 시간 아님)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

EXTENSION_MAP_GET = {
    'tags': ['신청'],
    'description': '''연장신청 지도 조회
    조회한 class에 신청이 되어있으면
    신청이 되어있는지와 신청이 되어있는 자리를 리스폰스
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
            'name': 'class_num',
            'description': '지도를 조회할 학습실 번호',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '지도 조회 성공',
            'examples': {
                'application/json(가온실)': {
                    'map': [
                        [1, 1, 1, 1, 1],
                        [1, 2, 0, 3, 4],
                        [5, 6, 0, '조민규', 8],
                        [9, 10, 0, 11, 12],
                        [13, 14, 0, 15, 16],
                        [17, 18, 0, 19, 20]
                    ],
                    'applied_this_class': True,
                    'applied_seat': 7
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
