"""The main module of the project """

class Fields :
    """ The Supprted fields """
    fields = {
        'char' : "models.CharField(max_length=225)",
        'email' : "models.EmailField()",
        'text' : "models.TextField()",
        'image' : 'models.ImageField()',
        'int' : 'models.IntegerField()',
        'float' : 'models.FloatField()',
        'uuid' : 'models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)',
        'date' : 'models.DateField()',
        'time' : 'models.TimeField()',
        'datetime' : 'models.DateTimeField()',
    }

    def make_dj_field (self, field_type, field_name) :
        """
            make tie field for your django model
        """
        return f'{field_name} = {self.fields[field_type]}' if field_type in self.fields else None

    def get_supprted_fields (self) : 
        return self.fields.keys()
    
class ModelBuilder (Fields):
    """
        model builder for buliding django models with fields
    """
    dj_models = ""
    imports = [
        'from django.db import models'
    ]
    def __init__(self, app, model_name,has_uuid, fields) :
        """
            initilized the model and his fields
        """
        self.model_body = ""
        app_name = app
        model_name = model_name
        self.model_body += f"# model {model_name} in app {app_name}\n"
        self.model_body += f"class {model_name} (models.Model): \n"
        fields = [self.make_dj_field(field_type=i['type'],field_name=i['name']) for i in fields]
        if has_uuid :
            if 'import uuid' not in self.imports:
                self.imports.append("import uuid")
            uuid_field = self.make_dj_field(field_name='id',field_type='uuid')
            fields.insert(0,uuid_field)
        for field in fields :
            self.model_body += '    ' + field + '\n'
        self.model_body += '\n\n'
    def generate (self) :
        """
            collect the fields and make the django model
        """
        self.dj_models += '# import libs\n'
        for imp in self.imports :
            self.dj_models += imp + "\n"
        self.dj_models += "\n"
        self.dj_models += self.model_body
        return self.dj_models
    

# models = [
#     {
#         'app' : "users" ,
#         'model_name' : "User",
#         'has_uuid' : False,
#         'fields': [
#             {
#                 'name' : 'first_name',
#                 'type' : 'char',
#             },
#             {
#                 'name' : 'last_name',
#                 'type' : 'char',
#             },
#             {
#                 'name' : 'email',
#                 'type' : 'email',
#             },
#             {
#                 'name' : 'passowrd',
#                 'type' : 'char',
#             },
#         ] 
#     }
# ]

# m = ModelBuilder(models)

# print(m.generate())


# # import models
# from django.db import models

# # model User in app users
# class User :
#     first_name = models.CharField(max_length=225)
#     last_name = models.CharField(max_length=225)
#     email = models.EmailField()
#     passowrd = models.CharField(max_length=225)

