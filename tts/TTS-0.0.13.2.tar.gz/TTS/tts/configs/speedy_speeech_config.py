from dataclasses import asdict, dataclass
from typing import List

from coqpit import check_argument

from TTS.tts.configs.commons import BaseTTSConfig, GSTConfig


@dataclass
class SpeedySpeechConfig(BaseTTSConfig):
    """Defines parameters for Speedy Speech (feed-forward encoder-decoder) based models."""

    model: str = "speedy_speech"
    # model specific params
    positional_encoding: bool = True
    hidden_channels: int = 128
    encoder_type: str = "residual_conv_bn"  # TODO: enum?
    encoder_params: dict = {}
    decoder_type: str = 'residual_conv_bn'
    decoder_params: dict = {}

    # multi-speaker settings
    use_speaker_embedding: bool = False
    use_external_speaker_embedding_file: bool = False
    external_speaker_embedding_file: str = False

    # optimizer parameters
    noam_schedule: bool = False
    warmup_steps: int = 4000
    lr: float = 1e-4
    wd: float = 1e-6
    grad_clip: float = 5.0
    seq_len_norm: bool = False
    loss_masking: bool = True

    # loss params
    decoder_loss_alpha: float = 0.25
    postnet_loss_alpha: float = 0.25
    postnet_diff_spec_alpha: float = 0.25
    decoder_diff_spec_alpha: float = 0.25
    decoder_ssim_alpha: float = 0.25
    postnet_ssim_alpha: float = 0.25
    ga_alpha: float = 5.0