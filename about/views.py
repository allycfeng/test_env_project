from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
from contact.forms import ContactForm
def home(request):
	if request.user.is_authenticated():
		#context = {'title':'Welcome', 'abc':request.user, 'img_link':'http://www.foodnavigator-usa.com/var/plain_site/storage/images/publications/food-beverage-nutrition/foodnavigator-usa.com/markets/us-organic-food-market-to-grow-14-from-2013-18/8668340-1-eng-GB/US-organic-food-market-to-grow-14-from-2013-18.jpg'}
		title = 'Welcome'
		my_user = request.user
		img_link = 'http://www.foodnavigator-usa.com/var/plain_site/storage/images/publications/food-beverage-nutrition/foodnavigator-usa.com/markets/us-organic-food-market-to-grow-14-from-2013-18/8668340-1-eng-GB/US-organic-food-market-to-grow-14-from-2013-18.jpg'
		form = ContactForm()
	else:
		title = 'Welcome'
		my_user = ''
		img_link = ''

	context = {'title':title, 
			'my_user':my_user, 
			'img_link':img_link,
			'form': form, 
		}
	return  render(request, 'home.html', context)


#form: METHOD=get, post, put, delete. ACTION= send to which urls

#method2: set local variables, and construct context at the end is better
# method1: locals() use local variables
	# return render(request, 'home.html', locals())


# virtually same result
# def home(request):
# 	context = {}
# 	print request
# 	return  render('home.html', context, context_instance=RequestContext(request))
