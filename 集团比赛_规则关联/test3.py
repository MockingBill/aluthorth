try:
    import wave
    import audiosegment
    wave_path1="./1.wav"
    wave_path2="./2.wav"
    v1 = audiosegment.from_file(wave_path1)
    v2 = audiosegment.from_file(wave_path2)
    print(v1)
    print(v2)
except Exception as e:
    pass
# with wave.open(wave_path1,"rb") as f1:
#     with wave.open(wave_path2,"rb") as f2:
#         print(f1.getparams())
#         print(f2.getparams())