# ==========================================
# Test Case 1
# ==========================================
from django.test import TransactionTestCase
from polls.models import Question
from django.utils import timezone

class QuestionTransactionTests(TransactionTestCase):

    # ==========================================
    # Test Case 1 ~ Check Database Transaction
    # ==========================================
    def test_create_question_transaction(self):
        Question.objects.create(
            question_text = 'Transaction Test Question',
            pub_date = timezone.now()
        )

        self.assertEqual(Question.objects.count(), 1)