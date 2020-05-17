from django.shortcuts import render , redirect
from .models import DemoFormm
from .forms import CreateForm
from .slug import unique_slug_generator
from django.core.paginator import Paginator
from taggit.models import Tag
# Create your views here.

# 

def create_form(request):
	if request.method == 'POST' :
		form = CreateForm(request.POST , request.FILES)

		if form.is_valid():
			formobj = form.save(commit=False)
			slug = unique_slug_generator(formobj)
			formobj.slug = slug
			formobj.save()
			form.save_m2m()

			return redirect(detail_view , slug=slug)
				
	else:
		form = CreateForm()

	context = {
		'form' : form,
	}
	return render(request, 'form1.html' , context)


def list_view(request):
	obj_list = DemoFormm.objects.all()

	paginator = Paginator(obj_list, per_page=5)
	page_number = request.GET.get('page', 1)
	page_obj = paginator.get_page(page_number)
	common_tags = DemoFormm.tags.most_common()


	context =     {
	        'page_obj': page_obj,
	        'paginator': paginator,
	        'page_number': int(page_number),
	        'common_tags': common_tags,
	        
	    }
    

	return render(request , 'list.html' , context)

def tagged(request , slug):
	tag = Tag.objects.get(slug=slug)
	obj_list = DemoFormm.objects.filter(tags = tag)
	paginator = Paginator(obj_list, per_page=5)
	page_number = request.GET.get('page', 1)
	page_obj = paginator.get_page(page_number)
	common_tags = DemoFormm.tags.most_common()
	context =     {
	        'page_obj': page_obj, 
	        'paginator': paginator,
	        'page_number': int(page_number),
	        'common_tags': common_tags,  
	    }
    

	return render(request , 'list.html' , context)

def detail_view(request,slug):
	obj = DemoFormm.objects.get(slug=slug)
	return render(request , 'detail.html' , {'obj':obj})

def update_view(request,slug):
	obj = DemoFormm.objects.get(slug=slug)
	if request.method == 'POST':
		form = CreateForm(request.POST,request.FILES , instance=obj)
		if form.is_valid():
			form.save()
			form.save_m2m()
			return redirect(detail_view , slug=slug)
	else:
		form = CreateForm(instance=obj)
	return render(request , 'edit.html', {'form': form})


def delete_view(request,slug):
	obj = DemoFormm.objects.get(slug=slug)
	if request.method == 'POST':
		obj.delete()
		return redirect('list')
	return render(request , 'delete.html' , {'obj':obj
		})

