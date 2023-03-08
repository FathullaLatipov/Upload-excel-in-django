from django.contrib import admin
import pandas as pd
from api_exel.forms import ProductForm
from api_exel.models import MyModel


@admin.register(MyModel)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['name', 'price', 'image']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if 'excel_file' in request.FILES:
            # load the Excel file into a pandas dataframe
            df = pd.read_excel(request.FILES['excel_file'])

            # select only the 'name' and 'price' columns
            df = df[['name', 'price', 'image']]

            # save each row as a new Product object
            for _, row in df.iterrows():
                product = MyModel(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                )
                product.save()
