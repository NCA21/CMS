from django.test import TestCase
from records.models import It, Nit, Nurses

class ItTestCase(TestCase):
    def setUp(self):
        It.objects.create(ip_first="Martha", ip_last="Jefferson")
        It.objects.create(ip_first="Thomas", ip_last="Jefferson")

    def test_it_introduction(self):
        it1 = It.objects.get(ip_first = "Thomas")
        it2 = It.objects.get(ip_first = "Martha")
        self.assertEqual(it1.intro(), "Patient Thomas Jefferson")
        self.assertEqual(it2.intro(), "Patient Martha Jefferson")

class NitTestCase(TestCase):
    def setUp(self):
        Nit.objects.create(p_MRN=123, p_cg=180)
        Nit.objects.create(p_MRN=321, p_cg=170)

    def test_nit_introduction(self):
        nit1 = Nit.objects.get(p_MRN=123, p_cg=180)
        nit2 = Nit.objects.get(p_MRN=321, p_cg=170)
        self.assertEqual(nit1.stat(), "Patient 123 has stable BG of 180")
        self.assertEqual(nit2.stat(), "Patient 321 has stable BG of 170")

class NursesTestCase(TestCase):
    def setUp(self):
        Nurses.objects.create(n_last="Adams", n_UNIT=2)
        Nurses.objects.create(n_last="Hamilton", n_UNIT=3)

    def test_nurses_introduction(self):
        n1 = Nurses.objects.get(n_last="Adams")
        n2 = Nurses.objects.get(n_last = "Hamilton")
        self.assertEqual(n1.assign(), "Nurse Adams is staffing Unit 2")
        self.assertEqual(n2.assign(), "Nurse Hamilton is staffing Unit 3")
