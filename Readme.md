> Dataset : We have used [Top 2000 Records](https://clinicaltrials.gov/search)

> This Dataset is Conveted to .parquet file (Similar to .csv)

> [Here](https://github.com/sanchit339/Raykor) is the code for that.

> Below is the Json and the Coverted text record.
```
    Example Json :
    "identificationModule": {
        "nctId": "NCT06390072",
            "orgStudyIdInfo": {
                "id": "23-X-71"
                },
                "briefTitle": "Project Hypnos: The Impact of a Brief Hypnosis Intervention on Single-limb Dynamic Balance in People With Chronic Ankle Instability"
    },

    Here is the Conversion :

    identificationModule nctId: NCT06390072, orgStudyIdInfo id: 23-X-71, briefTitle: Project Hypnos: The Impact of a Brief Hypnosis Intervention on Single-limb Dynamic Balance in People With Chronic Ankle Instability,

```

> Conversion : json -> text then text to .parquet

> This dataset to be used is uploaded on [HuggingFace](https://huggingface.co/datasets/hackint0sh/small-data).

> With [this](https://colab.research.google.com/drive/1Bnzy_lzENKtJBWWia7qsbnolLLQ0ec6U?usp=sharing)
 code we can have inference with the model.


- The code takes 2-3 Mins to Download and Load the libraries.
- Depending on the GPU Memeory the training time differs.
- The current code has been set to use the max available GPU memeory. 
- We can modify it my changing the `batch_size`

- Click on Run All 
![Img](./RunAll.jpg)

- After the Model is FineTuned on the dataset Give the prompt.