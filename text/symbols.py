'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
import os

_pad        = '_'
_eos        = '~'
_characters = '\'(),-.:;?'
_arabic_characters = ['ز', 'ح', 'ِ', 'و', 'ذ', 'غ', 'ط', 'ش', 'ى', 'ئ', 'ر', 'ُ', 'خ', 'ظ', 'س', 'ك', 'ء', 'ٌ', 'ت', 'ؤ', 'ه', 'ض', 'ْ', 'د', 'ج', 'ٍ', 'ل', 'ص', 'آ', 'ع', 'ً', 'ّ',
 'ن', 'أ', 'إ', 'ب', 'ق', 'ف', 'ا', 'ة', 'م', 'ث', 'ي', 'َ', ''] 

# Export all symbols:
symbols = [_pad, _eos] + list(_characters) + _arabic_characters
