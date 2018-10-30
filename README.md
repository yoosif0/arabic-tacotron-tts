



* python .\preprocess.py --dataset nawar
* python .\train.py --restore_step 201000
* python .\demo_server.py --checkpoint C:\Users\User\tacotron\logs-tacotron\model.ckpt-70000
* python -m pytest

Remember to delete the files in training folder then preprocess again if you changed the config
# Arabic Tacotron TTS

An implementation of Tacotron speech synthesis in TensorFlow for Arabic. 


### Audio Samples

Check **[Audio Samples](https://youssefsharief.github.io/arabic-tacotron-tts/)** from models trained using this repo on [Nawar Halabi's speech corpus](http://en.arabicspeechcorpus.com/)


## Background

In April 2017, Google published a paper, [Tacotron: Towards End-to-End Speech Synthesis](https://arxiv.org/pdf/1703.10135.pdf),
where they present a neural text-to-speech model that learns to synthesize speech directly from
(text, audio) pairs. However, they didn't release their source code or training data. This is an attempt to provide an open-source implementation of the model described in their paper.

This implementation is pretty much the same as [Keithito's implemetation](https://github.com/keithito/tacotron). Here are [changes](#changes) I made.


## Quick Start

### Installing dependencies

1. Install Python 3. Use version 3.5 for tensorflow support. You could use anaconda to create a new environment by 
    1. `conda create  -n myenv python=3.5 `
    2. `activate myenv`

2. Install tensorflow   
   * `pip install tensorflow` or `pip install tensorflow-gpu`
  
3. Install other requirements:
   ```
   pip install -r requirements.txt
   ```


### Using a pre-trained model

1. **Download and unpack the [pretrained model](https://drive.google.com/file/d/1c8VaKKKBdhqiwQWvC2K5ut18RKoNfpgg/view?usp=sharing)**
   
2. Extract the model files into a folder in a destination of your choice
   
3. **Run the demo server**:
   ```
   python demo_server.py --checkpoint .\{folder_in_a_destination_of_your_choice}\model.ckpt-200000
   ```

4. **Point your browser at localhost:9200**
   * Type what you want to synthesize. Use only diacritised Arabic text.



### Training

*Note: you need 40GB (more or less) of free disk space to train a model.*

1. **Download a speech dataset.**

   The following are supported out of the box:
    * [Nawar Halabi](http://en.arabicspeechcorpus.com/)

   You can use other datasets if you convert them to the right format. See [TRAINING_DATA.md](TRAINING_DATA.md) for more info.

* Preprocess 
    * Add a folder called nawar_without_hag9 in the tacotron directory in your user folder
        * Add temp_filtered.csv there
        * Add a folder called wavs there in which all wav files are there
    * Run `python .\preprocess.py --dataset nawar`
* Update max_iters to 400 if not already set to that number
* Train
    * `python .\train.py`


1. **Unpack the dataset into `~/tacotron`**

   After unpacking, your tree should look like this for Nawar Halabi's Speech Corpus:
   ```
   tacotron
     |- nawar
         |- temp.csv
         |- wavs
   ```

2. **Preprocess the data**
   ```
   python3 preprocess.py --dataset nawar
   ```
     * Use `--dataset nawar` for Nawar Halabi's data

3. **Train a model**
   ```
   python3 train.py
   ```

   Tunable hyperparameters are found in [hparams.py](hparams.py). You can adjust these at the command
   line using the `--hparams` flag, for example `--hparams="batch_size=16,outputs_per_step=2"`.
   Hyperparameters should generally be set to the same values at both training and eval time.
   See [TRAINING_DATA.md](TRAINING_DATA.md) for other languages.


4. **Monitor with Tensorboard** (optional)
   ```
   tensorboard --logdir ~/tacotron/logs-tacotron
   ```

   The trainer dumps audio and alignments every 1000 steps. You can find these in
   `~/tacotron/logs-tacotron`.

5. **Demo server for evaluation** 
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

## Thanks to
Dr. Taha Zerrouki, Dr. Motaz Saad, Dr. Nawar Halabi, Dr. Basem Ahmed, Suhail Kwailat, and Leo Ma for their descriptive feedback and recommendations.
