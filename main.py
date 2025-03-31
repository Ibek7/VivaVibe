import os
from dotenv import load_dotenv
from Utility.PostCreationService import PostCreationService
from Utility.PostPublishingService import PostPublishingService
import logging

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting AutoSpire")
    pCreate = PostCreationService()
    newPost = pCreate.createPost()
    pCreate.savePost(newPost)
    pPublish = PostPublishingService()
    pPublish.publishPost(newPost)