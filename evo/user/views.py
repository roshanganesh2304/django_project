from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic import CreateView,FormView,TemplateView,ListView,DetailView,DeleteView
from account.models import Products,Cart,Orders,Services,Scart,Status
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect('log')
    return inner

dec=[signin_required,never_cache]


@method_decorator(dec,name="dispatch")
class UserhomeView(TemplateView):
    template_name="uhome.html"

@method_decorator(dec,name="dispatch")
class SpareView(TemplateView):
    template_name="spares.html"

@method_decorator(dec,name="dispatch")
class ProductView(ListView):
    template_name="products.html"
    queryset=Products.objects.all()
    context_object_name="product"

    def get_context_data(self, **kwargs):
        res= super().get_context_data(**kwargs)
        print(res)
        res=Products.objects.filter(categories=self.kwargs.get('cat'))
        print(res)
        print(self.kwargs)
        return {"product":res}

@method_decorator(dec,name="dispatch")
class DetailsView(DetailView):
    template_name="details.html"
    queryset=Products.objects.all()
    pk_url_kwarg="did"
    context_object_name="product"


dec
def addtocart(request,*args,**kwargs):
    pid=kwargs.get('pid')
    pro=Products.objects.get(id=pid)
    user=request.user
    Cart.objects.create(product=pro,user=user)
    return redirect("uhome")

@method_decorator(dec,name="dispatch")        
class CartlistView(ListView):
    template_name="cartlist.html"
    queryset=Cart.objects.all()
    context_object_name="cart"

    def get_queryset(self):
        res=super().get_queryset()
        res=res.filter(user=self.request.user,status="added")
        return res

@method_decorator(dec,name="dispatch")
class CartdeleteView(DeleteView):
    model=Cart
    success_url=reverse_lazy('uhome')
    template_name="deletecart.html"
    pk_url_kwarg="cid"
    
@method_decorator(dec,name="dispatch")    
class PlaceorderView(TemplateView):
    template_name="placeorder.html"
    def post(self,request,*args,**kwargs):
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        cid=kwargs.get('cid')
        cart=Cart.objects.get(id=cid)
        product=cart.product
        user=request.user
        Orders.objects.create(product=product,user=user,address=address,phone=phone)
        cart.status="Order Placed"
        cart.save()
        return redirect('uhome')
    
@method_decorator(dec,name="dispatch")    
class OrderListView(ListView):
    template_name="orders.html"
    queryset=Orders.objects.all()
    context_object_name="orders"

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset=queryset.filter(user=self.request.user)
        return queryset
dec  
def cancelorder(request,**kwargs):
    iid=kwargs.get('iid')
    order=Orders.objects.get(id=iid)
    order.order_status="Cancelled"
    order.save()
    #mail service
    to_mail=request.user.email
    msg=f"Order for the request {order.product.title} is cancelled successfully!! Check your Evoindia account for more details"
    from_mail="illathh292@gmail.com"
    subject="Order Cancellation Confirmation"
    send_mail(subject,msg,from_mail,[to_mail])
    return redirect('order')

@method_decorator(dec,name="dispatch")
class ServiceView(TemplateView):
    template_name="service.html"

@method_decorator(dec,name="dispatch")
class CenterView(ListView):
    template_name="center.html"
    queryset=Services.objects.all()
    context_object_name="service"

    def get_context_data(self, **kwargs):
        res= super().get_context_data(**kwargs)
        res=Services.objects.filter(categories=self.kwargs.get('sat'))
        return {"service":res}

@method_decorator(dec,name="dispatch")
class SdetailsView(DetailView):
    template_name="sdetails.html"
    queryset=Services.objects.all()
    pk_url_kwarg="sid"
    context_object_name="product"

dec
def secart(request,*args,**kwargs):
    uid=kwargs.get('uid')
    ser=Services.objects.get(id=uid)
    user=request.user
    Scart.objects.create(name=ser,user=user)
    return redirect("uhome")

@method_decorator(dec,name="dispatch")
class SlistView(ListView):
    template_name="slist.html"
    queryset=Scart.objects.all()
    context_object_name="scart"

    def get_queryset(self):
        res=super().get_queryset()
        res=res.filter(user=self.request.user,status="added")
        return res


@method_decorator(dec,name="dispatch")
class ServicedeleteView(DeleteView):
    model=Scart
    success_url=reverse_lazy('uhome')
    template_name="serdelete.html"
    pk_url_kwarg="sid"


@method_decorator(dec,name="dispatch")
class PlaceserviceView(TemplateView):
    template_name="bookservice.html"
    def post(self,request,*args,**kwargs):
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        vid=kwargs.get('vid')
        cart=Scart.objects.get(id=vid)
        name=cart.name
        user=request.user
        Status.objects.create(name=name,user=user,address=address,phone=phone)
        cart.status="Service Booked"
        cart.save()
        return redirect('uhome')

@method_decorator(dec,name="dispatch")       
class ServicelistView(ListView):
    template_name="status.html"
    queryset=Status.objects.all()
    context_object_name="status"

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset=queryset.filter(user=self.request.user)
        return queryset

dec    
def cancelbook(request,**kwargs):
    bid=kwargs.get('bid')
    status=Status.objects.get(id=bid)
    status.order_status="Cancelled"
    status.save()
    to_mail=request.user.email
    msg=f"Your Service slot at {status.name.title} is cancelled succefully!! Check your Evoindia account for more details"
    from_mail="illathh292@gmail.com"
    subject="Service Cancellation"
    send_mail(subject,msg,from_mail,[to_mail])
    return redirect('uhome')

