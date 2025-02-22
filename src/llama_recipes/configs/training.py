# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from dataclasses import dataclass
import json

@dataclass
class train_config:
    model_name: str="PATH/to/LLAMA/7B"
    rope_scaling: str=json.dumps({"type": "dynamic", "factor": 2.0})
    enable_fsdp: bool=False
    low_cpu_fsdp: bool=False
    batch_size_training: int=4
    gradient_accumulation_steps: int=1
    gradient_clipping: bool = True
    gradient_clipping_threshold: float = 1.0
    num_epochs: int=3
    num_workers_dataloader: int=1
    lr: float=5e-4
    weight_decay: float=0.0
    gamma: float= 0.85
    seed: int=27
    use_fp16: bool=False
    mixed_precision: bool=True
    val_batch_size: int=1
    peft_method: str = "lora" # None , llama_adapter, prefix, pept, v1
    use_peft: bool=False
    output_dir: str = "PATH/to/save/PEFT/model"
    freeze_layers: bool = False
    num_freeze_layers: int = 1
    quantization: bool = False
    one_gpu: bool = False
    save_model: bool = True
    dist_checkpoint_root_folder: str="PATH/to/save/FSDP/model" # will be used if using FSDP
    dist_checkpoint_folder: str="fine-tuned" # will be used if using FSDP
    save_optimizer: bool=False # will be used if using FSDP
    use_fast_kernels: bool = False # Enable using SDPA from PyTroch Accelerated Transformers, make use Flash Attention and Xformer memory-efficient kernels
    save_metrics: bool = False # saves training metrics to a json file for later plotting
    