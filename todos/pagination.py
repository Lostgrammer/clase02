from rest_framework.pagination import PageNumberPagination

class StandardResultSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page/size'
    max_page_size = 100