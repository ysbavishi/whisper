import speech_recognition as sr
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder 
from langchain_community.llms import Ollama
import pyaudio
def talk_with_bot(data:str) -> str:
    llm = Ollama(
        model="llama3",
        base_url="http://localhost:11434"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
             (
                 "system"
                 """Your name is Optimus,
                 Always address me as Boss
                 You have 100 honesty, 90 sarcasm, 75 humour and 100 sincerity
                 Your job is to take notes and return them as markdown code blocks 
                 You are free to provide your insights, elaborate or summarize the notes
                 Do a sentmiental analysis on original notes
                 Wrap the markdown code block with =====================
                 Include your analysis and input outside markdown code block
                 """
             ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )
    chain = prompt | llm
    print("Starting question boss")
    response = chain.invoke({"messages": [HumanMessage(content=f"{data}")]})
    print(response)
    return ""
def summary(data:str) -> str:
    llm = Ollama(
        model="llama3",
        base_url="http://localhost:11434"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
             (
                 "system"
                 "Get me the summary and your inputs from the following :- "
             ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )
    chain = prompt | llm
    print("Starting question boss")
    response = chain.invoke({"messages": [HumanMessage(content=f"{data}")]})
    print(response)
    return ""
p = pyaudio.PyAudio()
# # Get stereo device
# for i in range(p.get_device_count()):
#     dev = p.get_device_info_by_index(i)
#     if dev['name'] == 'Stereo Mix (Realtek(R) Audio)':
#         stereo_mix = dev
#         stereo_mix_index = dev['index']

# r = sr.Recognizer()
# with sr.Microphone(device_index=stereo_mix_index) as source:
#     # print("Listening on " + str(stereo_mix_index))
#     print("started")
#     audio = r.listen(source=source)
#     try:
#         print("Started")
#         text:str = r.recognize_whisper(audio, language='english')
#         print(text)
#     except sr.UnknownValueError:
#         print("Wispher is dumb")
#     except sr.RequestError as e:
#         print(f"Whipser not found {e}")
# # with sr.Microphone() as source:
#     print("Say Something")
#     audio = r.listen(source=source, timeout=None)
#     print(source)
# try:
#     text:str = r.recognize_whisper(audio, language='english')
#     if "optimus" in text.lower():
#         print("I am up boss")
#         t = sr.Recognizer()
#         with sr.Microphone() as voice:
#             print("What should I take notes of boss")
#             new_audio = t.listen(source=voice)
#             data:str = t.recognize_whisper(new_audio, language='english')
#             print(data)
#             # talk_with_bot(data)
#     else:
#         print(text)
# except sr.UnknownValueError:
#     print("Wispher is dumb")
# except sr.RequestError as e:
#     print(f"Whipser not found {e}")

# p = pyaudio.PyAudio()
# import wave
# Get stereo device
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if dev['name'] == 'Stereo Mix (Realtek(R) Audio)':
        stereo_mix = dev
        stereo_mix_index = dev['index']
        break
if not stereo_mix:
    print("stereo mix not found")

# stream = p.open(format=pyaudio.paInt16, channels=2, rate=48000, input=True, frames_per_buffer=1024, input_device_index=stereo_mix_index)
# frames = []
# for i in range(0, int(48000 / 1024 * 30)):
#     data = stream.read(1024)
#     frames.append(data)
# stream.stop_stream()
# stream.close()
# p.terminate()
# wf = wave.open('output.wav', 'wb')
# wf.setnchannels(2)
# wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
# wf.setframerate(48000)
# wf.writeframes(b''.join(frames))
# wf.close()

# from os import path
# r = sr.Recognizer()
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)),"output.wav")
# with sr.AudioFile(AUDIO_FILE) as source:
#     # print("Listening on " + str(stereo_mix_index))
#     print("started")
#     audio = r.listen(source=source)
#     try:
#         print("Started")
#         text:str = r.recognize_whisper(audio, language='english')
#         print(text)
#     except sr.UnknownValueError:
#         print("Wispher is dumb")
#     except sr.RequestError as e:
#         print(f"Whipser not found {e}")

r = sr.Recognizer()
with sr.Microphone(device_index=stereo_mix_index,sample_rate=48000) as source:
    print("started")
    audio = r.listen(source=source, timeout=60000, phrase_time_limit=20000)
    try:
        print("Started")
        text:str = r.recognize_whisper(audio, language='english')
        summary(text)        
        print(text)
    except sr.UnknownValueError:
        print("Wispher is dumb")
    except sr.RequestError as e:
        print(f"Whipser not found {e}")
