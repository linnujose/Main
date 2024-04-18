
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static  import static
from .views import remove_from_cart  # Import the remove_from_cart view
from .views import view_cart  # Import the view_cart function
from .views import increase_cart_item  # Import the increase_cart_item function
from .views import decrease_cart_item  # Import the decrease_cart_item function
from .views import fetch_cart_count

# from .views import chatgpt, generate_response







urlpatterns = [
   path('',views.index,name="index"),
   
   path('login/',views.login,name="login"),
   path('register/',views.register,name="register"),
   path('logout/',views.logout_view,name="logout"),
   path('userhome/',views.userhome,name="userhome"),
   path('sellerreg/',views.sellerreg,name="sellerreg"),
   path('sellerhome/',views.sellerhome,name="sellerhome"),
   path('add_product/',views.add_product,name="add_product"),
   path('view_product/',views.view_product,name="view_product"),
   path('product_list/',views.product_list,name="product_list"),
   path('product_list/<slug:category_slug>/', views.product_list, name='product_list_category'),
    path('product_list/<slug:category_slug>/<slug:subcategory_slug>/', views.product_list, name='product_list_subcategory'),

   #  path('increase_cart_item/<int:product_id>/', views.increase_cart_item, name='increase_cart_item'),
   #  path('decrease_cart_item/<int:product_id>/', views.decrease_cart_item, name='decrease_cart_item'),

   #  path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
   #  path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    



   path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
   path('deactivate_product/<int:product_id>/', views.deactivate_product, name='deactivate_product'),
   
   #linnus add to whislist and cart
   path('product/<int:product_id>/', views.product_details, name='product_details'),
   path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
   path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    
   path('cart/', views.cart, name='cart'),
   path('wishlist/', views.wishlist, name='wishlist'),
   path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
   path('userprofile/', views.userprofile, name='userprofile'),

   path('changepassword/', views.changepassword, name='changepassword'),
   path('shop/', views.shop, name='shop'),
   path('base/', views.base, name='base'),
   path('navbar/', views.navbar, name='navbar'),
   path('account/', views.account, name='account'),


   path('remove-from-cart/<int:product_id>/',views.remove_from_cart, name='remove-from-cart'),
   # path('cart/', view_cart, name='cart'),
   path('increase-cart-item/<int:product_id>/',views.increase_cart_item, name='increase-cart-item'),
    path('decrease-cart-item/<int:product_id>/',views.decrease_cart_item, name='decrease-cart-item'),
   path('fetch-cart-count/',views.fetch_cart_count, name='fetch-cart-count'),


   #userprofile
   path('save_profile/', views.save_profile, name='save_profile'),


   # userprofile
   # path('user_profile/', views.user_profile, name='user_profile'),


   #payment
   # path('checkout/', views.checkout, name='checkout'),

   path('fetch-cart-count/',views.fetch_cart_count, name='fetch-cart-count'),
   path('create-order/', views.create_order, name='create-order'),
   path('handle-payment/',views.handle_payment, name='handle-payment'),
   path('checkout/',views.checkout, name='checkout'),


   #billinvoice
   # path('billinvoice/', views.bill_invoice, name='bill_invoice'),
   path('billinvoice/', views.bill_invoice, name='bill_invoice'),




   path('adminpanal/', views.adminpanal, name='adminpanal'),
   path('adminpanal/registerduser/', views.registerduser, name='registerduser'),
   path('adminpanal/orderview/', views.orderview, name='orderview'),
   path('adminpanal/adminproduct/', views.adminproduct, name='adminproduct'),
   path('adminpanal/orderview/assignorder', views.assignorder, name='assignorder'),
   
   
# delivery agent
   path('deliveryhome/', views.deliveryhome, name='deliveryhome'),
   path('deliveryorder/', views.deliveryorder, name='deliveryorder'),
   # path('order/<int:order_id>/', order_detail, name='order_detail'),
   path('deliverynav/', views.deliverynav, name='deliverynav'),
   path('deliverynavbar/', views.deliverynavbar, name='deliverynavbar'),
   path('deliveryappform/', views.deliveryappform, name='deliveryappform'),

   path('approval/', views.approval, name='approval'),
   path('approved_delivery_boy/', views.approved_delivery_boy, name='approved_delivery_boy'),
   path('approve/<int:application_id>/', views.approve_application, name='approve_application'),
   path('orderuserdetails/', views.orderuserdetails, name='orderuserdetails'),
   

   
   



# userdetails
   # path('userdetails/', views.userdetails, name='userdetails'),


   #chatgpt nrs

   # path('chatgpt/', chatgpt, name='chatgpt'),
   # path('generate-response/', generate_response, name='generate_response'),


   path('shopbyage/', views.shopbyage, name='shopbyage'),
   path('myorders/', views.my_orders, name='myorders'),
   path('order_details/', views.order_details, name='order_details'),
   path('order_details/<int:order_id>/', views.order_details, name='order_details'),

  
   
 
      # forgot password

   path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
   path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),



   #Delivery agent
   path('deliveryreg/',views.deliveryreg, name="deliveryreg"),
   path('deliveryhome/',views.deliveryhome, name="deliveryhome"),
   path('giftfinder/',views.giftfinder, name="giftfinder"),



   # recommendation 
   path('product-recommendations/', views.product_recommendations, name='product_recommendations'),
   path('product/<int:product_id>/', views.product_details, name='product_details'),


#gift registry
   path('gift_registry/',views.gift_registry, name="gift_registry"),


   # update status 
   path('update/<int:order_id>/', views.update_status, name='updatestatus'),


   path('rating/', views.rating, name='rating'),
   # path('submit_rating/', views.submit_rating, name='submit_rating'),
   # path('submit_rating/', views.submit_rating_view, name='submit_rating'),
   # path('submit-rating/', views.submit_rating, name='submit_rating'),


   





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
