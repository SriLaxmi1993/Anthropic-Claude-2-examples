import streamlit as st
import anthropic

def main():
    st.title("Mood Analyzer")

    # Get the API key from the user
    api_key = st.text_input("Enter your Anthropic API Key:", type="password")

    if api_key:
        # Create the Anthropic client
        client = anthropic.Anthropic(api_key=api_key)

        # Get user input
        user_input = st.text_area("Enter your thoughts or feelings for the day:")

        if st.button("Analyze Mood"):
            message = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=689,
                temperature=0,
                messages=[
                    {"role": "user", "content": f"Based on the following text, can you analyze the overall mood or sentiment expressed by the person?\n\n{user_input}"}
                ]
            )
            mood_analysis = message.content

            # Display the mood analysis
            st.write("**Mood Analysis:**")
            st.write(mood_analysis)

            # Define mood categories
            mood_categories = ["Happy", "Sad", "Angry", "Anxious", "Neutral"]

            # Categorize the mood based on keywords or patterns
            mood_category = "Neutral"
            for category in mood_categories:
                if category.lower() in mood_analysis.lower():
                    mood_category = category
                    break

            st.write(f"**Mood Category:** {mood_category}")

            # Provide recommendations
            if mood_category != "Neutral":
                message = client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=689,
                    temperature=0,
                    messages=[
                        {"role": "user", "content": f"Based on the mood analysis '{mood_analysis}' and the mood category '{mood_category}', can you provide some recommendations or suggestions to help the person feel better?"}
                    ]
                )
                recommendations = message.content

                st.write("**Recommendations:**")
                st.write(recommendations)

    else:
        st.warning("Please enter your Anthropic API Key to use the app.")

if __name__ == "__main__":
    main()