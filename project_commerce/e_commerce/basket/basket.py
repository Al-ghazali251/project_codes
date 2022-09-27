from store.models import Product
from decimal import Decimal


# For creating sessions



class Basket():
    '''
    A base Basket class , providing some default behaviours that can be inherited or overrided as necessary
    '''
    
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
            
        self.basket = basket
        
        
    def add(self,product, qty):
        '''
        Adding and updating  user basket sesssion data
        '''
        product_id = product.id
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
            
    
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}
        
        self.session.modified = True
        
    
    def __iter__(self):
        #This syntax will be used to collect  the product id in the session data and will be used to query the database and return the products needed
        
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()  # Copying the session data base to pass additional data
        
        for product in products:
            basket[str(product.id)]['product'] = product
            
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
            
        
        
        
        
        
        
        
    def __len__(self):
        # gets the basket data and counts the qty of item
        
        return sum(item['qty'] for item in self.basket.values())  # I never understand am sha
    
    
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
    
    
    def delete(self, product):
        #deleting item from session data by using the id 
        product_id = str(product)
        
        if product_id in self.basket:
            del self.basket[product_id]
            self.session.modified = True      
            
            
    def update(self,product, qty):
    # This is to delete item from session data
        product_id = str(product)
        qty = qty 
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty 
            self.session.modified = True
    
    
     
        