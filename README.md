### Roop Api

Roop Api is a simple Rest api that allows you to use roop for faceswaping

## Setup

1.  Ensure you have python installed on your machine
2.  Ensure you have micromamba installed on your machine
3.  Clone the repository
4.  Run the ansible playbook to install the required dependencies

## Running

1. Ensure your virtual environment is activated by running the following command
   `micromamba activate face_api`
2. Run the following command to start the server
   `uvicorn main:app --reload`

## Patch

1. go to /home/{{user}}/micromamba/envs/myenv/lib/python3.11/site-packages/basicsr/data/degradations.py
2. Replace

```
   from torchvision.transforms.functional_tensor import rgb_to_grayscale
   from torchvision.transforms.functional import rgb_to_grayscale
```
