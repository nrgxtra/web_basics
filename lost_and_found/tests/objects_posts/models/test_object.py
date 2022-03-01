from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.models import Object


class TestObject(TestCase):
    def test_WhenWidthIsLessThan_3_expectToRaise(self):
        name = 'Object1'
        image = 'http://image.com'
        width = 2
        height = 1
        weight = 1.2

        obj = Object(
            name=name,
            image=image,
            width=width,
            height=height,
            weight=weight,
        )
        with self.assertRaises(ValidationError) as context:
            obj.full_clean()
            obj.save()
        self.assertIsNotNone(context.exception)

    def test_WhenWidthIsEqualTo_3_expectToDoNothing(self):
        name = 'Object1'
        image = 'http://image.com'
        width = 3
        height = 1
        weight = 1.2

        obj = Object(
            name=name,
            image=image,
            width=width,
            height=height,
            weight=weight,
        )

        obj.full_clean()
        obj.save()

    def test_WhenWidthIsEqualTo_600_expectToDoNothing(self):
        name = 'Object1'
        image = 'http://image.com'
        width = 600
        height = 1
        weight = 1.2

        obj = Object(
            name=name,
            image=image,
            width=width,
            height=height,
            weight=weight,
        )

        obj.full_clean()
        obj.save()

    def test_WhenWidthIsMoreThan_600_expectToRaise(self):
        name = 'Object1'
        image = 'http://image.com'
        width = 601
        height = 1
        weight = 1.2

        obj = Object(
            name=name,
            image=image,
            width=width,
            height=height,
            weight=weight,
        )
        with self.assertRaises(ValidationError) as context:
            obj.full_clean()
            obj.save()
        self.assertIsNotNone(context.exception)

    def test_WhenWidthIsBetween3AndT600_expectToDoNothing(self):
        name = 'Object1'
        image = 'http://image.com'
        width = 500
        height = 1
        weight = 1.2

        obj = Object(
            name=name,
            image=image,
            width=width,
            height=height,
            weight=weight,
        )

        obj.full_clean()
        obj.save()
