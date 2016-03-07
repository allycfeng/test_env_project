from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
from contact.forms import ContactForm
from contact.forms import ContactForm

def home(request):
	if request.user.is_authenticated():
		success_message = False
		title = 'Welcome'
		my_user = request.user
		img_link = 'http://www.foodnavigator-usa.com/var/plain_site/storage/images/publications/food-beverage-nutrition/foodnavigator-usa.com/markets/us-organic-food-market-to-grow-14-from-2013-18/8668340-1-eng-GB/US-organic-food-market-to-grow-14-from-2013-18.jpg'
		form = ContactForm(request.POST or None)
		# the usage of None here, is to prevent first loading validation message

		if form.is_valid():
			#save data from form data directly 
			form.save()
			success_message = "Success from saved( sent)"
			##change fields  before save
			# new_contact = form.save(commit=False)
			# print new_contact
			# new_contact.name = "Justin Michel"
			# new_contact.save()

			##this will save data from form too, but quite messu
			#print request.POST
			#print form.cleaned_data['email']
			#new_contact = Contact.objects.create(email=email,....)

	else:
		title = 'Welcome'
		my_user = ''
		img_link = ''

	context = {'title':title, 
			'my_user':my_user, 
			'img_link':img_link,
			'form': form, 
			'success_message':success_message
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
