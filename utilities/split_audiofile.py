from pydub import AudioSegment
import os
import shutil
import math

def split_audiofile(chunk_duration, audio_path, results_path):
    # Split all audios from 'audio_path' into chunks with 'chunk_duration' miliseconds duration
    # and the results goes to 'results_path'
    audio = AudioSegment.from_file(audio_path)
    audio_duration = len(audio)
    filename = audio_path.split('/')[1]
    extension = audio_path.split('.')[1]

    print('File', filename)
    print('Audio duration:', audio_duration)
    if audio_duration <= chunk_duration:
        print(f'Too short to chunk. Copying the original audiofile to {results_path}')
        shutil.copyfile(audio_path, os.path.join(results_path, filename))
    else:
        num_chunks = math.ceil(audio_duration / chunk_duration)
        print(f'Number of chunks: {num_chunks}')
        for i in range(0, num_chunks):
            audio_chunk = audio[chunk_duration*i:chunk_duration*(i+1)]
            chunk_filename = filename.split('.')[0] + "_{0:03}".format(i) + '.' + extension
            audio_chunk.export(
                os.path.join(results_path, chunk_filename), format=extension)
            print(f'{chunk_filename} chunk copied to {results_path}')

if __name__ == "__main__":
    chunk_duration = 30000 #miliseconds
    audio_path = 'audio_samples/'
    results_path = 'results/'
    audio_formats_tuple = ('.wav', '.mp3')
    for audiofile in os.listdir(audio_path):
        if audiofile.endswith(audio_formats_tuple):
            split_audiofile(chunk_duration, os.path.join(audio_path, audiofile), results_path)
        print("\n")