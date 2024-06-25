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

### Get questions from a PDF
- You need to provide the path to your target pdf document
- The initial and final page you want to process
- The name of your output file don't include the .json extension, it comes by default
    - The directory is also defined by default as outputs

```bash
python toddler/inquire.py <"your pdf full path"> <"initial page"> <"final page"> <"new_output">
```

### Get questions from a PDF
- You need to provide the path to your target json document (this should be the output of inquire.py)

- The name of your output file don't include the .json extension, it comes by default
    - The directory is also defined by default as outputs
- The name of your output file don't include the .json extension, it comes by default
    - The directory is also defined by default as outputs
- The output will look like this
```json
{"messages": [{"role": "system", "content": "you are becoming an expert on Teradata in-database analytics functions"}, {"role": "user", "content": "What are the functions used for handling outliers in data cleaning?"}, {"role": "assistant", "content": "The functions used for handling outliers are TD_GetFutileColumns, TD_OutlierFilterFit, and TD_OutlierFilterTransform."}]}
{"messages": [{"role": "system", "content": "you are becoming an expert on Teradata in-database analytics functions"}, {"role": "user", "content": "Which function is used to handle missing values in data cleaning?"}, {"role": "assistant", "content": "The function used to handle missing values is TD_SimpleImputeFit."}]}
{"messages": [{"role": "system", "content": "you are becoming an expert on Teradata in-database analytics functions"}, {"role": "user", "content": "What is the purpose of the TD_GetRowsWithoutMissingValues function?"}, {"role": "assistant", "content": "The purpose of the TD_GetRowsWithoutMissingValues function is to get rows without missing values in the data."}]}
{"messages": [{"role": "system", "content": "you are becoming an expert on Teradata in-database analytics functions"}, {"role": "user", "content": "Which functions are related to parsing data in data cleaning?"}, {"role": "assistant", "content": "The functions related to parsing data are Pack, StringSimilarity, TD_ConvertTo, and Unpack."}]}
{"messages": [{"role": "system", "content": "you are becoming an expert on Teradata in-database analytics functions"}, {"role": "user", "content": "What is the main purpose of the Pack function?"}, {"role": "assistant", "content": "The main purpose of the Pack function is to pack data from multiple input columns into a single column, simplifying and organizing data sets."}]}
{"messages": [{"role": "system", "content": "you are becoming an expert on Teradata in-database analytics functions"}, {"role": "user", "content": "How are virtual columns created in the packed column by the Pack function identified?"}, {"role": "assistant", "content": "Virtual columns created by the Pack function are identified by their column name and separated by commas in the packed column."}]}
```
- You should provide the content of the system message, like in this case "you are becoming an expert on Teradata in-database analytics functions"
```bash
python <"input file"> <"output file"> "you are becoming an expert on Teradata in-database analytics functions"
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