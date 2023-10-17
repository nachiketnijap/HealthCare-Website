from django.shortcuts import render,get_object_or_404, redirect
from doctors.models import Doctor
from products.models import Product
from .forms import DealForm
from .models import Deal,CountDeals
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
# Create your views here.
def doctor_deal(request):
    doctors = Doctor.objects.all()
    products = Product.objects.all()
    users = User.objects.all()

    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        product_id = request.POST.get('product')
        quantity_ordered = request.POST.get('quantity')
        date = request.POST.get('date')
        entered_by_id = request.POST.get('entered_by')
        
        doc_name = Doctor.objects.get(id=doctor_id)
        product_id = Product.objects.get(id=product_id)
        entered_by = User.objects.get(id=entered_by_id)

        # if CountDeals.objects.filter(entered_by=entered_by).exists():
        #     add=0
        #     add=str(add)+quantity_ordered
        #     v=CountDeals.objects.filter(entered_by=entered_by).quantity_ordered
        #     op=add+v
        #     count=CountDeals(
        #         res=CountDeals.objects.filter(entered_by=entered_by).update(quantity_ordered=op),
                
        #     )
        #     count.save()
        # else:
        #     count=CountDeals(
        #         entered_by=entered_by,
        #         quantity_ordered=quantity_ordered,
        #     )
        #     count.save()


        deal = Deal(
            doc_name=doc_name,
            product_name=product_id,
            quantity_ordered=quantity_ordered,
            date=date,
            entered_by=entered_by
        )
        deal.save()
        messages.success(request, 'Successfull !')
        return redirect('deal_list')
    context = {'doctors': doctors, 'products': products, 'users':users}
    return render(request, 'deals/product_deals.html', context)    

@login_required(login_url='/')
def update_deal(request, pk):
    obj = Deal.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = DealForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deal Updated Successfully !')
            return redirect('deal_list')
    else:
        form = DealForm(instance=obj)
    
    context = {'form': form}
    return render(request, 'deals/form.html', context)

@login_required(login_url='/')
def deal_list(request):
    deals = Deal.objects.all()
    context = {'deals': deals}
    return render(request, 'deals/list.html', context)

@login_required(login_url='/')
def delete_deal(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    
    if request.method == 'POST':
        deal.delete()
        messages.success(request, 'Deal Deleted Successfully !')
        return redirect('deal_list')
        
    
    context = {'deals': deal}
    return render(request, 'deals/delete_deal.html', context)
