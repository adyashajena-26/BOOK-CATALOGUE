from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book
import requests
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
def profile_view(request):
    if request.user.is_authenticated:

        return render(request,'pages/profile.html')
    else:
       
        return redirect('login')
    
def bookSearch_view(request):
    print(request.method)
    if request.user.is_authenticated:
        form = BookForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                isbn = form.cleaned_data.get('ISBN')
                reqUrl = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'+str(isbn)
                details = requests.request('GET', reqUrl)

                print(details.json())

                print(isbn)
            else:
                print('form is not valid')
        context={
            'form':form,
        }
        return render(request,'pages/bookSearch.html',context=context)
    else:
        return redirect('login')


def showBook_view(request):
    if request.user.is_authenticated:
        form = BookForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                isbn = form.cleaned_data.get('ISBN')
                reqUrl = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'+str(isbn)
                details = requests.request('GET', reqUrl)
                data = details.json()
                number_of_books = data['totalItems']
                books=[]
                for i in range(0,number_of_books):
                    book_dict={}
                    volume_info=data['items'][i]['volumeInfo']
                    if 'title' in volume_info:
                        book_dict['title']=volume_info['title']
                    else:
                        book_dict['title']='No Title Available'
                    if 'authors' in volume_info:
                        book_dict['authors']=volume_info['authors']
                    else:
                        book_dict['authors']='No Author Available'
                    if 'pageCount' in volume_info:
                        book_dict['pageCount']=volume_info['pageCount']
                    else:
                        book_dict['pageCount']='Page count not Available'
                    if 'averageRating' in volume_info:
                        book_dict['averageRating']=volume_info['averageRating']
                    else:
                        book_dict['averageRating']='Rating not Available'
                    if 'imageLinks' in volume_info:
                        book_dict['imageLinks']=volume_info['imageLinks']['thumbnail']
                    else:
                        book_dict['imageLinks']='No Image Available'
                    books.append(book_dict)
                    context={
                        'number_of_books':number_of_books,
                        'books':books,
                    }
            else:
                return HttpResponse('Error')
                

        return render(request,'pages/selectBook.html',context=context)
    else:
        return redirect('login')
def addBook_view(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            book_info = request.GET
            book_data = book_info['data']
            book_index = int(book_info['index'])
            book_data = json.loads(book_data)
            book_data = book_data[book_index]
        
            bookobj = Book(title=book_data['title'],authors=','.join(book_data['authors']),pageCount=book_data['pageCount'],averageRating=book_data['averageRating'],imageLink=book_data['imageLinks'],user=request.user)
            bookobj.save()
            
            
            # book_dict = book_info.dict()
            # book_detail = book_dict['data']
            # book_index = book_dict['index'][0]
            # print(json.parse(book_detail))
            # book_info = eval(book_info)
            # print(type(book_info))
            # bookObj = Book(title=book_info['title'])
            # bookObj.save()
    
            return JsonResponse({'success':True})
        else:
            return HttpResponse('Error')
    else:
        return redirect('login')

def deleteBook(request,id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('profile')
    else:
        return redirect('login')
