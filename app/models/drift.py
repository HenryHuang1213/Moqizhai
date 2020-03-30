'''
    -*- coding: utf-8 -*- 
    Time : 2020/2/12 19:19 
    Author : HenryHuang
    File : drift.py 
    Software: PyCharm
'''
__author__ = 'HenryHuang'

from sqlalchemy import Column, Integer, String, SmallInteger

from app.libs.enum import PendingStatus
from app.models.base import Base


class Drift(Base):
    '''
        一次具体的交易信息
    '''

    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    # 赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    _pending = Column('pending', SmallInteger, default=1)

    @property
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self, status):
        self._pending = status.value




