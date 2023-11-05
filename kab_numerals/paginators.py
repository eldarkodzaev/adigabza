from django.core.paginator import Paginator, InvalidPage


class NumeralsPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except InvalidPage:
            if int(number) > 1:
                return self.num_pages
            return 1
