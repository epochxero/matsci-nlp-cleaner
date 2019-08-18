### Set up

1. Make sure you have `python3.6` and the `pip` module installed. 
We recommend using [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
1. Navigate to the root folder of this repository (the same folder that contains this README file)
and run `pip install -r requirements.txt`. Note: If you are using a conda env and any packages fail to compile during this step, you may need to first install those packages separately with `conda install package_name`. 
1. Wait for all the requirements to be downloaded and installed.
1. Run `python setup.py install` to install this module. This will also download the Word2vec model files.
If the download fails, manually download the [model](https://storage.googleapis.com/mat2vec/pretrained_embeddings), 
[word embeddings](https://storage.googleapis.com/mat2vec/pretrained_embeddings.wv.vectors.npy) and 
[output embeddings](https://storage.googleapis.com/mat2vec/pretrained_embeddings.trainables.syn1neg.npy) and put them in mat2vec/training/models.
1. Finalize your chemdataextractor installation by executing ``cde data download`` (You may need to restart your virtual environment for the cde command line interface to be found).
1. You are ready to go!

#### Processing

Example python usage:

```python
from mat2vec.processing import MaterialsTextProcessor
text_processor = MaterialsTextProcessor()
text_processor.process("LiCoO2 is a battery cathode material.")
```
> (['CoLiO2', 'is', 'a', 'battery', 'cathode', 'material', '.'], [('LiCoO2', 'CoLiO2')])

For the various methods and options see the docstrings in the code.
