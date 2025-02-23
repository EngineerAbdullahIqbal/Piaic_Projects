from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


class AdvancedReviewChain(Flow):
    # Define the language model to use.
    model = "gemini/gemini-2.0-flash-exp"

    @start()
    def summarize_review(self):
        """
        Step 1: Summarize a detailed customer review into one sentence.
        """
        review = (
            "I visited your store last week and had a mixed experience. "
            "While the ambiance was fantastic and the staff were friendly, "
            "the product quality did not meet my expectations. "
            "The delivery was prompt, but the after-sales support left much to be desired. "
            "Overall, I believe there is room for improvement in several areas."
        )
        prompt = f"Summarize the following customer review in one sentence:\n\n{review}"
        response = completion(
            api_key=api_key,
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        summary = response['choices'][0]['message']['content'].strip()
        print(f"Review Summary: {summary}")
        return summary

    @listen('summarize_review')
    def extract_topics(self, summary):
        """
        Step 2: Extract key topics mentioned in the summary.
        """
        prompt = (
            f"Identify the main topics discussed in the summary below. "
            f"Focus on aspects such as service, product quality, ambiance, and support.\n\n{summary}"
        )
        response = completion(
            api_key=api_key,
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        topics = response['choices'][0]['message']['content'].strip()
        print(f"Extracted Topics: {topics}")
        return topics

    @listen('extract_topics')
    def analyze_sentiment(self, topics):
        """
        Step 3: Analyze the sentiment (positive, negative, or neutral) for each extracted topic.
        """
        prompt = (
            f"Given the following topics, provide a sentiment (positive, negative, or neutral) "
            f"for each, formatted as 'topic: sentiment'.\n\n{topics}"
        )
        response = completion(
            api_key=api_key,
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        sentiment_analysis = response['choices'][0]['message']['content'].strip()
        print(f"Sentiment Analysis: {sentiment_analysis}")
        return sentiment_analysis

    @listen('analyze_sentiment')
    def generate_recommendations(self, sentiment_analysis):
        """
        Step 4: Generate actionable recommendations based on the sentiment analysis.
        """
        prompt = (
            f"Based on the following sentiment analysis, suggest actionable recommendations "
            f"for improving customer satisfaction:\n\n{sentiment_analysis}"
        )
        response = completion(
            api_key=api_key,
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        recommendations = response['choices'][0]['message']['content'].strip()
        print(f"Recommendations: {recommendations}")
        return recommendations

def kickoff():
    chain = AdvancedReviewChain()
    chain.kickoff()

def plot():
    chain = AdvancedReviewChain()
    chain.plot()

if __name__ == "__main__":
    kickoff()
