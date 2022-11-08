from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


try:
    external_data = {
        'id': 1,
        'signup_ts': 'broken',
        'friends': [1, 2, 3],
    }

    User(**external_data)

    user = User(**external_data)
except ValidationError as e:
    print(e.json(indent=4))
    print(e.errors())

# [Output]
# [
#     {
#         "loc": [
#             "signup_ts"
#         ],
#         "msg": "invalid datetime format",
#         "type": "value_error.datetime"
#     }
# ]
# [{'loc': ('signup_ts',), 'msg': 'invalid datetime format', 'type': 'value_error.datetime'}]