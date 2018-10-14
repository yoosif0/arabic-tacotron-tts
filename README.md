



* python .\preprocess.py --dataset nawar
* python .\train.py --restore_step 201000
* python .\demo_server.py --checkpoint C:\Users\User\tacotron\logs-tacotron\model.ckpt-70000
* python -m pytest

Remember to delete the files in training folder then preprocess again if you changed the config
# Arabic Tacotron TTS

An implementation of Tacotron speech synthesis in TensorFlow for Arabic. This implementation is pretty much the same as [Keithito's implemetation](https://github.com/keithito/tacotron). Here are [changes](#changes) I made.


### Audio Samples

  * **[Audio Samples](https://keithito.github.io/audio-samples/)** from models trained using this repo.
    * The first set was trained for 441K steps on the [LJ Speech Dataset](https://keithito.com/LJ-Speech-Dataset/)
      * Speech started to become intelligble around 20K steps.
    * The second set was trained by [@MXGray](https://github.com/MXGray) for 140K steps on the [Nancy Corpus](http://www.cstr.ed.ac.uk/projects/blizzard/2011/lessac_blizzard2011/).


### Recent Updates

1. @npuichigo [fixed](https://github.com/keithito/tacotron/pull/205) a bug where dropout was not being applied in the prenet.

2. @begeekmyfriend created a [fork](https://github.com/begeekmyfriend/tacotron) that adds location-sensitive attention and the stop token from the [Tacotron 2](https://arxiv.org/abs/1712.05884) paper. This can greatly reduce the amount of data required to train a model.


## Background

In April 2017, Google published a paper, [Tacotron: Towards End-to-End Speech Synthesis](https://arxiv.org/pdf/1703.10135.pdf),
where they present a neural text-to-speech model that learns to synthesize speech directly from
(text, audio) pairs. However, they didn't release their source code or training data. This is an
independent attempt to provide an open-source implementation of the model described in their paper.

The quality isn't as good as Google's demo yet, but hopefully it will get there someday :-).
Pull requests are welcome!



## Quick Start

### Installing dependencies

1. Install Python 3.

2. Install the latest version of [TensorFlow](https://www.tensorflow.org/install/) for your platform. For better
   performance, install with GPU support if it's available. This code works with TensorFlow 1.3 and later.

3. Install requirements:
   ```
   pip install -r requirements.txt
   ```


### Using a pre-trained model

1. **Download and unpack a model**:
   ```
   curl http://data.keithito.com/data/speech/tacotron-20180906.tar.gz | tar xzC /tmp
   ```

2. **Run the demo server**:
   ```
   python3 demo_server.py --checkpoint /tmp/tacotron-20180906/model.ckpt
   ```

3. **Point your browser at localhost:9000**
   * Type what you want to synthesize



### Training

*Note: you need 40GB or more of free disk space to train a model.*

1. **Download a speech dataset.**

   The following are supported out of the box:
    * [Nawar Halabi](http://en.arabicspeechcorpus.com/)

   You can use other datasets if you convert them to the right format. See [TRAINING_DATA.md](TRAINING_DATA.md) for more info.


2. **Unpack the dataset into `~/tacotron`**

   After unpacking, your tree should look like this for Nawar Halabi's Speech Corpus:
   ```
   tacotron
     |- nawar
         |- temp.csv
         |- wavs
   ```

3. **Preprocess the data**
   ```
   python3 preprocess.py --dataset nawar
   ```
     * Use `--dataset nawar` for Nawar Halabi's data

4. **Train a model**
   ```
   python3 train.py
   ```

   Tunable hyperparameters are found in [hparams.py](hparams.py). You can adjust these at the command
   line using the `--hparams` flag, for example `--hparams="batch_size=16,outputs_per_step=2"`.
   Hyperparameters should generally be set to the same values at both training and eval time.
   See [TRAINING_DATA.md](TRAINING_DATA.md) for other languages.


5. **Monitor with Tensorboard** (optional)
   ```
   tensorboard --logdir ~/tacotron/logs-tacotron
   ```

   The trainer dumps audio and alignments every 1000 steps. You can find these in
   `~/tacotron/logs-tacotron`.

6. **Demo server for evaluation** 
   ```powershell
   python .\demo_server.py --checkpoint C:\Users\User\tacotron\logs-tacotron\model.ckpt-70000
   ```

## Notes and Common Issues

  * If you pass a Slack incoming webhook URL as the `--slack_url` flag to train.py, it will send
    you progress updates every 1000 steps.



## <a name="changes"></a> Changes from the original repo
1. add Arabic speech corpus preprocessing stuff
2. host Arabic trained model based on Nawar Halabi's Speech Corpus
3. update hparams to work with the Arabic speech corpus
4. add instructional explanation on how to reproduce
5. add Arabic specific tests
6. remove some of the unused code
7. update symbols to match the Arabic phonetic language
8. adjust data-feeder so that all input text are phonetised by [arabic_pronounce](https://github.com/youssefsharief/arabic_pronounce)

## To Do
* Add cleaners
* Add embedded diacritiser