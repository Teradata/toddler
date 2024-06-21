# Teradata Open Domain Dynamic Library for Extraction of Responses (Toddler)

Widely available Large Language Models are trained over large corpuses of data. These corpuses of data cannot include every piece of information that might be needed by its users. Retrieval Augmented Generation (RAG) and Fine Tuning are commonly used techniques to incorporate knowledge that goes beyond their initial training data in the responses provided by LLMs.

Both Retrieval Augmented Generation and Fine Tuning rely on incorporating new data, either by  crafting a highly relevant narrow context as part of a prompt sent to the model, or by adjusting the model parameters while performing extra rounds of training on relevant data as to their context of interest.

In both scenarios having relevant data in the form of questions and answers is beneficial, since this is the format of text that the model will interact with most of the time. The raw data that needs to be incorporated though, is rarely in this format. 

The purpose of Toddler is to provide a tool that allows inputting a given document (currently pdfs are supported) to an LLM (currently only OpenAI API is supported) to retrieve a JSON array of questions and answers based on the provided document.

This JSON array can be used later as a dataset for RAG or fine tuning.

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