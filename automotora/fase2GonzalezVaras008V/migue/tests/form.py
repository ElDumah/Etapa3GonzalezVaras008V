from django.test import SimpleTestCase
from budget.forms import ExpenseForm




class  testForms(SimpleTestCase ):

     def Text_form_dato_valido(self):
         form = ExpenseForm(data={
         'title': ''
         'model':''
         'category':''
         })

      self.assertTrue(form.is_valido())

      def text_expense_form_no_dato(self())
      form= ExpenseForm(dato={})

      self.assertFalse(form.is_valido())
      self.assertEquials(len(form.errors),3)
