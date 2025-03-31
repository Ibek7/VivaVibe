<<<<<<< HEAD
# VivaVibe  
Instagram Account: [butterman_411](https://www.instagram.com/butterman_411/)  
<img src="https://firebasestorage.googleapis.com/v0/b/instagram-autobot-df35b.appspot.com/o/IMG_B108D631FF82-1.jpeg?alt=media&token=6ea618ae-b89a-4020-9636-8c74c14eed4b" alt="Screenshot of instagram page" width="370" height="700">

###

<img src="https://firebasestorage.googleapis.com/v0/b/instagram-autobot-df35b.appspot.com/o/IMG_F633978156DD-1.jpeg?alt=media&token=d97fc1ef-3562-4236-811b-c84156739314" alt="Screenshot of sample ig post" width="370" height="600">

## Purpose  
VivaVibe is a project built to generate and publish motivational posts on Instagram. While designed for motivational content, the framework is flexible enough to support any theme for creating an Instagram account via using different prompts.

## Overview  
The project is divided into two primary services: the post creation service, which uses OpenAI's ChatGPT and DALL-E models to generate captions, hashtags and images, and the post publishing service, which handles interactions with the Instagram account via the Facebook and Instagram Graph APIs. All post data is stored in Google Firebase database and storage. Additional services may be introduced as the project evolves and more features are added.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd AutoInspire-main
   ```

2. **Create and Activate a Virtual Environment (Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   If a `requirements.txt` file is present, run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the root directory of the project (where `main.py` is located) with the following content. Replace the placeholder values with your actual API keys and credentials:

   ```dotenv
   OPENAI_API_KEY=your_openai_api_key_here
   FIREBASE_CREDENTIALS=/path/to/your/firebaseServiceAccount.json
   INSTAGRAM_API_TOKEN=your_instagram_graph_api_token_here
   ```

5. **Running the Project:**

   Since VivaVibe is written in Python, there is no compilation step. Instead, run the project directly using the Python interpreter:

   ```bash
   python main.py
   ```

   This command will load your environment variables, initialize the required services (OpenAI, Firebase, and Instagram), generate a post, save it to Firebase, and publish it on Instagram.

## Development notes 
This project is still in development, and while the design isn't final, I’ve prioritized delivering a functional version first. Some aspects, such as file path management, absence of a dedicated logger for different logging priorities, and processes that could be run asynchronously, are still rough and will be refined over time. Since this is a personal project, it’s currently tailored to my own needs, but adjustments could be made later if it’s extended for broader use. My focus for now is tackling the most challenging and urgent requirements before refining other aspects.
=======
# VivaVibe
VivaVibe is a Python-based project that automates the creation and publication of motivational posts on Instagram. Leveraging OpenAI’s ChatGPT and DALL-E for content generation, Firebase for data storage, and the Instagram Graph API for publishing, VivaVibe offers a flexible framework for generating engaging social media content.
>>>>>>> 18a415f8ef9c7f836d4f382d9ac7e75f7809b8ac
