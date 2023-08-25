from typing import Literal, Optional
from invokeai.app.invocations.baseinvocation import BaseInvocation, InvocationContext
from .prompt import PromptOutput
import requests
from pydantic import BaseModel, Field
import time
import random

class OobaboogaInvocation(BaseInvocation):
    """Oobabooga Prompt Generator node"""

    # fmt: off
    type: Literal["oobabooga"] = "oobabooga"

    # Inputs
    oobaContext: str =  Field(default="fill the details in the stable diffusion prompt the user enters. Please be as detailed as possible. Don't ask the user for information, but fill in the blanks for him. Be creative! User prompt :", description="context")
    prompt: str = Field(default="")
    max_tokens: int = Field(default=300, description="maximum number of token to generate")
    temperature: float = Field(default=1.31)
    seed: int = Field(default=-1)
    trigger: int = Field(default=0, description="Used to trigger the generator without changing values")
    # For local streaming, the websockets are hosted without ssl - http://
    HOST = Field(default="localhost:5000", description="host:port")


    # For reverse-proxied streaming, the remote will likely host with ssl - https://
    # URI = 'https://your-uri-here.trycloudflare.com/api/v1/generate'

    #fmt: on
    def run(self):
        random.seed()
        r=random.randint(0,5)
        time.sleep(3+r)
        request = {
            'prompt': self.oobaContext+"\n"+self.prompt+"\n",
            'max_new_tokens': self.max_tokens,

            # Generation params. If 'preset' is set to different than 'None', the values
            # in presets/preset-name.yaml are used instead of the individual numbers.
            'preset': 'None',
            'do_sample': True,
            'temperature': self.temperature,
            'top_p': 0.29,
            'typical_p': 1,
            'epsilon_cutoff': 0,  # In units of 1e-4
            'eta_cutoff': 0,  # In units of 1e-4
            'tfs': 1,
            'top_a': 0,
            'repetition_penalty': 1.09,
            'repetition_penalty_range': 0,
            'top_k': 72,
            'min_length': 0,
            'no_repeat_ngram_size': 0,
            'num_beams': 1,
            'penalty_alpha': 0,
            'length_penalty': 1,
            'early_stopping': False,
            'mirostat_mode': 0,
            'mirostat_tau': 5,
            'mirostat_eta': 0.1,
            'seed': self.seed,
            'add_bos_token': True,
            'truncation_length': 2048,
            'ban_eos_token': False,
            'skip_special_tokens': True,
            'stopping_strings': []
        }

        URI = f"http://{self.HOST}/api/v1/generate"
        response = requests.post(URI, json=request)
        generatedPrompt = str(response.json()['results'][0]['text']).replace("AI:","")
        print(f"\nGenerated prompt: {generatedPrompt}\nSeed:{self.seed}\nTemp:{self.temperature}\n")
        response = ""
        return generatedPrompt

    # fmt: on
    def invoke(self, context: InvocationContext) -> PromptOutput:
           return PromptOutput(
            prompt=self.run(),
        )






