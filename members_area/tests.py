from django.test import TestCase

import cloudinary
import cloudinary.uploader
import cloudinary.api


# Create your tests here.


class CloudinaryTestCase(TestCase):
    cloudinary.uploader.upload("dog.mp4",
                               folder="my_folder/my_sub_folder/",
                               public_id="my_dog",
                               overwrite=true,
                               notification_url="https://mysite.example.com/notify_endpoint",
                               resource_type="video")
