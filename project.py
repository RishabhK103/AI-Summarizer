import speech_recognition as sr
import openai

openai.api_key = 'your_openai_api_key'

def speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
        audio = r.listen(source)
        print("Recognizing . . . . ", end="")

        try:
            print("You have said:\n" + r.recognize_google(audio))
            print("done\n")
        except Exception as e:
            print("Error: " + str(e))

        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

        global catext
        catext = r.recognize_google(audio)
        return catext

if __name__ == "__main__":
    speech()

prom = "summarize the following paragraph: "
text = prom + catext

response = openai.Completion.create(
  engine="davinci",
  prompt=text,
  max_tokens=100,
  temperature=0.3,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

# Extract the generated summary from the API response
summary = response.choices[0].text.strip()

# Print the summary
print("summary", summary)
