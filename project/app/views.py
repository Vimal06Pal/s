from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import View
from geopy.geocoders import Nominatim
from .helper import get_place, offer
from django.db.models import Q

import datetime




# Create your views here.

def index(request):
    return render(request,"app/base.html")

def get_image_to_text(upload_files):
    fs = FileSystemStorage()
    x=''
    for file in upload_files:
        file_name=fs.save(file.name,content=file)
        # print("ffffffffffffffffffffffffffffffff",file_name
        p =str(file_name)
        x = x+p
        x = x+'/'
    return(x)


def view_product(request):
    if request.method =="POST":
        name = request.POST["name"]
        price = request.POST['price']
        category = request.POST['category']
        description = request.POST['description']
        upload_file = request.FILES['document']
        # filenamename = request.POST.get("filename")
        upload_files = request.FILES.getlist("uploadfols")
        text_form = get_image_to_text(upload_files)

        # print(text_form)


        product = Product(name= name,price = price,category = Category.objects.get(name = category),description = description,image = upload_file,multiple_images = text_form)
        product.save()
        # .__dict__


    getall_category = Category.objects.all()
    context = {"getall_category":getall_category}
    return render(request,"app/upload_product.html",context)

def add_category(request):
    if request.method =="POST":
        category_item = request.POST["category"]
        category = Category(name = category_item)
        category.save()
        
        
    return(render(request,"app/add_category.html"))

def all_products(request):
    products=None
    # print(request.user)
    # print(products)
    categories = Category.get_all_categories()
    # print(categories)
    demo_list = []
    files = AddCarousel.objects.all()
    # print(files)
    for file in files:
        file =str(file).split('/')

        file = file[:len(file)-1]
        # print("____________",file)

        demo_list= demo_list+file
    categoryId=None

    now = datetime.datetime.now().strftime('%A')
    day  =offer(now)

    k=''
    for k,v in day.items():
        category = k
        discount = v
    # print(category,discount)
    try:
        print("===============try executring =============")
        category_offer = Category.objects.get(name = category)
        categoryid = (category_offer.id)

        product = Product.objects.get(category_id = categoryid)
        discounted = ((product.price * discount)/100)
        discounted_price = product.price - discounted
        product.offer_price = discounted_price

        # print(product)
        # for prod in product:
        product.offer = True
        product.save()
# Entry.objects.filter(~Q(id=3))

        other_product = Product.objects.filter(~Q(category_id =categoryid))
        # print(other_product)
        for other in other_product:
            other.offer = False
            other.offer_price = other.price
            other.save()
        


    except:
        print("===============except executring =============")

        pass

    try:
        categoryId = request.GET["category"]
        # print(categoryId)
    except:
        pass
    if categoryId:
        products = Product.get_products_by_category_id(categoryId)
        # print(products)
    else:
        products=Product.get_all_products()
        # print(products)
    
    if request.user.is_anonymous:
        context1= {}
    else:
        context1 = {"userr":request.user}

    context = {"products":products}
    context2 = {"images":demo_list}
    context3 = {"categories":categories}

    return render(request,"app/index.html",{"c":[context,context1,context2,context3]})
    # return render(request,"app/base.html")

def upload_multiImage(request):
    '''this function is used select mutiple file  simultanously ,
    saving the file in the media folder using the FileSystemStorage

    FileStorage helps in saving the image in the media file it also helps
     in managing the name of the repeated file
    
    to upload all the selecting file at once in the one row of the table
    file name should be converted in the string with and add "/" to  end of the every name
    
    Now save the file in the book table  '''
    x = ""
    if request.method =='POST':
        name = request.POST.get("filename")
        upload_file = request.FILES.getlist("uploadfols")
        fs = FileSystemStorage()

        for file in upload_file:
            file_name=fs.save(file.name,content=file)
            # print("ffffffffffffffffffffffffffffffff",file_name)


            p =str(file_name)
            x = x+p
            x = x+'/'

        get_images = AddCarousel.objects.all()
        print(get_images)
        carousel = get_images(name =x)
        # carousel = AddCarousel(name = x)
        carousel.save()
        # return redirect("show")


    
    return render(request,'app/upload_multiple_images.html')



def signup_handle(request):
    user = User()
    if request.method =="POST":
        print("--------------------------------")
        username = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("password")

        error_message = None

        if(not username):
            error_message = "username  Required !!"
        elif len(username)<4:
            error_message="username must be contain 5 character"
        else:
            pass

        try:
            User.objects.get(email = email)
            return redirect("/signup")
        except:

            if confirm == password:
                user  = User(username = username,email = email)
                user.set_password(password) # to set the password in the encrypted form

                # user.make_password(password)  for our own password
                # user.check_password(raw_password)

                user.save()
                print("data saved to db")
                return redirect("login")

    return render(request,"app/signup.html")




        
def login_handle(request):
    if request.method == "POST":
        usern = request.POST['name']
        # print(username)
        pswd  = request.POST['password']
        # email = request.POST["email"]

        # print(password)
        userr = User.objects.get(username = usern)
        print(userr)
        # print(user.password)
        
    
        # pwd = User.check_password(raw_password = password)
        # print("iiiiiiiiiiiiiiiiiiiiiiiiii",pwd)
        user = authenticate(username=usern,password = pswd)
        print("-------------------------",user)
        if user != None:
        #     print("---------------login successfully-----------------------------")
            login(request,user)
            return redirect('/allproduct')

        #     try:
        #         profile =Profile.objects.get(user = user)
        #         print("===========================",profile)
        #         return redirect("/showall")
        #     except:
        #         "Profile matching query does not exist."
        #         return redirect("profile")
        #     # return render(request,"blogapp/blog.html")
           
    return render(request,'app/signin.html')

def logoutUser(request):
    logout(request)
    # request.session.clear_expired()

    return redirect("login")

def productview(request,name):
    print(name,"======================")
    product = Product.objects.get(name=name)
    files = product.multiple_images
    file =str(files).split('/')
    file = file[:len(file)-1]
    # print(file)
    context3= {}
    all_comments  =Comments.objects.filter(product = product)
    context3 ={"all_comments":all_comments}

    all_rating = Rating.objects.filter(product = product)
    context6 = {"all_rating":all_rating} 
    # try:
    product_quantity = Cart.objects.filter(product = product, user = request.user)
    # print(product_quantity)
    # except:
    #     pass
    context5 ={"product_quantity":product_quantity}
    # pincode = Pincode()
    context4 ={}
    try:
        pincode = Pincode.objects.get(user = request.user)
        # print(pincode.address)
        context4 = {"pincode":pincode}
    except:
        pass
    print("===================")
    try:
        coupons = Coupon.objects.filter(category = product.category)
        context7 = {"coupons":coupons}
        print("coupon",coupons)
    except:
        pass
  
    context2 = {"demo":file}
    
    context = {"products":product}

    context1={}
    if request.user.is_anonymous:
        pass
    else:
        context1 = {"userr":request.user}
    
    return render(request,"app/see_product.html",{"c":[context,context1,context2,context3,context4,context5,context6,context7]})

def addcomments(request):
    if request.method =="POST":
        print("+++++++++++++++++++++++++++")
        name = request.POST.get('name')
        # print(name)
        print("-------------sdsh----------")
        if request.user.is_anonymous:
            return redirect("login")
        # elif request.user ==:
        #     pass
        else:
                # order = Order.objects.filter(user = request.user)
                # print(order[0].user)
            product = Product.objects.get(id = name)
            if Order.objects.filter(user = request.user) and Order.objects.filter(product_id = name):

                comm = request.POST.get("comments")
                print(comm)
                comment = Comments()
        
                comment.body = comm
                comment.order = Order.objects.filter(user = request.user)[0]
                comment.product=product
        
                comment.save()
            else:
                pass
            return redirect("productview",name= product.name)
    return render(request,"app/see_product.html")
    return render(request,"app/base.html")

def check_pincode(request):
    if request.method =="POST":
        zipcode = request.POST.get('pincode')
        name = request.POST.get('name')
        
        # print(zipcode)

        place = get_place(zipcode)
        if place != None:
            try:
                pincode = Pincode.objects.filter(user = request.user)
                pincode.delete()
            except:
                pass
            pincode = Pincode()
            pincode.address = place
            pincode.zipcode = zipcode
            pincode.user = request.user
            pincode.save()
            product = Product.objects.get(id = name)

            print("pincode saved to db============")
        else:
            try:
                pincode = Pincode.objects.filter(user = request.user)
                pincode.delete()
            except:
                pass
            # pincode = Pincode()
            # pincode.address = "Delivery not available"
            # pincode.zipcode = zipcode
            # pincode.user = request.user
            # pincode.save()
            product = Product.objects.get(id = name)
            pass
        return redirect("productview",name= product.name)

    return render(request,"app/see_product.html")
    


def add_to_cart(request):
    # usern  =request.user
    # user  =User.objects.get(username = usern)
    # if usern == user:
    if request.method =="POST":
        product_id = request.POST.get('name')
        # print(product_id)
        product = Product.objects.get(id = product_id)
        print(product.name)
        context={"product":product}
    context1={}
    if request.user.is_anonymous:
        pass
    else:
        context1 = {"userr":request.user}

    # cart = Cart()
    # cart = cart.objects.all()/

    try:
        cart = Cart.objects.get(product_id = product_id,user =request.user)
        # cart = Cart.objects.all()
        print("-----------Before--------------------",cart.quantity)

        cart.quantity = cart.quantity+1
        print("--------------After-----------------",cart.quantity)

        cart.save()
       
           
    except:
        print("except is working....")
        product = Product.objects.get(id = product_id)
        cart = Cart()

        cart.product = product
        cart.user = request.user
        cart.quantity = 1
        if cart.quantity == 0:
            print("quantity is 0 you can delete this product from cart")
        cart.save()
        
        # pass
    # cart.product = 

    # else:
    #     return(redirect('/signin'))
    return redirect("productview",name= product.name)


    # return(render(request,"app/item_added_cart.html",{"c":[context,context1]}))

    # pass


# print((now.strftime("%A"))=="Wednesday")
def cartpage(request,id):
    if request.method =="POST":
        product_id = request.POST.get('quantity')
        print(product_id)
        product = Product.objects.get(id = product_id)
        print(product.name)
        context={"product":product}
    cart = Cart.objects.filter(user = request.user)
    print("=============",cart)
    price_quantity={}
    # now = datetime.datetime.now().strftime('%A')
    # day  =offer(now)
    # print("============================day============================",day)
    # k=''
    # for k,v in day.items():
    #     category = k
    #     discount = v

    grand_total= 0
    for c in cart:
        
        # l.append(c.product.price)
        # l.append(c.quantity)
        # if(c.product.category.name == k):
        #   discounted_price = ((c.product.price * discount)/100)
        #     price = c.product.price-discounted_price  
        p = c.product.offer_price * c.quantity
        grand_total = grand_total+p
        pass
        # else:
        #     prices = c.product.price * c.quantity
        #     # price_quantity[c.product.id] = prices
        #     grand_total= grand_total+prices

        # print(c.product.price)
        # print(c.quantity)
    # print(price_quantity)
    # print(grand_total)
    context3 = {"grand_total":grand_total}
    context = {"cart":cart}
    context1={}
    if request.user.is_anonymous:
        pass
    else:
        context1 = {"userr":request.user}

    return render(request,"app/cartpage.html",{"c":[context,context1,context3]})

def quantity_add(request):
    return render(request,"app/base.html")

def add_item(request):
    if request.method =="POST":
        product_id = request.POST.get('name')
        print(product_id)

    quantity=add_items(product_id,request.user) 
    if quantity == "False":
        print("your cannot add product in your cart")
    else:
        print(quantity)  

    product = Product.objects.get(id = product_id)
    return redirect("productview",name= product.name)

    # return render(request,"app/base.html")

def remove_item(request):
    if request.method =="POST":
        product_id = request.POST.get('name')
        print(product_id)
    quantity=remove_items(product_id,request.user)  
    print(quantity) 

    product = Product.objects.get(id = product_id)
    return redirect("productview",name= product.name)
    # return render(request,"app/base.html")


def add_items(product_id,user):
    cart = Cart.objects.get(product_id = product_id,user =user)
        # cart = Cart.objects.all()
    print("-----------Before--------------------",cart.quantity)
    
    cart.quantity = cart.quantity+1
    print("--------------After-----------------",cart.quantity)
    if cart.quantity>2:
        return("False")
    else:

        cart.save()
        print((cart.product.price)*(cart.quantity))
        return(cart.quantity) 

def remove_items(product_id,user):
    cart = Cart.objects.get(product_id = product_id,user =user)
        # cart = Cart.objects.all()
    print("-----------Before--------------------",cart.quantity)

    cart.quantity = cart.quantity-1
   
    print("--------------After-----------------",cart.quantity)

    cart.save()
    if cart.quantity == 0:
        print("product is available for delete from th cart")
        cart.delete()
        cart.quantity = 0
    return(cart.quantity)  


def add_item_cart(request):
    if request.method =="POST":
        product_id = request.POST.get('name')
        print(product_id)

    quantity=add_items(product_id,request.user)  
    print(quantity) 
    usern = User.objects.get(username = request.user)
    print(usern.id)


    product = Product.objects.get(id = product_id)
    return redirect("cartpage",id=usern.id)
    return(render(request,"app/base.html"))
# 

def remove_item_cart(request):
    if request.method =="POST":
        product_id = request.POST.get('name')
        print("====================",product_id)
    quantity=remove_items(product_id,request.user)  
    print(quantity)
    usern = User.objects.get(username = request.user)


    product = Product.objects.get(id = product_id)
    return redirect("cartpage",id= usern.id)
    # return(render(request,"app/base.html"))

def checkout(request,id):
    address =request.POST.get("address")
    phone = request.POST.get("phone")
    # usern = request.user
    cart =Cart.objects.filter(user = request.user)
    # print(cart)
    print("---------------------------runninn")
    for item in cart:

        price = item.product.price
        order = Order()
        order.product = item.product
        order.user = request.user
        order.price = item.product.offer_price * item.quantity
        order.quantity = item.quantity
        order.address = address
        order.phone = phone
        order.save()
        cart = Cart.objects.get(product = item.product,user = request.user)
        cart.delete()

    order = Order.objects.filter(user = request.user) 
    context = {"order":order} 
       
    return render(request,"app/order.html",context)

def rating(request):
    if request.method =="POST":
        print("+++++++++++++++++++++++++++")
        name = request.POST.get("name")
        # print(name)
        print("-------------sdsh----------")
        if request.user.is_anonymous:
            return redirect("login")
        # elif request.user ==:
        #     pass
        else:
                # order = Order.objects.filter(user = request.user)
                # print(order[0].user)
            product = Product.objects.get(id = name)
            if Order.objects.filter(user = request.user) and Order.objects.filter(product_id = name):

                choice = request.POST.get("ratingname")
                print(choice)
                rating = Rating()
        
                rating.choice = choice
                rating.order = Order.objects.filter(user = request.user)[0]
                rating.product=product

                rating.save()
            else:
                pass
            return redirect("productview",name= product.name)
    return render(request,"app/see_product.html")
    # print(request.POST["ratingname"])
    # return render(request,"app/base.html")


def add_coupons(request):
    # print(request.POST)
    if request.method =="POST":
        coupon_offerd = request.POST["coupon_name"]
        print(coupon_offerd)
        category = request.POST['category']


        coupons = Coupon(coupon = coupon_offerd,category = Category.objects.get(name = category))
        coupons.save()
    
        # category = Category(name = category_item)
        # category.save()
    getall_category = Category.objects.all()
    context = {"getall_category":getall_category}
    return render(request,"app/coupon.html",context)

    # category = Category.objects.get(name = category)