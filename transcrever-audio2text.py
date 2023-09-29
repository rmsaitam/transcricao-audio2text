import sys
import whisper

if len(sys.argv) != 2:
    print("Uso: python script.py <arquivo_de_audio>")
    sys.exit(1)

arquivo_de_audio = sys.argv[1]

try:
    modelo = whisper.load_model("base")
    resposta = modelo.transcribe(arquivo_de_audio)
    print(resposta["text"])
except Exception as e:
    print(f"Erro ao transcrever o arquivo de áudio: {str(e)}")

