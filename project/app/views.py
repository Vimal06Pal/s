from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import View
from geopy.geocoders import Nominatim
from .helper import get_place, offer




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
    print(request.user)
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
        print(products)
    
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
    print(file)
    context3= {}
    # all_comments  =Comments.objects.filter(product = product)
    # context3 ={"all_comments":all_comments}
    # try:
    product_quantity = Cart.objects.filter(product = product, user = request.user)
    print(product_quantity)
    # except:
    #     pass
    context5 ={"product_quantity":product_quantity}
    # pincode = Pincode()
    pincode = Pincode.objects.get(user = request.user)
    print(pincode)
    context4 = {"pincode":pincode}
  
    context2 = {"demo":file}
    
    context = {"products":product}

    context1={}
    if request.user.is_anonymous:
        pass
    else:
        context1 = {"userr":request.user}
    
    return render(request,"app/see_product.html",{"c":[context,context1,context2,context3,context4,context5]})

# def addcomments(request):
#     if request.method =="POST":
#         print("+++++++++++++++++++++++++++")
#         name = request.POST.get('name')
#         # print(name)
#         print("-------------sdsh----------")
#         if request.user.is_anonymous:
#             return redirect("login")
#         else:
#             product = Product.objects.get(id = name)
#             comm = request.POST.get("comments")
#             # print(comm)
#             comment = Comments()
       
#             comment.body = request.POST['comments']
#             comment.user     = request.user
#             comment.product=product
    
#             comment.save()
#             return redirect("productview",name= product.name)
#     return render(request,"app/see_product.html")
    # return render(request,"app/base.html")

def check_pincode(request):
    if request.method =="POST":
        zipcode = request.POST.get('pincode')
        name = request.POST.get('name')
        
        # print(zipcode)

        place = get_place(zipcode)
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


import datetime
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
    now = datetime.datetime.now().strftime('%A')
    day  =offer(now)
    for k,v in day.items():
        category = k
        discount = v

    grand_total= 0
    for c in cart:
        
        # l.append(c.product.price)
        # l.append(c.quantity)
        if(c.product.category.name == k):
            discounted_price = ((c.product.price * discount)/100)
            price = c.product.price-discounted_price
            p = price * c.quantity
            grand_total = grand_total+p
            pass
        else:
            prices = c.product.price * c.quantity
            # price_quantity[c.product.id] = prices
            grand_total= grand_total+prices

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
