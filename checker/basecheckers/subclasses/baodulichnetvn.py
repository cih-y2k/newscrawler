#!/usr/bin/python
# -*- coding: utf8 -*-

# Done
# Broken url (500)
from checker.basecheckers import *


class BaoDuLichNetVnChecker(BaseChecker):
    def __init__(self):
        # Bắt buộc phải gọi đầu tiên
        super().__init__()

        # Chứa tên miền không có http://www dùng cho parser tự động nhận dạng
        self._domain = 'baodulich.net.vn'

        # Custom các regex dùng để parse một số trang dùng subdomain (ví dụ: *.vnexpress.net)
        # self._domain_regex =

        # Biến vars có thể được sử dụng cho nhiều mục đích khác
        # self._vars[''] =