from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

class CustomerFeedbackChain(Flow):
    # Define the language model to use.
    model = "gemini/gemini-2.0-flash-exp"

    @start()
    def summarize_review(self):
        """
        Start the workflow by summarizing a detailed customer review.
        """
        review = (
            "I visited your store last week and had a mixed experience. "
            "While the ambiance was fantastic and the staff were friendly, "
            "the product quality did not meet my expectations. "
            "Overall, I left feeling a bit disappointed despite the good service."
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
    def analyze_sentiment(self, summary):
        """
        Analyze the sentiment of the summarized review.
        """
        prompt = (
            f"Based on this summary, determine if the overall sentiment is positive, "
            f"negative, or neutral:\n\n{summary}"
        )
        response = completion(
            api_key=api_key,
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        sentiment = response['choices'][0]['message']['content'].strip()
        print(f"Overall Sentiment: {sentiment}")
        return sentiment

def kickoff():
    chain = CustomerFeedbackChain()
    chain.kickoff()

def plot():
    chain = CustomerFeedbackChain()
    chain.plot()

if __name__ == "__main__":
    kickoff()
