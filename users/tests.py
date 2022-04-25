from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTest(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('test1@gmail.com', 'username', 'firstname', 'password')
        self.assertEqual(super_user.email, 'test1@gmail.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        # self.assertEqual(super_user.password, 'password')
        self.assertEqual(super_user.is_superuser, True)
        self.assertEqual(super_user.is_staff, True)
        self.assertEqual(super_user.is_active, True)
        self.assertEqual(str(super_user), 'username')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(email='test1@gmail.com', user_name='username', first_name='firstname',
                                        password='password', is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(email='test1@gmail.com', user_name='username', first_name='firstname',
                                        password='password', is_staff=False)

    def test_new_user(self):
        db =get_user_model()
        user = db.objects.create_user('test1@gmail.com','username', 'firstname', 'password')
        self.assertEqual(user.email, 'test1@gmail.com')
        self.assertEqual(user.user_name, 'username')
        self.assertEqual(user.first_name, 'firstname')
        self.assertEqual(user.is_superuser, False)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_active, False)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='',user_name='username',first_name='firstname', password='password'
            )










