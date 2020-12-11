from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile




class ClienteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(Nombre='Esteban', Apellido='Varas', email='esteban@hotmail.com',
        ,Numero="+5693407668" ,Username='esteban', Password='1234',descripción='automiviles',web='www.autosmiguelitos',
        facebook='facebook.com', twitter='twitter.com', instagram='instragram.com'  )

    def test_Nombre_label(self):
        usuario=Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('Nombre').verbose_name
        self.assertEquals(field_label,'Nombre')

    def test_Apellido_label(self):
        usuario=Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('Apellido').verbose_name
        self.assertEquals(field_label,'Apellido')



    def test_Nombre_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('Nombre').max_length
        self.assertEquals(max_length,16)

    def test_Apellido_max_length(self):
        usuario=Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('Apellido').max_length
        self.assertEquals(max_length,16)

    def UserRegisterView(self):
        Nombre=Nombre.objects.get(id=1)
        max_length = usuario._meta.get_field('usuario').max_length
        Password_length = usuario._meta.get_field(Password).max_length
