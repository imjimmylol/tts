import time
import torch
from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.tts_inference import Text2Speech
from parallel_wavegan.utils import download_pretrained_model
from parallel_wavegan.utils import load_model
import os
import scipy.io.wavfile
#
lang = 'Mandarin'
fs = 24000
tag = 'kan-bayashi/csmsc_conformer_fastspeech2'
vocoder_tag = "csmsc_parallel_wavegan.v1"

d = ModelDownloader()
text2speech = Text2Speech(
    **d.download_and_unpack(tag),
    device="cpu",
    threshold=0.5,
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=False,
    backward_window=1,
    forward_window=3,
    speed_control_alpha=1.0,
)
text2speech.spc2wav = None
vocoder = load_model(download_pretrained_model(vocoder_tag)).to("cpu").eval()
vocoder.remove_weight_norm()

def ch_ttw(text):
    with torch.no_grad():
        start = time.time()
        wav, c, *_ = text2speech(text)
        wav = vocoder.inference(c)
    rtf = (time.time() - start) / (len(wav) / fs)
    res_array = wav.view(-1).cpu().numpy()
    scipy.io.wavfile.write((os.getcwd()+"/tts/static/audio_src/tmp.wav"), 24000, res_array)
    res = {"wav_array": str(list(res_array)), "rtf": rtf, "wav dir": (os.getcwd()+"/tts/static/audio_src/tmp.wav")}
    return res


# def test():
#     return {"wav_array": "it works", "rtf": "0.ch123"}
