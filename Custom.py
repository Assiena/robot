
from ast import keyword
from dbm.ndbm import library
from robot.libraries.BuiltIn  import BuiltIn
from robot.api.deco import library,keyword
@library
class Custom():

    def __init__(self):
      self.selLib= BuiltIn().get_library_instance("SeleniumLibrary")
      
    @keyword
    def  hello_world(self):
        print("hello")
        
    @keyword
    def add_items_to_cart_and_checkout(self,productsList):
         # ${elements}=  Get WebElements    css:.inventory_item_name
         productsTitles=self.selLib.get_webelements(" css:.inventory_item_name")
         for productsTitle in productsTitles:
             if  productsTitle.text  in productsList:
                 self.selLib.click_button("(//*[@class='pricebar'])["+str(i)+"]/button")
                   

             i = i + 1
     

             self.selLib.click_link("css:a.shopping_cart_link")
    
