from faster_whisper import WhisperModel
import sys
model = WhisperModel("base.en")

segments, info = model.transcribe(sys.argv[1])

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))