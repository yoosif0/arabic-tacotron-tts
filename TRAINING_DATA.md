# Training Data


This repo supports the following speech dataset:
  * [Nawar Halabi](http://en.arabicspeechcorpus.com/)

You can use any other dataset if you write a preprocessor for it.


### Writing a Preprocessor

Each training example consists of:
  1. The text that was spoken
  2. A mel-scale spectrogram of the audio
  3. A linear-scale spectrogram of the audio

The preprocessor is responsible for generating these. See [nawar.py](datasets/nawar.py) for a
commented example.

For each training example, a preprocessor should:

  1. Load the audio file:
     ```python
     wav = audio.load_wav(wav_path)
     ```

  2. Compute linear-scale and mel-scale spectrograms (float32 numpy arrays):
     ```python
     spectrogram = audio.spectrogram(wav).astype(np.float32)
     mel_spectrogram = audio.melspectrogram(wav).astype(np.float32)
     ```

  3. Save the spectrograms to disk:
     ```python
     np.save(os.path.join(out_dir, spectrogram_filename), spectrogram.T, allow_pickle=False)
     np.save(os.path.join(out_dir, mel_spectrogram_filename), mel_spectrogram.T,  allow_pickle=False)
     ```
     Note that the transpose of the matrix returned by `audio.spectrogram` is saved so that it's
     in time-major format.

  4. Generate a tuple `(spectrogram_filename, mel_spectrogram_filename, n_frames, text)` to
     write to train.txt. n_frames is just the length of the time axis of the spectrogram.


After you've written your preprocessor, you can add it to [preprocess.py](preprocess.py) by
following the example of the other preprocessors in that file.

