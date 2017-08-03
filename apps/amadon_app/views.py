from django.shortcuts import render, HttpResponse, redirect

context = {
  "items": [{'name': "Dojo Tshirt",'price': 19.99},
            {'name': "Dojo Sweater", 'price': 29.99},
            {'name': "Dojo Cup", 'price': 4.99},
            {'name': "Algorithim Book", 'price': 49.99}
            ]
}  # the index function is called when root is visited
def index(request):
  try:
    request.session['totalitems']
    request.session['totalamount']
  except:
    request.session['totalitems'] = 0
    request.session['totalamount'] = 0
  return render(request, "amadon_app/index.html", context)

def buy(request):
  for a_item in context['items']:
    if request.POST["name"] == a_item['name']:
      total = a_item['price'] * float(request.POST['quantity'])
      request.session['totalamount'] += total
      request.session['totalitems'] += int(request.POST['quantity'])
      request.session['itemcost'] = a_item['price']

  return redirect('/checkout')

def checkout(request):
  return render(request, 'amadon_app/indexCheckout.html')

def clear(request):
  request.session['totalamount'] = 0
  request.session['totalitems'] = 0
  request.session['itemcost'] = 0
  return redirect('/')
# Create your views here.
