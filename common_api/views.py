from django.http import JsonResponse

def get_books(request):
    books = [
        {'title': '책 이름 1', 'price': 20000, 'reviews': 120, 'rating': '★★★★☆'},
        {'title': '책 이름 2', 'price': 15000, 'reviews': 80, 'rating': '★★★★★'},
        {'title': '책 이름 3', 'price': 15000, 'reviews': 80, 'rating': '★★★★★'},
        {'title': '책 이름 4', 'price': 15000, 'reviews': 80, 'rating': '★★★★★'},
        {'title': '책 이름 5', 'price': 15000, 'reviews': 80, 'rating': '★★★★★'},
        {'title': '책 이름 6', 'price': 15000, 'reviews': 80, 'rating': '★★★★★'},
        {'title': '책 이름 7', 'price': 15000, 'reviews': 80, 'rating': '★★★★★'},
        {'title': '책 이름 8', 'price': 15000, 'reviews': 80, 'rating': '★★★★★'},
        {'title': '책 이름 9', 'price': 15000, 'reviews': 80, 'rating': '★★★★★'},
        {'title': '책 이름 10', 'price': 15000, 'reviews': 80, 'rating': '★★★★★'},
    ]
    return JsonResponse(books, safe=False)