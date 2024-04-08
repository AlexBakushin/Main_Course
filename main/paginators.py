from rest_framework.pagination import PageNumberPagination


class BasePaginator(PageNumberPagination):
    """
    Пагинатор по умолчанию
    """
    page_size = 10

