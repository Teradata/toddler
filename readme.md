# Teradata Open Domain Dynamic Library for Extraction of Responses (Toddler)

As with any toddler you present Toddler with information and it will respond with a lot of questions :) 

Now seriously...

Large Language Models (LLMs) are trained on extensive corpora of data. These corpora cannot include every piece of information that might be needed by users. Retrieval Augmented Generation (RAG) and fine-tuning are commonly used techniques to incorporate knowledge beyond the initial training data in the responses provided by LLMs.

Retrieval Augmented Generation: RAG involves crafting a highly relevant narrow context as part of a prompt sent to the model, effectively retrieving and integrating external information in real-time.

Fine-Tuning: Fine-tuning adjusts the model parameters through extra rounds of training on relevant data, tailoring the model to specific contexts or domains of interest.

Both techniques benefit significantly from having relevant data in the form of questions and answers, as this is the primary interaction format for the model. However, raw data is rarely structured this way.

The purpose of Toddler is to provide a tool that processes a given document (currently, PDFs are supported) and uses an LLM (currently, only the OpenAI API is supported) to generate a JSON array of questions and answers based on the provided document.

This JSON array can later be used as a dataset for RAG or fine-tuning, enhancing the model's performance and relevance in specific applications. For instance, Toddler can help create custom datasets for educational tools, customer support systems, or specialized knowledge bases.

## Requirements
- You need to provide an API Key for OpenAI API, currently the only LLM platform supported (Welcome to contribute adding more)
    - The key should be added in a .env file
- All other requirements are installed through the installation process before.

## Installation

```bash
git clone "https://github.com/teradata/toddler.git"
cd toddler
python -m venv venv
./venv/Scripts/Activate # for unix based OS source ./venv/bin/activate
pip install .
```

## To use Toddler
- You need to provide the path to your target pdf document
- The inuitial and final page you want to process
- The name of your output file don't include the .json extension, it comes by default
    - The directory is also defined by default as outputs

```bash
python python toddler/inquire.py <"your pdf full path"> <"initial page"> <"final page"> <"new_output">
```
## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request



Distributed under the Apache 2.0 License. See `LICENSE` for more information.

Contact
Reach out to us in the Teradata Community https://support.teradata.com/community