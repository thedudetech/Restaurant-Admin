from . import models
from table import Table
from table.columns import Column

class ProductTable(Table):
    Product_Id = Column(field='id')
    Product_Name = Column(field='product_name')
    Descriptions = Column(field='product_details')
    Quantity = Column(field='product_quantity')
    Price = Column(field='product_price')
     
    class Meta:
        model = models.Products


